import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Menu

class jogostoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Games Store")
        self.root.geometry("800x600")
        self.root.configure(bg="#f7f7f7")

        # Lista de desejos
        self.lista = []

        # As Generos de cada jogo
        self.jogos_data = [
            {"name": "Grand Theft Auto V", "Genero": "ação"},
            {"name": "Ready or Not", "Genero": "ação"},
            {"name": "Grand Theft Auto Online", "Genero": "ação"},
            {"name": "Manor Lords", "Genero": "Simulação"},
            {"name": "EA desporto FC 25", "Genero": "desporto"},
            {"name": "Bus Simulator 21", "Genero": "Simulação"},
            {"name": "Minecraft", "Genero": "aventura"},
            {"name": "Rainbow Six Siege", "Genero": "ação"}
        ]

        # Menu Bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # menu principal
        self.jogos_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Jogos", menu=self.jogos_menu)
        self.jogos_menu.add_command(label="ação", command=lambda: self.filter_jogos("ação"))
        self.jogos_menu.add_command(label="aventura", command=lambda: self.filter_jogos("aventura"))
        self.jogos_menu.add_command(label="Simulação", command=lambda: self.filter_jogos("Simulação"))
        self.jogos_menu.add_command(label="desporto", command=lambda: self.filter_jogos("desporto"))
        self.jogos_menu.add_command(label="todos", command=lambda: self.filter_jogos("todos"))

        # Menu da lista de desejos
        self.menu_bar.add_command(label="Lista de desejos", command=self.open_lista)

        # FraME
        self.jogo_display_frame = Frame(self.root, bg="#f7f7f7")
        self.jogo_display_frame.pack(fill=tk.BOTH, expand=True)

        self.display_jogos(self.jogos_data)

    def display_jogos(self, jogos):
        # limpar os jogos
        for widget in self.jogo_display_frame.winfo_children():
            widget.destroy()

        # Display dos jogos
        if not jogos:
            Label(self.jogo_display_frame, text="No jogos available", font=("Helvetica", 14), bg="#f7f7f7").pack(pady=20)
            return

        row_frame = None
        for index, jogo in enumerate(jogos):
            if index % 5 == 0:
                row_frame = Frame(self.jogo_display_frame, bg="#f7f7f7")
                row_frame.pack(fill=tk.X, pady=5)
            self.create_card(row_frame, jogo)

    def create_card(self, parent, jogo):
        card_frame = Frame(parent, bg="white", relief="sunken", borderwidth=1, padx=10, pady=10)
        card_frame.pack(side=tk.LEFT, padx=10)

        Label(card_frame, text=jogo["name"], font=("Helvetica", 12, "bold"), bg="white").pack(pady=5)

        Label(card_frame, text=f"Genero: {jogo['Genero']}", font=("Helvetica", 10), bg="white").pack(pady=5)

        buy_button = Button(card_frame, text="Adiciona há tua lista", command=lambda g=jogo["name"]: self.add_to_lista(g))
        buy_button.pack(pady=5)

    def add_to_lista(self, jogo):
        if jogo not in self.lista:
            self.lista.append(jogo)
            messagebox.showinfo("Lista de desejos", f"{jogo} já foi adicionado há tua lista de desejos!")
        else:
            messagebox.showinfo("Lista de desejos", f"{jogo} já esta na tua lista de desejos!")

    def open_lista(self):
        lista_window = tk.Toplevel(self.root)
        lista_window.title("Desejos")
        lista_window.geometry("400x400")

        Label(lista_window, text="Lista de desejos", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=10)

        for jogo in self.lista:
            self.create_lista_card(lista_window, jogo)

    def create_lista_card(self, parent, jogo_name):
        card_frame = Frame(parent, bg="white", relief="sunken", borderwidth=1, padx=10, pady=10)
        card_frame.pack(pady=5, fill=tk.X)

        Label(card_frame, text=jogo_name, font=("Helvetica", 12, "bold"), bg="white").pack(side=tk.LEFT, padx=5)

        remove_button = Button(card_frame, text="Remove", command=lambda g=jogo_name: self.remove_from_lista(g, card_frame))
        remove_button.pack(side=tk.RIGHT, padx=5)

    def remove_from_lista(self, jogo, frame):
        if jogo in self.lista:
            self.lista.remove(jogo)
            frame.destroy()
            messagebox.showinfo("lista", f"{jogo} foi removido da tua lista")

    def filter_jogos(self, Genero):
        if Genero == "todos":
            Filtro_jogos = self.jogos_data
        else:
            Filtro_jogos = [jogo for jogo in self.jogos_data if jogo["Genero"] == Genero]

        self.display_jogos(Filtro_jogos)

if __name__ == "__main__":
    root = tk.Tk()
    app = jogostoreApp(root)
    root.mainloop()
