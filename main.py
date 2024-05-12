from mtcnn import MTCNN
from deepface import DeepFace
import os
import shutil
import time
import cv2


def detect_faces(image):
    detector = MTCNN()
    faces = detector.detect_faces(image)

    output_folder = 'detected/'
    os.makedirs(output_folder, exist_ok=True)

    if faces:
        for i, face_info in enumerate(faces):
            x, y, w, h = face_info['box']

            padding = 20
            face = image[max(0, y - padding):y + h + padding, max(0, x - padding):x + w + padding]
            cv2.imwrite(os.path.join(output_folder, f'face_{i}.jpg'), face)  # Save the cropped face
        print("Faces detected and saved successfully using MTCNN.")
        return True
    else:
        print("No faces detected in the image.")
        return False


def verify_faces():
    a = []
    image_folder = os.listdir("detected")
    for image in image_folder:
        try:
            df = DeepFace.find(img_path=f"detected/{image}", db_path="faces", model_name="Facenet", distance_metric="cosine")
        except:
            print("No Face detected")
            shutil.rmtree("detected")
            print("removed folder detected")
            return
        if 'distance' in df[0] and len(df[0]['distance']) > 0 and df[0]['distance'][0] < 5:
            d = df[0]["identity"][0]
            filename = os.path.basename(d)
            base_name, extension = os.path.splitext(filename)
            a.append(base_name)
    print(a)

    # Clean up detected faces folder
    shutil.rmtree("detected")
    print("removed folder detected")




cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('video.mp4') if you want video file as input


if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()


while True:

    ret, frame = cap.read()


    if not ret:
        print("Error: Failed to capture frame.")
        break


    cv2.imshow('Webcam', frame) #comment it if you don't want to see the captured frames
    if detect_faces(frame):
        time.sleep(1)
        verify_faces()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


