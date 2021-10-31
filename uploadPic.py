import dropbox
import cv2
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        img_name = "img"+str(number)+'.jpg'
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return img_name
    print('Image is taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "BFI_FXSPClEAAAAAAAAAAfone_twEtfiAL3zc0UdGMxOdSvbjE3sWQLPFTpJfILT"
    file = img_name
    file_to = "/testFolder"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while (True):
        if ((time.time()-start_time)>= 5):
            name = take_snapshot()
            upload_file(name)
main()
