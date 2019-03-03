from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import os
date_string = time.strftime("%d-%m-%y")
img = Image.open("image.jpg")
font = ImageFont.truetype("Roboto-Black.ttf", 40)
font1 = ImageFont.truetype("Roboto-Black.ttf", 25)
draw=ImageDraw.Draw(img)
draw.text(xy=(400,400),text="Candidate Name",fill=(255,0,0),font=font)#insert name here.
draw.text(xy=(190,640),text=date_string,fill=(255,69,0),font=font1)
img.show()
i = 0
originalString = 'C:/Users/Sathwik Amburi/Desktop/Projects/Certificate_Generator/Sample/sample_out'
plusjpg = originalString + ".jpg"
exists = os.path.isfile(plusjpg)
if not exists:
    print("Printing")
    newString = originalString
else:
    print('File Name Already Exists')
    while exists:
        print('File Name Already Exists')
        newString = originalString + str(i)
        plusjpg = newString+".jpg"
        exists = os.path.isfile(plusjpg)
        i = i+1

    
savename = plusjpg
img.save(savename)

