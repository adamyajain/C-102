import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot() : 
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read frames while camera is on
        ret, frame = videoCaputreObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    #release the camera
    videoCaptureObject.release()
    #closes all the windows that might be open in the process
    cv2.destroyAllWindows()



def upload_file(img_name):
    access_token = "Ar4dR_cJnJY2P3lTN5FcnHA5UcDLCCeMA7fzcnrs4NQRMi_IxYGK5rH96AhH5hjMoVDtBiJ4-hQawWvvkyTVGZu8V_QPeav1mIHnT9ZHLJOAuomDsqN65yzyRu867kzPNo_j2JI"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")


def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()