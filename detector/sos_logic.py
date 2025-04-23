from .stages import Stages
import time 

class SOSdetector(Stages):
    def __init__(self):
        super().__init__()
        
        self.current_stage = 0
        self.start_time = time.time()
        self.end_time = time.time()
        
    
    def detect_hand_signal(self, hand_landmarks):
        """Detect SOS hand signal"""
        
        if self.current_stage == 0 and self._stage1(hand_landmarks):
            self.current_stage = 1
        
        if self.current_stage == 1 and self._stage2(hand_landmarks):
            self.current_stage = 2
            self.start_time = time.time()
        
        if self.current_stage == 2 and self._stage3(hand_landmarks):
            self.current_stage = 3
                
        if self.current_stage == 3 and self._stage2(hand_landmarks):
            self.current_stage = 4
            self.end_time = time.time()

        if self.current_stage == 4:
            if self.end_time - self.start_time < 3:
                return "SOS DETECTION"
            else:
                self.current_stage = 0

        if time.time() - self.start_time > 3:
            self.current_stage = 0
            
        return "No SOS"
