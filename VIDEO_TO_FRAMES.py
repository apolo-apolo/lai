import cv2
import os
 #This code was developed by O. Enrique Apolo Apolo
 #e-mail: eapolo@us.es
 #Departamento de Ingeniería Aeroespacial y Mecánica de Fluidos 
 #Universidad de Sevilla 
def video_to_frame(pathIn, pathOut):
    os.mkdir(pathOut)
 
    cap = cv2.VideoCapture(pathIn)
    count = 1 #Random value for the first frame
 
    while (cap.isOpened()):
 
        # Captura frame por frame
        ret, frame = cap.read()
 
        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "image{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break
 
    
    cap.release()
    cv2.destroyAllWindows()
 
def main():
    video_to_frame('wheat_02.mp4', 'frames_from_video')
 
if __name__=="__main__":
    main()