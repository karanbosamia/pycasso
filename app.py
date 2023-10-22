import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import glob

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.image_paths = []
        self.current_index = -1

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.load_button = tk.Button(root, text="Load Folder", command=self.load_folder)
        self.load_button.pack()

        self.previous_button = tk.Button(root, text="Previous", command=self.show_previous)
        self.previous_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.show_next)
        self.next_button.pack()

        root.bind("<Left>", lambda event: self.show_previous())
        root.bind("<Right>", lambda event: self.show_next())

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_paths = sorted(glob.glob(os.path.join(folder_path, '*.png')) + glob.glob(os.path.join(folder_path, '*.jpg')))
            if self.image_paths:
                self.current_index = 0
                self.show_image()

    def show_image(self):
        if self.current_index >= 0 and self.current_index < len(self.image_paths):
            image = Image.open(self.image_paths[self.current_index])
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()

    def show_next(self):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
