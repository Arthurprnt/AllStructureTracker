from tkinter import *
import pygame
import os
from threading import Thread
import subprocess

window_buttons = Tk()
size = (393, 400)
window_buttons.title("All Structures Tracker by DraquoDrass")
window_buttons.iconbitmap("assets/icon.ico")
window_buttons.geometry(str(size[0]) + "x" + str(size[1]))
window_buttons.minsize(size[0], size[1])
window_buttons.maxsize(size[0], size[1])

file = open("settings.txt", mode="r")
the_settings = file.readlines()
file.close()

font = ("Arial, 15")
bg = "#ffffff"
fg = "#000000"
changed_bg = str(the_settings[2].replace("CLICKED_BUTTONS=", "").replace("\n", ""))
width = 17

global structures
structures = []
for filenames in os.walk("assets/BLOCS/"):
    structures.extend(filenames)
structures = structures[2]
global structures_copy
structures_copy = list(structures)

def buttons_function():
    def bastion():
        button_bastion.configure(bg=changed_bg, fg=fg)
        if "bastion.png" in structures_copy:
            structures_copy.pop(structures_copy.index("bastion.png"))

    def burried_treasure():
        button_burried_treasure.configure(bg=changed_bg, fg=fg)
        if "burried_treasure.png" in structures_copy:
            structures_copy.pop(structures_copy.index("burried_treasure.png"))

    def desert_pyramid():
        button_desert_pyramid.configure(bg=changed_bg, fg=fg)
        if "desert_pyramid.png" in structures_copy:
            structures_copy.pop(structures_copy.index("desert_pyramid.png"))

    def end_city():
        button_end_city.configure(bg=changed_bg, fg=fg)
        if "end_city.png" in structures_copy:
            structures_copy.pop(structures_copy.index("end_city.png"))

    def igloo():
        button_igloo.configure(bg=changed_bg, fg=fg)
        if "igloo.png" in structures_copy:
            structures_copy.pop(structures_copy.index("igloo.png"))

    def jungle_temple():
        button_jungle_temple.configure(bg=changed_bg, fg=fg)
        if "jungle_temple.png" in structures_copy:
            structures_copy.pop(structures_copy.index("jungle_temple.png"))

    def mineshaft():
        button_mineshaft.configure(bg=changed_bg, fg=fg)
        if "mineshaft.png" in structures_copy:
            structures_copy.pop(structures_copy.index("mineshaft.png"))

    def nether_fortress():
        button_nether_fortress.configure(bg=changed_bg, fg=fg)
        if "nether_fortress.png" in structures_copy:
            structures_copy.pop(structures_copy.index("nether_fortress.png"))

    def nether_fossil():
        button_nether_fossil.configure(bg=changed_bg, fg=fg)
        if "nether_fossil.png" in structures_copy:
            structures_copy.pop(structures_copy.index("nether_fossil.png"))

    def ocean_monument():
        button_ocean_monument.configure(bg=changed_bg, fg=fg)
        if "ocean_monument.png" in structures_copy:
            structures_copy.pop(structures_copy.index("ocean_monument.png"))

    def ocean_ruins():
        button_ocean_ruins.configure(bg=changed_bg, fg=fg)
        if "ocean_ruins.png" in structures_copy:
            structures_copy.pop(structures_copy.index("ocean_ruins.png"))

    def pillager_outpost():
        button_pillager_outpost.configure(bg=changed_bg, fg=fg)
        if "pillager_outpost.png" in structures_copy:
            structures_copy.pop(structures_copy.index("pillager_outpost.png"))

    def ruined_portal():
        button_ruined_portal.configure(bg=changed_bg, fg=fg)
        if "ruined_portal.png" in structures_copy:
            structures_copy.pop(structures_copy.index("ruined_portal.png"))

    def shipwreck():
        button_shipwreck.configure(bg=changed_bg, fg=fg)
        if "shipwreck.png" in structures_copy:
            structures_copy.pop(structures_copy.index("shipwreck.png"))

    def stronghold():
        button_stronghold.configure(bg=changed_bg, fg=fg)
        if "stronghold.png" in structures_copy:
            structures_copy.pop(structures_copy.index("stronghold.png"))

    def swamp_hut():
        button_swamp_hut.configure(bg=changed_bg, fg=fg)
        if "swamp_hut.png" in structures_copy:
            structures_copy.pop(structures_copy.index("swamp_hut.png"))

    def village():
        button_village.configure(bg=changed_bg, fg=fg)
        if "village.png" in structures_copy:
            structures_copy.pop(structures_copy.index("village.png"))

    def wooden_mansion():
        button_wooden_mansion.configure(bg=changed_bg, fg=fg)
        if "wooden_mansion.png" in structures_copy:
            structures_copy.pop(structures_copy.index("wooden_mansion.png"))

    def clear():
        button_bastion.configure(bg=bg, fg=fg)
        button_burried_treasure.configure(bg=bg, fg=fg)
        button_desert_pyramid.configure(bg=bg, fg=fg)
        button_end_city.configure(bg=bg, fg=fg)
        button_igloo.configure(bg=bg, fg=fg)
        button_jungle_temple.configure(bg=bg, fg=fg)
        button_mineshaft.configure(bg=bg, fg=fg)
        button_nether_fortress.configure(bg=bg, fg=fg)
        button_nether_fossil.configure(bg=bg, fg=fg)
        button_ocean_monument.configure(bg=bg, fg=fg)
        button_ocean_ruins.configure(bg=bg, fg=fg)
        button_pillager_outpost.configure(bg=bg, fg=fg)
        button_ruined_portal.configure(bg=bg, fg=fg)
        button_shipwreck.configure(bg=bg, fg=fg)
        button_stronghold.configure(bg=bg, fg=fg)
        button_swamp_hut.configure(bg=bg, fg=fg)
        button_village.configure(bg=bg, fg=fg)
        button_wooden_mansion.configure(bg=bg, fg=fg)
        for i in range(0, len(structures_copy) - 1):
            structures_copy.pop()
        for i in structures:
            structures_copy.append(i)

    def settings():
        subprocess.Popen('explorer "settings.txt"')

    button_bastion = Button(text="Bastion Remnant", font=font, bg=bg, fg=fg, width=width, command=bastion)
    button_burried_treasure = Button(text="Burried Treasure", font=font, bg=bg, fg=fg, width=width, command=burried_treasure)
    button_desert_pyramid = Button(text="Desert Pyramid", font=font, bg=bg, fg=fg, width=width, command=desert_pyramid)
    button_end_city = Button(text="End City", font=font, bg=bg, fg=fg, width=width, command=end_city)
    button_igloo = Button(text="Igloo", font=font, bg=bg, fg=fg, width=width, command=igloo)
    button_jungle_temple = Button(text="Jungle Temple", font=font, bg=bg, fg=fg, width=width, command=jungle_temple)
    button_mineshaft = Button(text="Mineshaft", font=font, bg=bg, fg=fg, width=width, command=mineshaft)
    button_nether_fortress = Button(text="Nether Fortress", font=font, bg=bg, fg=fg, width=width, command=nether_fortress)
    button_nether_fossil = Button(text="Nether Fossil", font=font, bg=bg, fg=fg, width=width, command=nether_fossil)
    button_ocean_monument = Button(text="Ocean Monument", font=font, bg=bg, fg=fg, width=width, command=ocean_monument)
    button_ocean_ruins = Button(text="Ocean Ruins", font=font, bg=bg, fg=fg, width=width, command=ocean_ruins)
    button_pillager_outpost = Button(text="Pillager Outpost", font=font, bg=bg, fg=fg, width=width, command=pillager_outpost)
    button_ruined_portal = Button(text="Ruined Portal", font=font, bg=bg, fg=fg, width=width, command=ruined_portal)
    button_shipwreck = Button(text="Shipwreck", font=font, bg=bg, fg=fg, width=width, command=shipwreck)
    button_stronghold = Button(text="Stronghold", font=font, bg=bg, fg=fg, width=width, command=stronghold)
    button_swamp_hut = Button(text="Swamp Hut", font=font, bg=bg, fg=fg, width=width, command=swamp_hut)
    button_village = Button(text="Village", font=font, bg=bg, fg=fg, width=width, command=village)
    button_wooden_mansion = Button(text="Woodland Mansion", font=font, bg=bg, fg=fg, width=width, command=wooden_mansion)
    button_clear = Button(text="Clear", font=font, bg="#cccccc", fg=fg, width=width, command=clear)
    button_settings = Button(text="Settings", font=font, bg="#cccccc", fg=fg, width=width, command=settings)

    button_bastion.grid(row=0, column=0)
    button_burried_treasure.grid(row=0, column=1)
    button_desert_pyramid.grid(row=1, column=0)
    button_end_city.grid(row=1, column=1)
    button_igloo.grid(row=2, column=0)
    button_jungle_temple.grid(row=2, column=1)
    button_mineshaft.grid(row=3, column=0)
    button_nether_fortress.grid(row=3, column=1)
    button_nether_fossil.grid(row=4, column=0)
    button_ocean_monument.grid(row=4, column=1)
    button_ocean_ruins.grid(row=5, column=0)
    button_pillager_outpost.grid(row=5, column=1)
    button_ruined_portal.grid(row=6, column=0)
    button_shipwreck.grid(row=6, column=1)
    button_stronghold.grid(row=7, column=0)
    button_swamp_hut.grid(row=7, column=1)
    button_village.grid(row=8, column=0)
    button_wooden_mansion.grid(row=8, column=1)
    button_clear.grid(row=9, column=0)
    button_settings.grid(row=9, column=1)

