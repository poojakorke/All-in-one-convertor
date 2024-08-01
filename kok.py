from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import customtkinter
from PIL import Image
from tkinter import filedialog
import pytesseract as tess
import speech_recognition as sr
import os
import pyttsx3

mainwindow= Tk()
mainwindow.title('CONVERTOR ')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='purple')
def ocr():
 tess.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
 app=Toplevel(mainwindow)
 app=customtkinter.CTk()
 app.geometry('650 × 50')
 app.title('Image to text converter:-')
 app.maxsize(600,450)
 frame=customtkinter.CTkFrame(app,corner_radius=20,border_color='#0000ff',border_width=4,)
 frame.pack(padx=20,pady=20,fill='both')
 txt=customtkinter.CTkLabel(frame,text="Extract Text From Image",font=("Ariel",20))
 txt.pack(pady=10)

 progress_txt=customtkinter.CTkLabel(frame,text="0%")
 progress_txt.place(x=390,y=144)

 def openImage():
     progressbar.set(0)
     progress_txt.configure(text='100%')
     filename=filedialog.askopenfilename()
     img1=Image.open(filename)
     get_txt=tess.image_to_string(img1)
     progressbar.start()
     progressbar.set(1)
     txt_box.insert('0.0',get_txt)
     app.title(filename)
     progress_txt.configure(text='100%')
     progressbar.stop()

img=customtkinter.CTkImage(Image.open('img1.jpg'),size=(42,42))
btn=customtkinter.CTkButton(frame,text='Add Image',text_color='#FFFFFF',corner_radius=8,image=img,width=20, height=30,
                            compound='right',font=('Arial',20),border_spacing=10,
                            command=openImage,hover_color='#ff0000')
btn.pack(padx=20,pady=20)
progressbar=customtkinter.CTkProgressBar(frame,progress_color='#ffff00')
progressbar.pack()
progressbar.set(0)
txt_box=customtkinter.CTkTextbox(frame,font=('Arial',18),width=520,height=420,corner_radius=8)
txt_box.pack(pady=20)





def texttospeech():
    texttospeechwindow = Toplevel(mainwindow)
    engine = pyttsx3.init()

    texttospeechwindow.title("text to speech")
    texttospeechwindow.configure(bg="purple")
    texttospeechwindow.geometry("660x300")
    def speak():
    
     engine.say(text.get())
     engine.runAndWait()
     engine.stop()
#Label frame
    pk = LabelFrame(texttospeechwindow,text="Text to speech",font="40",bd=7,bg="pink")
    pk.pack(fill="both",expand="yes",side=LEFT,padx=45,pady=45)
    Label(pk,text="Text",font="45",padx=10).pack(side=LEFT)
#   entry----user enter text
    text= StringVar()
    Entry(pk,width=50,bd=5,textvariable=text).pack(side=LEFT,padx=30)

#button
    Button(pk,text="Speech",font=25,command=speak).pack(side=LEFT,padx=10)




def speechtotext():
     
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter by DataFlair')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='purple')
 
    Label(speechtotextwindow, text='Speech-to-Text Converter ', font=("Comic Sans MS", 15), bg='white').place(x=50)
 
    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=7, y=100)
   
    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=140, y=50)
 

    
def say(text1):
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3")
     os.system("start text.mp3")
 
def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text1






texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='white', command=texttospeech)
texttospeechbutton.place(x=100, y=150)
ocrbutton= Button(mainwindow, text='Image-To-Text Conversion', font=('Times New Roman', 16), bg='white',command=ocr)
ocrbutton.place(x=100,y=250)

speechtotextbutton = Button(mainwindow, text='speech- to -text Conversion', font=('Times New Roman', 16), bg='white', command=speechtotext)
speechtotextbutton.place(x=100,y=350)



mainwindow.mainloop()