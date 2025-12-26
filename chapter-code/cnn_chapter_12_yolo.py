import cv2
from ultralytics import YOLO

# Load a pre-trained model (let's use the nano version for speed)
model = YOLO('yolov8n.pt')

print("Starting webcam detection...")
print("Point your webcam at different objects and watch the magic!")
print("Press 'q' to quit")

# Real-time detection on webcam
results = model.predict(
    source=0,           # 0 = default webcam
    show=True,       # Display results in a window
    conf=0.5,           # Confidence threshold (only show detections with 50%+ confidence)
    save=False,      # Don't save every frame (we're just watching)
    stream=True,   # For real-time processing
    verbose=False # Less text output for cleaner experience
)

# The magic happens here - it will keep running until you press 'q'
for result in results:
    # The video window will show detections in real-time
    # Try these experiments:
    # - Wave your hand in front of the camera
    # - Show your phone to the camera  
    # - Hold up a book or bottle
    # - See if it detects your face as a "person"
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
print("Webcam detection ended!")

