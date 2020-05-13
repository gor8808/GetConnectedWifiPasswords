from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
import os
import qrcode
fileName = "Gor"
os.system("title ID CARD Generator by Codehub")
img = qrcode.make("Gor Grigoryan")   
img.save(fileName+'.bmp')

