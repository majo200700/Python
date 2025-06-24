import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número")
        self.root.geometry("400x300")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Adivina un número entre 1 y 100", font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Adivinar", font=("Arial", 14), command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.target_number:
                self.result_label.config(text="Demasiado bajo. ¡Intenta de nuevo!")
            elif guess > self.target_number:
                self.result_label.config(text="Demasiado alto. ¡Intenta de nuevo!")
            else:
                messagebox.showinfo("¡Felicidades!", f"¡Adivinaste el número en {self.attempts} intentos!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()