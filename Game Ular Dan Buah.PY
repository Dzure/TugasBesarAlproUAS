#TUBES ALPRO
#Adiyatma Sadya Nugraha

#Set UP
from tkinter import*
import turtle
import pygame
from pygame import mixer
import time
import random

splash_win= Tk()


#Define the size of the window or frame
width = splash_win.winfo_screenwidth()
height = splash_win.winfo_screenheight()
splash_win.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

#Remove border of the splash Window

splash_win.overrideredirect(True)

#Define the label of the window
splash_label= Label(splash_win, text= "\n \n \n Hallo Selamat Datang \n Semoga Enjoy Dengan Gamenya", fg = "green", 
font= ('Times New Roman', 40)).pack(pady=70)
def mainWin():
   splash_win.destroy()
   
   

#Splash Window Timer

splash_win.after(5000, mainWin)

mainloop()

delay = 0.1



# Data Skor
skor = 0
skor_tertinggi = 0

# Layar

wn = turtle.Screen()
wn.title("Ular Dan Buah")
wn.bgpic("grass3.gif")
wn.bgcolor("green")
wn.setup(width=735, height=735)
wn.tracer(0) 


#Background Musik
pygame.mixer.init(44100, -16,2,2048)
mixer.music.load('background.wav')
mixer.music.play(-1)



# Kepala Ular
kepala = turtle.Turtle()
kepala.speed(0)
kepala.shape("circle")
kepala.color("orange")
kepala.penup()
kepala.goto(0,0)
kepala.arah = "stop"

# Buah Ular
buah = turtle.Turtle()
wn.addshape("apel2.gif")
buah.speed(0)
buah.shape("apel2.gif")
buah.penup()
buah.goto(0,100)

segments = []

# Papan Skor
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Skor: 0  Skor Tertinggi: 0", align="center", font=("MS Serif", 24, "normal"))

# Fungsi Arah
def keatas():
    if kepala.arah != "down":
        kepala.arah = "up"

def kebawah():
    if kepala.arah != "up":
        kepala.arah = "down"

def kekiri():
    if kepala.arah != "right":
        kepala.arah = "left"

def kekanan():
    if kepala.arah != "left":
        kepala.arah = "right"

def gerakan():
    if kepala.arah == "up":
        y = kepala.ycor()
        kepala.sety(y + 20)

    if kepala.arah == "down":
        y = kepala.ycor()
        kepala.sety(y - 20)

    if kepala.arah == "left":
        x = kepala.xcor()
        kepala.setx(x - 20)

    if kepala.arah == "right":
        x = kepala.xcor()
        kepala.setx(x + 20)

# KeYBINDING & Error Handling
try:
   wn.listen()
   wn.onkeypress(keatas, "w")
   wn.onkeypress(kebawah, "s")
   wn.onkeypress(kekiri, "a")
   wn.onkeypress(kekanan, "d")
except KeyError:
    print("Masukkan Keybindings Yang Sesuai")
except TypeError:
    print("Masukkan Keybindings Yang Sesuai")
except ArithmeticError:
     print("Masukkan Keybindings Yang Sesuai")
except SyntaxError:
     print("Masukkan Keybindings Yang Sesuai")
except NameError:
     print("Masukkan Keybindings Yang Sesuai")


# Loop Game (Pengulangan)
keadaan = "start"
Ganabrak = True
while Ganabrak:
    wn.update()

    # Tabrakan Dengan Perbatasan
    if kepala.xcor()>740 or kepala.xcor()<-740 or kepala.ycor()>365 or kepala.ycor()<-365:
        wn.bgpic("game_over.gif")
        

        turtle.pendown()
 

        

        #Efek Suara Menabrak Dinding
        tabrak_dinding = mixer.Sound('Crash.wav')
        tabrak_dinding.play()
      
        time.sleep(1)
        kepala.goto(0,0)
        kepala.arah = "stop"

        #Menyembunyikan Segmen
        for segment in segments:
            segment.goto(1000, 1000)
    

        segments.clear()

        # Reset skor
        skor = 0

        # Reset delay
        delay = 0.1

        pen.clear()
        pen.write("Skor: {}  Skor Tertinggi: {}".format(skor, skor_tertinggi), align="center", font=("MS Serif", 24, "normal")) 

    
        
        


    # Cek Jarak Antara Ular dan buah
    if kepala.distance(buah) < 20:
        #Efek Suara saat ular memakan
        makan_buah = mixer.Sound('laser.wav')
        makan_buah.play()
        # Memindahkan Buah ke tempat random
        x = random.randint(-740, 740)
        y = random.randint(-365, 365)
        buah.goto(x,y)

        # Menambahkan Segment 
        segment_baru = turtle.Turtle()
        segment_baru.speed(0)
        segment_baru.shape("square")
        segment_baru.color("red","black")
        segment_baru.penup()
        segments.append(segment_baru)

        # Memperpendek Delay
        delay -= 0.001

        # Menambahkan Skor
        skor += 10

        if skor > skor_tertinggi:
            skor_tertinggi = skor
        
        pen.clear()
        pen.write("Skor: {}  Skor Tertinggi: {}".format(skor, skor_tertinggi), align="center", font=("MS Serif", 24, "normal")) 

    # Pindahkan segmen akhir terlebih dahulu dalam urutan terbalik
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Memindahkan Segmen Badan ke Kepala
    if len(segments) > 0:
        x = kepala.xcor()
        y = kepala.ycor()
        segments[0].goto(x,y)

    gerakan()    

    # Cek Jarak Kepala Ular dengan Segmen Badan
    for segment in segments:
        if segment.distance(kepala) < 20:
            time.sleep(1)
            kepala.goto(0,0)
            kepala.arah = "berhenti"
            
        
            # Menyembunyikan Segmen
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Membersihkan Segmen
            segments.clear()

            # Reset Skor
            skor = 0

            # Reset delay
            delay = 0.1
        
            # Update Tampilan Skor
            pen.clear()
            pen.write("Skor: {}  Skor Tertinggi: {}".format(skor, skor_tertinggi), align="center", font=("MS Serif", 24, "normal"))
            
        
    time.sleep(delay)
    
wn.mainloop()

        