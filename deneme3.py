import face_recognition
import cv2
from time import sleep
#import RPi.GPIO as GPIO


def lock(pin):
    #GPIO.output(pin, GPIO.LOW)
    print('Kilitlendi!')

def unlock(pin):
    #GPIO.output(pin, GPIO.HIGH)
    print('Kilit Açıldı!')

#role_pini = [26]
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(role_pini, GPIO.OUT)
#lock(role_pini)


video_capture = cv2.VideoCapture(0)


#volkan1_image = face_recognition.load_image_file("            ")
#volkan1_face_encoding = face_recognition.face_encodings(volkan1_image)[0]

#volkan2_image = face_recognition.load_image_file("            ")
#volkan2_face_encoding = face_recognition.face_encodings(volkan2_image)[0]

#volkan3_image = face_recognition.load_image_file("            ")
#volkan3_face_encoding = face_recognition.face_encodings(volkan3_image)[0]



#fatih1_image = face_recognition.load_image_file("            ")
#fatih1_face_encoding = face_recognition.face_encodings(fatih1_image)[0]

#fatih2_image = face_recognition.load_image_file("            ")
#fatih2_face_encoding = face_recognition.face_encodings(fatih2_image)[0]

#fatih3_image = face_recognition.load_image_file("            ")
#fatih3_face_encoding = face_recognition.face_encodings(fatih3_image)[0]



#mustafa1_image = face_recognition.load_image_file("            ")
#mustafa1_face_encoding = face_recognition.face_encodings(mustafa1_image)[0]

#mustafa2_image = face_recognition.load_image_file("            ")
#mustafa2_face_encoding = face_recognition.face_encodings(mustafa2_image)[0]

#mustafa3_image = face_recognition.load_image_file("            ")
#mustafa3_face_encoding = face_recognition.face_encodings(mustafa3_image)[0]



arda1_image = face_recognition.load_image_file("            ")
arda1_face_encoding = face_recognition.face_encodings(arda1_image)[0]

arda2_image = face_recognition.load_image_file("            ")
arda2_face_encoding = face_recognition.face_encodings(arda2_image)[0]

arda3_image = face_recognition.load_image_file("            ")
arda3_face_encoding = face_recognition.face_encodings(arda3_image)[0]



known_face_encodings = [

    #volkan1_face_encoding,
    #volkan2_face_encoding,
    #volkan3_face_encoding,

    #fatih1_face_encoding,
    #fatih2_face_encoding,
    #fatih3_face_encoding,

    #mustafa1_face_encoding,
    #mustafa2_face_encoding,
    #mustafa3_face_encoding,

    arda1_face_encoding,
    arda2_face_encoding,
    arda3_face_encoding

]
known_face_names = [
    #"Volkan ASLAN",
    #"Volkan ASLAN",
    #"Volkan ASLAN",
    #"Fatih Ataman SAKIZCI",
    #"Fatih Ataman SAKIZCI",
    #"Fatih Ataman SAKIZCI",
    #"Mustafa DİNÇÇİ",
    #"Mustafa DİNÇÇİ",
    #"Mustafa DİNÇÇİ",
    "Arda KAHRIMAN",
    "Arda KAHRIMAN",
    "Arda KAHRIMAN"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                # unlock() #role_pini
                print("Bravo")
                #if name == "Arda KAHRIMAN":
                    ##unlock() #role_pini
                    #print("Bravo")


            face_names.append(name)
    sleep(1)
    print("Kilitlendi")
    #lock()  #role_pini

    process_this_frame = not process_this_frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#GPIO.cleanup()
video_capture.release()
cv2.destroyAllWindows()

