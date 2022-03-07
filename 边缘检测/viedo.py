import cv2

def viedo_canny(video):
    cap=cv2.VideoCapture(video)
    while 1:
        ret,frame=cap.read()
        img=frame
        if ret :
            img_resize=cv2.resize(img,(1080,608))
            blurred = cv2.GaussianBlur(img_resize, (3, 3), 0)
            gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
            xgrad = cv2.Sobel(gray,cv2.CV_16SC1, 1, 0)
            ygrad = cv2.Sobel(gray,cv2.CV_16SC1, 0, 1)
            output = cv2.Canny(xgrad, ygrad, 50, 150)
            cv2.imshow("video", output)
            if cv2.waitKey(24) & 0xff==27:
                break
        else:
            break
            cap.release()
            cv2.destroyAllWindows()

viedo_canny("《原神》剧情PV-「神女劈观」.《原神》剧情PV-「神女劈观」.mp4")#把MP4格式视频放在根目录下， 然后复制路径到这里，即可运行
