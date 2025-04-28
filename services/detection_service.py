import cv2
import mediapipe as mp
from detector.sos_logic import SOSdetector
from utils.image_utils import save_image, show_normal, show_SOS
from config.settings import DETECTION_CONFIDENCE, TRACKING_CONFIDENCE
import time  
from .message_service import send_email

class DetectionService:
    def __init__(self, 
                detector = None,
                image_flip = True,
                only_right_hand = False,
                send_email = False):
        
        # Mediapipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence = DETECTION_CONFIDENCE,
                                         min_tracking_confidence = TRACKING_CONFIDENCE)
        self.mp_drawing = mp.solutions.drawing_utils
        
        # Detector and user param
        if detector:
            self.detector = detector()
        else: 
            self.detector = SOSdetector()
            
        self.image_flip = image_flip
        self.only_right_hand = only_right_hand 
        self.send_email = send_email
        
        # SOS detect show in 3 seconds
        self.sos_detected_time = None 
        self.sos_display_duration = 3 
        
    def run(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, image = cap.read()
            if not ret:
                break

            # Process image
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Check if SOS is still being displayed
            if self.sos_detected_time is not None:
                elapsed_time = time.time() - self.sos_detected_time
                if elapsed_time < self.sos_display_duration:
                    show_SOS(image)
                    cv2.imshow("Hand Signal Detection", image)
                    if cv2.waitKey(5) & 0xFF == 27:
                        break
                    continue # continue showing (jump over the loop)
                else:
                     # Reset after 3 seconds
                    self.sos_detected_time = None 
                    self.detector.current_stage = 0  

            # Process hand detection
            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]
                self.mp_drawing.draw_landmarks(image, hand, self.mp_hands.HAND_CONNECTIONS)
                signal = self.detector.detect_hand_signal(hand.landmark)
                if signal == "SOS DETECTION":
                    self.sos_detected_time = time.time()  
                    image_path, formated_time = save_image(image) 
                    
                    if self.send_email:
                        subject = "SOS Detector Alert"
                        text_content = f"Your camera has detected a SOS handsign case at {formated_time}, please check out this attach image"
                        send_email(subject, text_content, image_path)
                    show_SOS(image)
                else: show_normal(image, text="No SOS detected")  # No SOS handsign
            else: show_normal(image, text="No hand detected")  # No hand
            
            cv2.imshow("Hand Signal Detection", image)
            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()