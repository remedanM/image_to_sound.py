from PIL import Image
import pytesseract
import pyttsx3
# from gtts import gTTS

# store the image into a variable
img = Image.open('pro2.jpg')
# change the image into text and store it in to a variable
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_string(img)
# create a file and write in it the text of the image
with open('abc.txt', 'w') as f:
    f.write(result)
    print(result)
# initiat pyttsx3
engine = pyttsx3.init()
# start the audio
engine.say(result)
engine.runAndWait()


# other way of audio
# gTTS(result, lang='en').save('pro.mp3')


