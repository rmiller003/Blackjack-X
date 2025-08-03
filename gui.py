import tkinter as tk
from tkinter import messagebox
from blackjack import Blackjack
import pygame

class BlackjackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        self.master.geometry("1024x768")

        pygame.mixer.init()
        pygame.mixer.music.load("music/jazz.ogg")
        pygame.mixer.music.play(loops=-1)

        self.canvas = tk.Canvas(master, width=1024, height=768)
        self.canvas.pack()
        self.background_image = tk.PhotoImage(file="background/casino.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        self.title_label = tk.Label(self.canvas, text="Welcome to Miller's Casino", font=("Edwardian Script ITC", 46), fg="white", bg="saddle brown")
        self.canvas.create_window(512, 50, window=self.title_label)

        self.blackjack_game = Blackjack()

        self.dealer_frame = tk.Frame(self.canvas, pady=10, bg="darkgreen")
        self.canvas.create_window(512, 250, window=self.dealer_frame)
        self.dealer_label = tk.Label(self.dealer_frame, text="Dealer's Hand:", fg="white", bg="darkgreen")
        self.dealer_label.pack()
        self.dealer_cards_frame = tk.Frame(self.dealer_frame, bg="darkgreen")
        self.dealer_cards_frame.pack()

        self.player_frame = tk.Frame(self.canvas, pady=10, bg="darkgreen")
        self.canvas.create_window(512, 450, window=self.player_frame)
        self.player_label = tk.Label(self.player_frame, text="Player's Hand:", fg="white", bg="darkgreen")
        self.player_label.pack()
        self.player_cards_frame = tk.Frame(self.player_frame, bg="darkgreen")
        self.player_cards_frame.pack()

        self.buttons_frame = tk.Frame(self.canvas, bg="darkgreen")
        self.canvas.create_window(512, 650, window=self.buttons_frame)

        self.hit_button = tk.Button(self.buttons_frame, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT)

        self.stand_button = tk.Button(self.buttons_frame, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT)

        self.play_again_button = tk.Button(self.buttons_frame, text="Play Again", command=self.play_again)
        self.play_again_button.pack(side=tk.LEFT)
        self.play_again_button.config(state=tk.DISABLED)

        self.start_game()

    def start_game(self):
        self.blackjack_game.player.deal()
        self.blackjack_game.dealer.deal()
        self.update_ui()

    def update_ui(self):
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()

        for widget in self.player_cards_frame.winfo_children():
            widget.destroy()

        for card in self.blackjack_game.dealer.cards:
            card.show(self.dealer_cards_frame)

        for card in self.blackjack_game.player.cards:
            card.show(self.player_cards_frame)

        self.dealer_label.config(text=f"Dealer's Hand: {self.blackjack_game.dealer.score}")
        self.player_label.config(text=f"Player's Hand: {self.blackjack_game.player.score}")

    def hit(self):
        if self.blackjack_game.player.hit() == 1:
            self.update_ui()
            messagebox.showinfo("Bust", "You busted!")
            self.end_game()
        else:
            self.update_ui()

    def stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

        self.update_ui()

        if self.blackjack_game.dealer.check_score() == 21:
            self.determine_winner()
            return

        while self.blackjack_game.dealer.check_score() < 17:
            if self.blackjack_game.dealer.hit() == 1:
                self.update_ui()
                messagebox.showinfo("Winner", "Dealer busted! You win!")
                self.end_game()
                return
            self.update_ui()

        self.determine_winner()

    def determine_winner(self):
        player_score = self.blackjack_game.player.check_score()
        dealer_score = self.blackjack_game.dealer.check_score()

        if player_score > dealer_score:
            messagebox.showinfo("Winner", "You win!")
        elif player_score < dealer_score:
            messagebox.showinfo("Loser", "Dealer wins!")
        else:
            messagebox.showinfo("Push", "It's a tie!")

        self.end_game()

    def end_game(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.blackjack_game = Blackjack()
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
