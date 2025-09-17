
'''
ModuleNotFoundError: No module named 'captcha'
pip install  captcha
'''

from captcha.image import ImageCaptcha
# pip install captcha

#  pip install faker
from faker import Faker
import random

data = Faker() 
name = data.name()
email = data.ascii_email()
print(name)
print(email)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = random.choice(a)
y = random.choice(a)
username, domain = email.split('@')

length=len(username)
total = str(x)+username[0:length-3]+str(y)+username[length-4:length]
print(total)
print()

image = ImageCaptcha(width=350, height=120)
txt_captcha = total
image.generate(txt_captcha)
image.write(txt_captcha, './images/'+total+'.png')


# # #PIL = pillow 
# from PIL import Image
# image = Image.open('./images/'+total+'.png')
# image.show()
# print()


import cv2
image = cv2.imread('./images/'+total+'.png')

# 이미지 크기
img_height, img_width = image.shape[:2]

# 화면 해상도 
screen_width = 1920  #  1920x1080 해상도
screen_height = 1080

# 창 위치 계산
x = (screen_width - img_width) // 2
y = (screen_height - img_height) // 2
cv2.namedWindow('title', cv2.WINDOW_NORMAL)
cv2.moveWindow('title', x, y)

cv2.imshow("title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()






print()