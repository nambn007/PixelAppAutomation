import tkinter as tk
from selenium import webdriver

def divide_screen(num_popups):
    # Get screen width and height
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    # Calculate popup width and height
    popup_width = screen_width // 2
    popup_height = screen_height // 2

    # Calculate positions for each popup
    positions = []
    for i in range(num_popups):
        x_position = (i % 2) * popup_width
        y_position = (i // 2) * popup_height
        positions.append((x_position, y_position))

    return positions