from services.detection_service import DetectionService 
from detector.sos_logic import SOSdetector

def main():
    service = DetectionService(detector = SOSdetector)
    service.run()
    
if __name__ == "__main__":
    main()