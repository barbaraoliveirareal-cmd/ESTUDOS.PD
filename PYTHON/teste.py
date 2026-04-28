import tkinter as tk
import random

def sim():
    label.config(text="Eba! Te amo! ❤️")
    btn_nao.destroy()

def move_nao(event):
    btn_nao.place(x=random.randint(0, 200), y=random.randint(0, 200))

root = tk.Tk()
root.title("Pergunta importante")
root.geometry("300x250")

label = tk.Label(root, text="Quer sair comigo?", font=("Arial", 14))
label.pack(pady=20)

btn_sim = tk.Button(root, text="Sim", command=sim)
btn_sim.pack()

btn_nao = tk.Button(root, text="Não")
btn_nao.pack(pady=10)
btn_nao.bind("<Enter>", move_nao)

root.mainloop()
