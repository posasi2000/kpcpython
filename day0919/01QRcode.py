# QRcode만들기
'''
ModuleNotFoundError: No module named 'qrcode'
pip install qrcode 

OpenCV = Open Source Computer Vision 라이브러리 
ModuleNotFoundError: No module named 'cv2'
pip install opencv-python
 
pip install cv2 설치아닙니다 
pip list
'''



import qrcode

url = 'https://www.google.com'
qr_img = qrcode.make(url)
qr_img.save(stream='./images/QR_code.png')


import cv2
image = cv2.imread('./images/QR_code.png')
cv2.imshow("title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()






