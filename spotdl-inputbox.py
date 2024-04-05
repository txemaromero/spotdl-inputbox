import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import subprocess
import os

class SpotifyDownloaderGUI:
    def __init__(self, root):
        self.root = root
        root.title('Spotify Playlist Downloader')

        # Create download button
        self.download_button = tk.Button(root, text='Download Spotify Playlist', command=self.download_playlist)
        self.download_button.pack(pady=20)

    def download_playlist(self):
        # Ask for Spotify playlist URL
        url = simpledialog.askstring("Input", "Enter the Spotify Playlist URL:", parent=self.root)

        if url:
            # Ask for directory to save the playlist
            directory = filedialog.askdirectory()

            if directory:
                # Change working directory to the selected directory
                os.chdir(directory)

                # Run spotDL command
                subprocess.run(['spotdl', url])

if __name__ == '__main__':
    root = tk.Tk()
    gui = SpotifyDownloaderGUI(root)
    root.mainloop()
