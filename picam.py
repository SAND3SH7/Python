from picamera2 import Picamera2
import cv2

cam=Picamera2()
cam.configure(cam.create_preview_configuration())
cam.start()
count=0

while True:
    frame=cam.capture_array()
    cv2.imshow("pi camera",frame)
    key=cv2.waitkey(1)& 0xff
    if key == 32:
        filename=f"photo {i}".jpg
        cv2.imwrite(filename,frame)
        count+=1
    elif key == ord('q'):
        print('quit')
        break
cv2.destroyAllWindows()
cam.stop()