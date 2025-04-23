class Stages:
    def __init__(self):
        pass
    
    def _stage1(self, hand_landmarks):
        """Stage 1: All fingers (A to E) open""" 
        THUMB_TIP = hand_landmarks[4]
        THUMB_IP = hand_landmarks[3]
        THUMB_MCP = hand_landmarks[2]
        
        INDEX_FINGER_TIP = hand_landmarks[8]
        INDEX_FINGER_PIP = hand_landmarks[6]
        
        MIDDLE_FINGER_TIP = hand_landmarks[12]
        MIDDLE_FINGER_PIP = hand_landmarks[10]
        
        RING_FINGER_TIP = hand_landmarks[16]
        RING_FINGER_PIP = hand_landmarks[14]
        
        PINKY_TIP = hand_landmarks[20]
        PINKY_PIP = hand_landmarks[18]
            
        return (
            THUMB_TIP.y < THUMB_IP.y and THUMB_MCP.y and 
            INDEX_FINGER_TIP.y < INDEX_FINGER_PIP.y and
            MIDDLE_FINGER_TIP.y < MIDDLE_FINGER_PIP.y and
            RING_FINGER_TIP.y < RING_FINGER_PIP.y and
            PINKY_TIP.y < PINKY_PIP.y
        )

    def _stage2(self, hand_landmarks):
        """ Stage 2: Only finger A (thumb) folds and fingers (B to E) open"""
        THUMB_TIP = hand_landmarks[4]
        THUMB_IP = hand_landmarks[3]
        THUMB_MCP = hand_landmarks[2]
        
        INDEX_FINGER_TIP = hand_landmarks[8]
        INDEX_FINGER_PIP = hand_landmarks[6]
        
        MIDDLE_FINGER_TIP = hand_landmarks[12]
        MIDDLE_FINGER_PIP = hand_landmarks[10]
        
        RING_FINGER_TIP = hand_landmarks[16]
        RING_FINGER_PIP = hand_landmarks[14]
        
        PINKY_TIP = hand_landmarks[20]
        PINKY_PIP = hand_landmarks[18]
        return (
            THUMB_TIP.x > THUMB_IP.x and THUMB_IP.x > THUMB_MCP.x and 
            INDEX_FINGER_TIP.y < INDEX_FINGER_PIP.y and
            MIDDLE_FINGER_TIP.y < MIDDLE_FINGER_PIP.y and
            RING_FINGER_TIP.y < RING_FINGER_PIP.y and
            PINKY_TIP.y < PINKY_PIP.y
        )

    def _stage3(self, hand_landmarks):
        """Stage 3: All fingers (B to E) fold over finger A (thumb)"""        
        INDEX_FINGER_TIP = hand_landmarks[8]
        INDEX_FINGER_PIP = hand_landmarks[6]
        
        MIDDLE_FINGER_TIP = hand_landmarks[12]
        MIDDLE_FINGER_PIP = hand_landmarks[10]
        
        RING_FINGER_TIP = hand_landmarks[16]
        RING_FINGER_PIP = hand_landmarks[14]
        
        PINKY_TIP = hand_landmarks[20]
        PINKY_PIP = hand_landmarks[18]

        return (
            INDEX_FINGER_TIP.y > INDEX_FINGER_PIP.y and
            MIDDLE_FINGER_TIP.y > MIDDLE_FINGER_PIP.y and
            RING_FINGER_TIP.y > RING_FINGER_PIP.y and
            PINKY_TIP.y > PINKY_PIP.y
        )    