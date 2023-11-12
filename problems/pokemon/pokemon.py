"""
Exercise: Pokemon battle
Goal: given two pokemon, create two classes, Fight and Pokemon
- Pokemon: will create a pokemon
- Fight: will start a fight between two pokemons
- Interface: optional but you can do a simple one :)
"""

import time
from tkinter import Tk, PhotoImage, Canvas


# Interface OPTIONAL

class Interface:

    def __init__(self, tk, pokemon1, pokemon2):
        self.tk = tk
        window_width = 500
        window_height = 500
        screen_width = self.tk.winfo_screenwidth()
        screen_height = self.tk.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.tk.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.set_pokemon1()
        self.set_pokemon2()
        self.set_health_label(self)
        self.set_fight_button()

    def set_pokemon1(self):
        self.pokemon1_img = PhotoImage(file=self.pokemon1.pokemon_img)
        self.pokemon1_img = self.pokemon1_img.subsample(3, 3)
        self.pokemon1_img_label = self.canvas.create_image(100, 250, image=self.pokemon1_img)
        self.pokemon1_name_label = self.canvas.create_text(100, 300, text=self.pokemon1.name)

    def set_pokemon2(self):
        self.pokemon2_img = PhotoImage(file=self.pokemon2.pokemon_img)
        self.pokemon2_img = self.pokemon2_img.subsample(3, 3)
        self.pokemon2_img_label = self.canvas.create_image(400, 250, image=self.pokemon2_img)
        self.pokemon2_name_label = self.canvas.create_text(400, 300, text=self.pokemon2.name)

    def set_health_label(self, fight):
        self.pokemon1_health_label = self.canvas.create_text(100, 200, text=self.pokemon1.get_health())
        self.pokemon2_health_label = self.canvas.create_text(400, 200, text=self.pokemon2.get_health())

    def set_new_health(self, fight):
        self.canvas.itemconfig(self.pokemon1_health_label, text=self.pokemon1.get_health())
        self.canvas.itemconfig(self.pokemon2_health_label, text=self.pokemon2.get_health())
        self.canvas.update()

    def set_fight_button(self):
        self.fight_button = self.canvas.create_text(250, 400, text=" Click to Fight", font=("Arial", 20))
        self.canvas.tag_bind(self.fight_button, "<Button-1>", lambda x: self.fight())

    def fight(self):
        self.canvas.delete(self.fight_button)
        # set label "fight started" in middle of screen
        self.fight_info = self.canvas.create_text(250, 20, text="Fight started!")
        time.sleep(2)

        fight = Fight(self.pokemon1, self.pokemon2, self)
        fight.fight()

    def fight_description(self, msg):
        self.canvas.itemconfig(self.fight_info, text=msg)
        time.sleep(1)


# ======================================================================

class Fight:
    turn = 0

    def __init__(self, pokemon1, pokemon2, interface):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.base_attack = 2
        self.interface = interface

    def fight(self):

        print("Pikachu entering the arena: Pika Pika Pika")
        print("Mewtwo entering the arena: Mew Mew Mew")

        while self.pokemon1.get_health() > 0 and self.pokemon2.get_health() > 0:
            # pair turn pokemon1 attack
            if self.turn % 2 == 0:
                msg = self.pokemon1.name + " attack " + self.pokemon2.name
                self.pokemon2.set_health(self.pokemon2.get_health() - self.pokemon1.level * self.base_attack)
                print(msg)

            # impair turn pokemon2 attack
            else:
                msg = self.pokemon2.name + " attack " + self.pokemon1.name
                print(msg)
                self.pokemon1.set_health(self.pokemon1.get_health() - self.pokemon2.level * self.base_attack)
            self.interface.fight_description(msg)
            self.turn += 1
            interface.set_new_health(self)
            time.sleep(1)
        if self.pokemon1.get_health() > self.pokemon2.get_health():
            winner_msg = self.pokemon1.name + " won!"
        else:
            winner_msg = self.pokemon2.name + " won!"

        print(winner_msg)
        self.interface.fight_description(winner_msg)


class Pokemon:

    def __init__(self, name, level, type, scream, max_health, current_health, pokemon_img):
        self.name = name
        self.level = level
        self.type = type
        self.scream = scream
        self.max_health = max_health
        self.current_health = current_health
        self.pokemon_img = pokemon_img

    def set_health(self, health):
        print(self.name + " health: " + str(health))
        self.current_health = health

    def get_health(self):
        print(self.name + " health: " + str(self.current_health))
        return self.current_health


if __name__ == '__main__':
    tk = Tk()
    tk.title("Pokemon Fight")
    pokemon1 = Pokemon("Pikachu", 10, "Electric", "Pika Pika", 100, 100, "pokemon_image/pikachu.png")
    pokemon2 = Pokemon("Mewtwo", 10, "Psychic", "Mew Mew", 100, 100, "pokemon_image/mew.png")
    interface = Interface(tk, pokemon1, pokemon2)
    tk.mainloop()
