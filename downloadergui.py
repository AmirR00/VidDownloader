import tkinter as tk
from pytube import YouTube

class downloader():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.config(bg="#aef2b2")
        self.window.title("YoutubeVideoDownloader")
        self.e = tk.Entry(self.window, font=("Times New Roman", 20), width=30, highlightbackground="#b9faaf")
        self.e.place(x=100, y=90)
        self.b1 = tk.Button(self.window, text="Enter", font=("Calibri", 20), width=15, 
                            foreground="#538c57", highlightthickness=2,
                              highlightbackground='#fff7ab', command=self.vidDownloader)
        self.b1.place(x=140, y=145)
        self.window.mainloop()

    def vidDownloader(self):
        self.geturl = self.e.get()
        for i in self.window.winfo_children():
            i.destroy()
        self.l1 = tk.Label(self.window, text="Select Resolution", width=20, fg="#b5553a", 
                           bg="#aef2b2", font=("Times New Roman", 30))
        self.l1.place(x=100, y=60)
        self.b2 = tk.Button(self.window, text="Lowest \nresolution", font=("Calibri", 20), width=15, 
                            foreground="#538c57", highlightthickness=2,
                              highlightbackground='#fff7ab', command=lambda:self.resquality(low=True))
        self.b2.place(x=140, y=150)
        self.b3 = tk.Button(self.window, text="Highest \nresolution", font=("Calibri", 20), width=15, 
                            foreground="#538c57", highlightthickness=2,
                              highlightbackground='#fff7ab', command=lambda:self.resquality(low=False))
        self.b3.place(x=140, y=250)
    
    def resquality(self, low):
        yt = YouTube(self.geturl)
        if low == True:
            data = yt.streams.get_lowest_resolution()
        elif low == False:
            data = yt.streams.get_highest_resolution()
        # for i in yt.streams:
        #     istring = str(i)
        #     istring = istring.split(" ")
        #     a = istring[3].split("=")[1][1:-1]
        #     print(a)


        data.download(output_path="Videos")
        for i in self.window.winfo_children():
            i.destroy()
        self.l2 = tk.Label(self.window, text="Done!", font=("Calibri", 40), bg="#aef2b2")
        self.l2.place(x=185, y=200)







obj = downloader()




