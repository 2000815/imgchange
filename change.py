# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ExifTags
from PIL.ExifTags import TAGS
import sys


args = sys.argv


print(args)
print("第1引数：" + args[1])
print("第2引数；" + args[2])
print("画像の名前：" + args[3])

#第一引数が左上の文字で第二引数が右上の文字

#画像の読み込みとサイズの確認



image = Image.open('pillow/'+ args[3])
for orientation in ExifTags.TAGS.keys(): 
    if ExifTags.TAGS[orientation]=='Orientation' : 
        break 
exif = dict(image._getexif().items())

if   exif[orientation] == 3 : 
    img=image.rotate(180, expand=True)
elif exif[orientation] == 6 : 
    img=image.rotate(270, expand=True)
elif exif[orientation] == 8 : 
    img=image.rotate(90, expand=True)
else:
    img = image


small_img = img.resize((1080, 1080))




draw = ImageDraw.Draw(small_img)
width ,height= small_img.size
font_size= 90
font_path= '/Library/Fonts/Arial Unicode.ttf'
font = ImageFont.truetype( font_path , font_size) #fontの種類と左上の文字サイズ
draw.text((0, 0), args[2],(252,76,0),font=font) #左上の文字

size = font.getsize(args[1])#ここにも文字を入力する（サイズに関する）

draw.text((height/2,width), args[1], (252,126,254),font=font,anchor='mb') 
draw.text((width,0), '未使用品',(252,76,0),font=font,anchor='ra') 



#同じファイルに保存
small_img.save('pillow/befor.PNG' , quality=95)

imgn = Image.open('pillow/befor.PNG')

for orientation in ExifTags.TAGS.keys(): 
    if ExifTags.TAGS[orientation]=='Orientation' : 
        break 
exif = dict(imgn._getexif().items())

if   exif[orientation] == 3 : 
    new_img=imgn.rotate(0, expand=True)
elif exif[orientation] == 6 : 
    new_img=imgn.rotate(90, expand=True)
elif exif[orientation] == 8 : 
    new_img=imgn.rotate(270, expand=True)
else:
    new_img =imgn

new_img.save('change/New_img.PNG' , quality=95)

#第一引数に商品名、第二引数にサイズ
