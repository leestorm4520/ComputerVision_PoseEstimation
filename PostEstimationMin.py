import cv2
import mediapipe as mp
import time

mpPose=mp.solutions.pose
pose=mpPose.Pose()
cap=cv2.VideoCapture("examples_media_video.avi")
pTime=0

while True: 
    success, img= cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result=pose.process(imgRGB)
    print(result)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()