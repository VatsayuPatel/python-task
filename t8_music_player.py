# Create a simple music player that can play MP3 files and allow the user to create and manage playlists. using python

import os
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter import filedialog

from pygame import mixer
from mutagen.mp3 import MP3  # for song Length
import time

mixer.init()


class musicPlayer:
    def __init__(self, Tk):
        self.root = Tk
        self.root.title('Music Payer')

        # Adding Width and Height
        self.root.geometry('600x600')

        # Adding Background color
        self.root.configure(background='white')

        self.playlist = []
        self.current_index = 0

        # Open File
        def openfile():
            global filename
            filename = filedialog.askopenfilename()

        # Manu
        self.menubar = Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label="Open", command=openfile)
        self.submenu.add_command(label="Exit", command=self.root.destroy)

        def About():
            tkinter.messagebox.showinfo("About US", 'Music Player created by Anjali')

        self.submenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.submenu)
        self.submenu.add_command(label="About", command=About)

        # Adding Lable
        self.filelable = Label(text='Lets Play Music', bg='white', fg='black', font=25)
        self.filelable.place(x=50, y=20)

        def songinfo():
            self.filelable['text'] = 'Current Music :- ' + os.path.basename(filename)

        # Adding main Img
        self.photo = ImageTk.PhotoImage(file='t8_music-player/images/music-photo.jpeg')
        Label(self.root, image=self.photo, bg='white').place(x=50, y=50)

        # Lable
        self.label1 = Label(self.root, text='Lets Play it', font=25, bg='black', fg='white')
        self.label1.pack(side=BOTTOM, fill=X)

        # for song Length
        def length_bar():
            # starting from zero
            current_time = mixer.music.get_pos() / 1000

            # convert current_time in min and sec
            convert_current_time = time.strftime('%M:%S', time.gmtime(current_time))

            # select mp3 sonng...
            song_mut = MP3(filename)

            # get length of song...
            song_mut_length = song_mut.info.length

            # convert into min and sec.
            convert_song_mut_length = time.strftime('%M:%S', time.gmtime(song_mut_length))

            # blit on screen
            self.lengthbar.config(text=f'Total Length: {convert_current_time} Of {convert_song_mut_length}')
            self.lengthbar.after(1000, length_bar)

        # lable for song length
        self.lengthbar = Label(self.root, text="Totale Length : 00:00", bg='white', fg='black', font=20)
        self.lengthbar.place(x=50, y=250)

        # Creating Buttons...
        # play_button function
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    length_bar()
                    self.label1['text'] = 'Music is Playing...'
                    songinfo()
                except:
                    tkinter.messagebox.showerror("Erroe", 'File could Not Found, Please Try agin...')
            else:
                mixer.music.unpause()
                self.label1['text'] = 'Music Unpaused..'

        # play_button--
        self.photo_LB = ImageTk.PhotoImage(file='t8_music-player/images/1_start_button.jpg')
        Button(self.root, image=self.photo_LB, bd=0, bg='white', command=playmusic).place(x=50, y=300)

        # Function for pausemusic
        def pausemusic():
            global paused
            paused = TRUE
            mixer.music.pause()
            self.label1['text'] = 'Music Paused'

        # pause_button--
        self.photo_PB = ImageTk.PhotoImage(file='t8_music-player/images/2_pause_button.jpg')
        Button(self.root, image=self.photo_PB, bd=0, bg='white', command=pausemusic).place(x=150, y=300)

        # function for stopmusic
        def stopmusic():
            mixer.music.stop()
            self.label1['text'] = 'Music is Stopped'

        # stop_button--
        self.photo_SB = ImageTk.PhotoImage(file='t8_music-player/images/3_stop_button.jpg')
        Button(self.root, image=self.photo_SB, bd=0, bg='white', command=stopmusic).place(x=250, y=300)

        # mute
        def mute():
            self.scale.set(0)
            self.mute = ImageTk.PhotoImage(file='t8_music-player/images/mute_bytton.png')
            Button(self.root, image=self.mute, command=unmute, bd=0, bg='white').place(x=85, y=420)
            self.label1['text'] = "Music Mute"

        # Function for UnMute
        def unmute():
            self.scale.set(25)
            self.photo_VB = ImageTk.PhotoImage(file='t8_music-player/images/volume-Button.png')
            Button(self.root, image=self.photo_VB, bd=0, bg='white', command=mute).place(x=85, y=420)
            self.label1['text'] = "Music UnMute"

        # Volume button image
        self.photo_VB = ImageTk.PhotoImage(file='t8_music-player/images/volume-Button.png')
        Button(self.root, image=self.photo_VB, bd=0, bg='white', command=mute).place(x=85, y=420)

        # function for volume button
        def volume(vol):
            volume = int(vol) / 100
            mixer.music.set_volume(volume)

        # Volume Bar
        self.scale = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, length=200, bg='white', command=volume)
        self.scale.set(25)
        self.scale.place(x=140, y=400)

        # Playlist section
        self.filelabel_playlist = Label(text='My Playlist', bg='white', fg='black', font=25)
        self.filelabel_playlist.place(x=410, y=15)

        self.listbox = Listbox(self.root, bg='white', fg='black', selectbackground='green', selectmode=SINGLE)
        self.listbox.place(x=410, y=50, height=180, width=150)
        self.listbox.bind("<Double-Button-1>", self.play_selected_song)

        def add_to_playlist():
            file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
            if file_path:
                self.playlist.append(file_path)
                self.listbox.insert(END, os.path.basename(file_path))

        self.submenu_playlist = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Playlist", menu=self.submenu_playlist)
        self.submenu_playlist.add_command(label='Add to Playlist', command=add_to_playlist)
        self.submenu_playlist.add_command(label='Play next', command=self.play_next)

    def play_selected_song(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            selected_song = self.playlist[self.current_index]
            mixer.music.load(selected_song)
            mixer.music.play()
            self.filelable['text'] = 'Current Music: ' + os.path.basename(selected_song)
            self.label1['text'] = 'Music is Playing...'
            self.length_bar()

    def play_next(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            next_song = self.playlist[self.current_index]
            mixer.music.load(next_song)
            mixer.music.play()
            self.filelable['text'] = 'Current Music: ' + os.path.basename(next_song)
            self.label1['text'] = 'Music is Playing...'
            self.length_bar()

    def length_bar(self):
        current_time = mixer.music.get_pos() / 1000
        convert_current_time = time.strftime('%M:%S', time.gmtime(current_time))
        song_mut = MP3(self.playlist[self.current_index])
        song_mut_length = song_mut.info.length
        convert_song_mut_length = time.strftime('%M:%S', time.gmtime(song_mut_length))
        self.lengthbar.config(text=f'Total Length: {convert_current_time} Of {convert_song_mut_length}')
        self.lengthbar.after(1000, self.length_bar)


root = Tk()
obj = musicPlayer(root)
root.mainloop()
