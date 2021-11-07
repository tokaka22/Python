'''
BORDER_REPLICATE:边界复制
        BORDER_CONSTANT:常数扩充
        BORDER_REFLECT:反射扩充
        BORDER_REFLECT_101:以边界为中心反射扩充
        BORDER_WRAP:平铺扩充
'''
import cv2

src=cv2.imread(r'OpenCV\lena.jpg',1)
replicate=cv2.copyMakeBorder(src,src.shape[0],src.shape[0],src.shape[0],src.shape[0],borderType=cv2.BORDER_REPLICATE)
constant=cv2.copyMakeBorder(src,src.shape[0],src.shape[0],src.shape[0],src.shape[0],borderType=cv2.BORDER_CONSTANT)
reflect=cv2.copyMakeBorder(src,src.shape[0],src.shape[0],src.shape[0],src.shape[0],borderType=cv2.BORDER_REFLECT)
reflect_101=cv2.copyMakeBorder(src,src.shape[0],src.shape[0],src.shape[0],src.shape[0],borderType=cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(src,src.shape[0],src.shape[0],src.shape[0],src.shape[0],borderType=cv2.BORDER_WRAP)
cv2.imshow('replicate',replicate)
cv2.waitKey(0)
cv2.imshow('constant',constant)
cv2.waitKey(0)
cv2.imshow('reflect',reflect)
cv2.waitKey(0)
cv2.imshow('reflect_101',reflect_101)
cv2.waitKey(0)
cv2.imshow('wrap',wrap)
cv2.waitKey(0)
cv2.destroyAllWindows()