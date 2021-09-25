'''
cv2.resize 处理图像，新size，resize方法
    resize方法可看：https://blog.csdn.net/JNingWei/article/details/78218837
'''
import cv2

pic = cv2.imread('./Elegent_Girl.jpg')
pic = cv2.resize(pic, (400, 400), interpolation=cv2.INTER_CUBIC)
cv2.imshow('', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
