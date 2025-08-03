import tkinter as tk
from PIL import Image, ImageTk

class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value - 1]
        self.suit = '♥♦♣♠'[suit]
        suit_char = self.suit
        if self.suit == '♥':
            suit_char = 'H'
        elif self.suit == '♦':
            suit_char = 'D'
        elif self.suit == '♣':
            suit_char = 'C'
        elif self.suit == '♠':
            suit_char = 'S'
        self.image_path = f"cards/{self.value}{suit_char}.png"

    def get_image(self):
        image = Image.open(self.image_path)
        image = image.resize((100, 150), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def show(self, master):
        card_image = self.get_image()
        label = tk.Label(master, image=card_image)
        label.image = card_image
        label.pack(side=tk.LEFT, padx=5, pady=5)

    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost