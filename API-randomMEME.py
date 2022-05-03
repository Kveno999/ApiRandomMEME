import requests
import shutil
import random
import os
from PIL import Image, ImageFont, ImageDraw

def getResponse():
    global response
    response = requests.get("https://api.imgflip.com/get_memes")

getResponse()


def image_download():

    image_url = response.json()['data']['memes'][random.randrange(1, 100)]['url']
    global filename
    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream=True)

    question = str(input("Do u want to download this random meme? type yes/no : "))
    if question.lower() == "yes":
        if r.status_code == 200:
            r.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                shutil.copy(fr'C:\Users\kveni\PycharmProjects\ProjectForEPAM\venv\{filename}', newpath)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')
    elif question.lower() == "no":
        pass
    else:
        print("Please type yes or no correctly!")
        image_download()



def create_dir(folderName):
    global newpath
    newpath = fr'C:\Users\kveni\Desktop\PYhton dir tests/{folderName}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print("Created Directory : ", newpath)
    else:
        print("Directory already existed : ", newpath)
    return dir


def editImage():
    image = Image.open(filename)
    title_font = ImageFont.truetype(fr'C:\Users\kveni\Desktop\PYhton dir tests\test2\Inter-Bold.ttf', 25)
    title_text = str(input("Type your name to appiar it on meme template: "))
    image_editable = ImageDraw.Draw(image)
    image_editable.text((5, 5), title_text, (237, 230, 211), font=title_font)
    image.save(f"{filename}")
    shutil.copy(fr'C:\Users\kveni\PycharmProjects\ProjectForEPAM\venv\{filename}', newpath)
    print(f'Edited Image sucessfully Saved as {filename}')


print('Welcome to our space of meme templates!')
new_folder_name = str(input("Enter a folder name, where u want to save meme templates: "))

create_dir(new_folder_name)
image_download()
editImage()