import os
import pytesseract
from PIL import Image

# 設定要處理的資料夾路徑
folder_path = "./images"

# 設定要儲存OCR結果的資料夾路徑
ocr_folder_path = "./OCR"

# 設定Tesseract OCR的語言為繁體中文
lang = 'chi_tra'

# 設定Tesseract OCR字體路徑   #要手動設定
tessdata_dir_config = "C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 如果目標資料夾不存在，則建立資料夾
if not os.path.exists(ocr_folder_path):
    os.makedirs(ocr_folder_path)

# 讀取資料夾內所有的檔案清單
file_list = os.listdir(folder_path)

# 逐一處理資料夾內的圖片檔案
for filename in file_list:
    # 取得檔案完整路徑
    filepath = os.path.join(folder_path, filename)

    # 如果檔案是圖片，則進行OCR識別
    if filepath.endswith('.jpg') or filepath.endswith('.png'):
        # 讀取圖像檔案
        img = Image.open(filepath)

        # 將圖像轉換為文字
        text = pytesseract.image_to_string(img, lang=lang, config=tessdata_dir_config)

        # 儲存OCR結果到指定目錄中
        ocr_filename = filename.split('.')[0] + '_OCR.txt'
        ocr_filepath = os.path.join(ocr_folder_path, ocr_filename)
        with open(ocr_filepath, 'w', encoding='utf-8') as f:
            f.write(text)