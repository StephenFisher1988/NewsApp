# Import module
import tkinter as tk
from tkinter import *
import praw
import webbrowser

#Reddit Web Scraper API details
reddit = praw.Reddit(client_id='BD6x1qSj4axPADHutUnUGg', client_secret='5E6KTXjcy3i7CHwtFUTFwK4GuWoAvQ', user_agent='WebScraping')

#Get the top 3 stories from r/news for today and overwrite the rtext file
def tasknews():
    try:
        #Open the reddit text file
        rfile = open(r"rtext.txt", "w")
        news_top_posts = reddit.subreddit('news').top("day", limit=10)
        for post in news_top_posts:
            rfile.write(post.title + "\n")
        rfile.close()
    except:
        print("There was an issue loading reddit data")


# Create object
root = tk.Tk()
root.title('Useful Things')
w = 350 # width for the Tk root
h = 550 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x+500, y-100))

#News Field
label = Label(text = "r/news", font = "Castellar")
label.pack()

#Pull Reddit data and pass it into the widget
tasknews()
rfile = open(r"rtext.txt", "r")
for line in rfile:
    T = tk.Text(root, height=3, width=50, wrap=WORD)
    T.pack()
    T.insert(tk.END, line + "\n")

# Execute tkinter
root.mainloop()