def overlay_function():

    file = open("settings.txt", mode="r")
    the_settings = file.readlines()
    file.close()

    global display_number
    display_number = int(the_settings[1].replace("STRUCTURES_SHOWN=", "").replace("\n", ""))
    background_color = str(the_settings[3].replace("OVERLAY_BACKGROUND=", "").replace("\n", ""))
    displayed_icon = str(the_settings[4].replace("PREVIEWS=", "").replace("\n", ""))
    scrolling_speed = float(the_settings[5].replace("SCROLLING_SPEED=", "").replace("\n", ""))

    window_overlay_icon = pygame.image.load('assets/icon.png')
    window_overlay = pygame.display.set_mode((display_number*120, 140))
    pygame.display.set_caption('All Structures Overlay')
    pygame.display.set_icon(window_overlay_icon)
    global opened
    opened = True

    dict_images = {
        "bastion.png": pygame.image.load("assets/" + displayed_icon + "/bastion.png"),
        "burried_treasure.png": pygame.image.load("assets/" + displayed_icon + "/burried_treasure.png"),
        "desert_pyramid.png": pygame.image.load("assets/" + displayed_icon + "/desert_pyramid.png"),
        "end_city.png": pygame.image.load("assets/" + displayed_icon + "/end_city.png"),
        "igloo.png": pygame.image.load("assets/" + displayed_icon + "/igloo.png"),
        "jungle_temple.png": pygame.image.load("assets/" + displayed_icon + "/jungle_temple.png"),
        "mineshaft.png": pygame.image.load("assets/" + displayed_icon + "/mineshaft.png"),
        "nether_fortress.png": pygame.image.load("assets/" + displayed_icon + "/nether_fortress.png"),
        "nether_fossil.png": pygame.image.load("assets/" + displayed_icon + "/nether_fossil.png"),
        "ocean_monument.png": pygame.image.load("assets/" + displayed_icon + "/ocean_monument.png"),
        "ocean_ruins.png": pygame.image.load("assets/" + displayed_icon + "/ocean_ruins.png"),
        "pillager_outpost.png": pygame.image.load("assets/" + displayed_icon + "/pillager_outpost.png"),
        "ruined_portal.png": pygame.image.load("assets/" + displayed_icon + "/ruined_portal.png"),
        "shipwreck.png": pygame.image.load("assets/" + displayed_icon + "/shipwreck.png"),
        "stronghold.png": pygame.image.load("assets/" + displayed_icon + "/stronghold.png"),
        "swamp_hut.png": pygame.image.load("assets/" + displayed_icon + "/swamp_hut.png"),
        "village.png": pygame.image.load("assets/" + displayed_icon + "/village.png"),
        "wooden_mansion.png": pygame.image.load("assets/" + displayed_icon + "/wooden_mansion.png"),
    }

    positions = []
    x = 10
    for i in range(display_number+2):
        positions.append(x)
        x = x + 140

    while opened:
        window_overlay.fill(background_color)
        nb_index = 0
        for i in range(display_number+2):
            if structures_copy != []:
                name = structures_copy[nb_index]
                image = pygame.transform.scale(dict_images[name], (120, 120))
                window_overlay.blit(image, (positions[i], 10))
                positions[i] = positions[i] - scrolling_speed

                if positions[i] < -240:
                    structures_copy.append(structures_copy[0])
                    structures_copy.pop(0)
                    positions.pop(0)
                    positions.append(positions[-1]+140)

                nb_index = nb_index + 1
                if nb_index > len(structures_copy)-1:
                    nb_index = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opened = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    thread2 = Thread(target=buttons_function, args=())
    thread = Thread(target=overlay_function, args=())
    thread.start()
    thread2.start()

    window_buttons.mainloop()
    opened = False