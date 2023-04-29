from PIL import Image
import pytesseract
import time
from os import listdir
from os.path import isfile, isdir, join
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#前置:安裝pytesseract,import上面內容
#點擊產生資料夾內所有圖片 到OCR資料夾內

def OCR(pic):
    img = Image.open(pic)
    OCR= pytesseract.image_to_string(img, lang="chi_tra")  #圖片位置,繁體中文
    
    print(OCR)
    path = './OCR'
    if not os.path.isdir(path):
        os.mkdir(path)
    path = 'OCR/'+ pic + '.txt'                            #輸出
    f = open(path, 'w')
    f.write(OCR)
    f.close()

file=[]
# 取得目前工作目錄下的所有檔案清單
file_list = os.listdir(os.getcwd())

for file_name in file_list:
    if(file_name!="OCR.py"):
        file.append(file_name)


for file_name in file:
    OCR(file_name)


print("3秒後關閉")
time.sleep(3)
