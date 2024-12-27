# Smile Detection Application Code
# Import necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2

# Paths to the face cascade and pre-trained smile detector CNN
cascade_path = 'D:\Jupyter python\OpenCv\material\haarcascade\haarcascade_frontalface_default.xml'  # Path for haarcascade file
model_path ='D:\Jupyter python\OpenCv\PyCharm\model.h5'  # Path for model.h5 file
             

# Load the face detector cascade and smile detector CNN
detector = cv2.CascadeClassifier(cascade_path)
model = load_model(model_path)

# Open the webcam
print('[INFO] Starting webcam...')
video_path = "D:\Jupyter python\OpenCv\material\Videos\WhatsApp Video 2024-01-27 at 1.23.04 PM.mp4"  # Replace with the path to your video file
camera = cv2.VideoCapture(video_path)
 

# Keep looping
while True:
    # Grab the current frame
    (grabbed, frame) = camera.read()

    # Resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width=700)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the input frame
    rects = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30,30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)

    for (fX, fY, fW, fH) in rects:
        # Extract the ROI of the face from the grayscale image
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (28, 28))
        roi = roi.astype('float') / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        # Determine the probabilities of both 'smiling' and 'not smiling', then set the label accordingly
        (notSmiling, Smiling) = model.predict(roi)[0]
        label = 'Smiling' if Smiling > notSmiling else "Not Smiling"

        # Set the color based on the label
        color = (0, 255, 0) if label == 'Smiling' else (0, 0, 255)

        # Display the label and bounding box on the output frame
        cv2.putText(frame, label, (fX, fY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH), color, 2)

    # Show the frame with smiling/not smiling labels
    cv2.imshow('Smile Detection', frame)

    # If 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
