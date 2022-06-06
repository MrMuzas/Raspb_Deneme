import cv2
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_locations, face_names = sfr.detect_known_faces(frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
