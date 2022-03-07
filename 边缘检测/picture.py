import cv2
def pic_canny(image):
    img=cv2.imread(image)
    blurred=cv2.GaussianBlur(img,(3,3),0)
    gray=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    xgrad=cv2.Sobel(gray.cv2_16SC1,1,0)
    ygrad = cv2.Sobel(gray.cv2_16SC1, 0, 1)
    output=cv2.Canny(xgrad,ygrad,50,150)
    cv2.imshow("canny",output)
    cv2.waitKey(0)

pic_canny()