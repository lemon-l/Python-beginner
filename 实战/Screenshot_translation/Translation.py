import tkinter.messagebox
from tkinter import *
from PIL import Image
from PIL import ImageGrab
import pytesseract
from googletrans import Translator
 
def get_image():
    '''
    剪切板获取图片，并保存在本地
    '''
    image_path = None
    img = ImageGrab.grabclipboard()
    if img and isinstance(img,Image.Image):
        image_path = './temp.png'
        img.save(image_path)
    return image_path

def img_orc(image_path):
    '''
    OCR识别图片中的英文
    '''
    return pytesseract.image_to_string(Image.open(image_path),lang='eng')

def trans_eng(content_english):
    '''
    谷歌翻译
    '''
    translator = Translator(service_urls=['translate.google.cn'])
    return translator.translate(content_english,src='en',dest='zh-cn').text

image_path = get_image()

if image_path:
    content_english = img_orc(image_path).replace("\r"," ").replace("\n"," ")
    if content_english:
        contet_Chinese = trans_eng(content_english)
        print(contet_Chinese)
        # 以对话框的形式显示翻译后的结果
        root = Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('翻译结果：',contet_Chinese)