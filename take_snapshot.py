import cv2

def take_snapshot() : 
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read frames while camera is on
        ret, frame = videoCaputreObject.read()
        #cv2.imwrite() method used to save img on storage device
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False
    #release the camera
    videoCaptureObject.release()
    #closes all the windows that might be open in the process
    cv2.destroyAllWindows()


take_snapshot()    