from tkinter import *
import pygame
import os
import threading
from twitchio.ext import commands
import subprocess
import keyboard

env = {}
file = open("settings.txt", mode="r")
the_settings = file.readlines()
for i in the_settings:
    if i[0] == "#":
        pass
    else:
        setting = i.split("=")
        setting[1] = setting[1].replace("\n", "")
        env[setting[0]] = setting[1]
file.close()

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=str(env["TWITCH_TOKEN"]), prefix="!", initial_channels=[str(env["TWITCH_USERNAME"])])

    async def event_ready(self):
        print(f'Logged in as {self.nick}')
        print((f'User id is {self.nick}'))

    @commands.command()
    async def switch(self, ctx: commands.Context):
        if ctx.author.is_mod:
            structure = ctx.message.content.split(" ")[1]
            if structure in add_n_sup_functions.keys():
                add_n_sup_functions[structure]()
                await ctx.send(f"The structure has been switch by {ctx.author.name}.")
                print(f"The structure has been switch by {ctx.author.name}.")
            else:
                await ctx.send(f"@{ctx.author.name}, this structure don't exist.")
        else:
            await ctx.send(f"You can't switch a structure as you're not mod.")

    @commands.command()
    async def clear(self, ctx: commands.Context):
        if ctx.author.is_mod:
            add_n_sup_functions["clear"]()
            await ctx.send(f"The grid has been cleared by {ctx.author.name}.")
            print(f"The grid has been cleared by {ctx.author.name}.")
        else:
            await ctx.send(f"You can't clear the grid as you're not mod.")

bot = Bot()

window_buttons = Tk()
sizes = {
    "1": ((224, 250), "8"),
    "2": ((325, 300), "11"),
    "3": ((393, 400), "15")
}
window_buttons.title("All Structures Tracker by DraquoDrass")
window_buttons.iconbitmap("assets/icon.ico")
window_buttons.geometry(str(sizes[str(env["BUTTONS_WINDOW_SIZE"])][0][0]) + "x" + str(sizes[str(env["BUTTONS_WINDOW_SIZE"])][0][1]))
window_buttons.minsize(str(sizes[str(env["BUTTONS_WINDOW_SIZE"])][0][0]), str(sizes[str(env["BUTTONS_WINDOW_SIZE"])][0][1]))
window_buttons.maxsize(str(sizes[str(env["BUTTONS_WINDOW_SIZE"])][0][0]), str(sizes[str(env["BUTTONS_WINDOW_SIZE"])][0][1]))
if str(env["ALWAYS_ON_TOP"]) == "True":
    window_buttons.attributes('-topmost', True)

font = (f"Arial, {str(sizes[str(env['BUTTONS_WINDOW_SIZE'])][1])}")
if str(env["DARK_MODE"]) == "True":
    bg = "#32393d"
    fg = "#ffffff"
    bgs = "#1a1e21"
    fgs = "#ffffff"
else:
    bg = "#ffffff"
    fg = "#000000"
    bgs = "#cccccc"
    fgs = "#000000"
changed_bg = str(env["CLICKED_BUTTONS"])
width = 17

global structures
structures = []
for filenames in os.walk("assets/BLOCS/"):
    structures.extend(filenames)
structures = structures[2]
global structures_copy
structures_copy = list(structures)

def buttons_function():
    def bastion_remnant():
        if "bastion_remnant.png" in structures_copy:
            while "bastion_remnant.png" in structures_copy:
                button_bastion_remnant.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("bastion_remnant.png"))
        else:
            button_bastion_remnant.configure(bg=bg, fg=fg)
            structures_copy.append("bastion_remnant.png")

    def burried_treasure():
        if "burried_treasure.png" in structures_copy:
            while "burried_treasure.png" in structures_copy:
                button_burried_treasure.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("burried_treasure.png"))
        else:
            button_burried_treasure.configure(bg=bg, fg=fg)
            structures_copy.append("burried_treasure.png")

    def desert_pyramid():
        if "desert_pyramid.png" in structures_copy:
            while "desert_pyramid.png" in structures_copy:
                button_desert_pyramid.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("desert_pyramid.png"))
        else:
            button_desert_pyramid.configure(bg=bg, fg=fg)
            structures_copy.append("desert_pyramid.png")

    def end_city():
        if "end_city.png" in structures_copy:
            while "end_city.png" in structures_copy:
                button_end_city.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("end_city.png"))
        else:
            button_end_city.configure(bg=bg, fg=fg)
            structures_copy.append("end_city.png")

    def igloo():
        if "igloo.png" in structures_copy:
            while "igloo.png" in structures_copy:
                button_igloo.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("igloo.png"))
        else:
            button_igloo.configure(bg=bg, fg=fg)
            structures_copy.append("igloo.png")

    def jungle_temple():
        if "jungle_temple.png" in structures_copy:
            while "jungle_temple.png" in structures_copy:
                button_jungle_temple.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("jungle_temple.png"))
        else:
            button_jungle_temple.configure(bg=bg, fg=fg)
            structures_copy.append("jungle_temple.png")

    def mineshaft():
        if "mineshaft.png" in structures_copy:
            while "mineshaft.png" in structures_copy:
                button_mineshaft.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("mineshaft.png"))
        else:
            button_mineshaft.configure(bg=bg, fg=fg)
            structures_copy.append("mineshaft.png")

    def nether_fortress():
        if "nether_fortress.png" in structures_copy:
            while "nether_fortress.png" in structures_copy:
                button_nether_fortress.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("nether_fortress.png"))
        else:
            button_nether_fortress.configure(bg=bg, fg=fg)
            structures_copy.append("nether_fortress.png")

    def nether_fossil():
        if "nether_fossil.png" in structures_copy:
            while "nether_fossil.png" in structures_copy:
                button_nether_fossil.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("nether_fossil.png"))
        else:
            button_nether_fossil.configure(bg=bg, fg=fg)
            structures_copy.append("nether_fossil.png")

    def ocean_monument():
        if "ocean_monument.png" in structures_copy:
            while "ocean_monument.png" in structures_copy:
                button_ocean_monument.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("ocean_monument.png"))
        else:
            button_ocean_monument.configure(bg=bg, fg=fg)
            structures_copy.append("ocean_monument.png")

    def ocean_ruins():
        if "ocean_ruins.png" in structures_copy:
            while "ocean_ruins.png" in structures_copy:
                button_ocean_ruins.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("ocean_ruins.png"))
        else:
            button_ocean_ruins.configure(bg=bg, fg=fg)
            structures_copy.append("ocean_ruins.png")

    def pillager_outpost():
        if "pillager_outpost.png" in structures_copy:
            while "pillager_outpost.png" in structures_copy:
                button_pillager_outpost.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("pillager_outpost.png"))
        else:
            button_pillager_outpost.configure(bg=bg, fg=fg)
            structures_copy.append("pillager_outpost.png")

    def ruined_portal():
        if "ruined_portal.png" in structures_copy:
            while "ruined_portal.png" in structures_copy:
                button_ruined_portal.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("ruined_portal.png"))
        else:
            button_ruined_portal.configure(bg=bg, fg=fg)
            structures_copy.append("ruined_portal.png")

    def shipwreck():
        if "shipwreck.png" in structures_copy:
            while "shipwreck.png" in structures_copy:
                button_shipwreck.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("shipwreck.png"))
        else:
            button_shipwreck.configure(bg=bg, fg=fg)
            structures_copy.append("shipwreck.png")

    def stronghold():
        if "stronghold.png" in structures_copy:
            while "stronghold.png" in structures_copy:
                button_stronghold.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("stronghold.png"))
        else:
            button_stronghold.configure(bg=bg, fg=fg)
            structures_copy.append("stronghold.png")

    def swamp_hut():
        if "swamp_hut.png" in structures_copy:
            while "swamp_hut.png" in structures_copy:
                button_swamp_hut.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("swamp_hut.png"))
        else:
            button_swamp_hut.configure(bg=bg, fg=fg)
            structures_copy.append("swamp_hut.png")

    def village():
        if "village.png" in structures_copy:
            while "village.png" in structures_copy:
                button_village.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("village.png"))
        else:
            button_village.configure(bg=bg, fg=fg)
            structures_copy.append("village.png")

    def wooden_mansion():
        if "wooden_mansion.png" in structures_copy:
            while "wooden_mansion.png" in structures_copy:
                button_wooden_mansion.configure(bg=changed_bg, fg=fg)
                structures_copy.pop(structures_copy.index("wooden_mansion.png"))
        else:
            button_wooden_mansion.configure(bg=bg, fg=fg)
            structures_copy.append("wooden_mansion.png")

    def clear():
        button_bastion_remnant.configure(bg=bg, fg=fg)
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
        while structures_copy != []:
            structures_copy.pop()
        for i in structures:
            structures_copy.append(i)

    global add_n_sup_functions
    add_n_sup_functions = {
        "bastion_remnant": bastion_remnant,
        "burried_treasure": burried_treasure,
        "desert_pyramid": desert_pyramid,
        "end_city": end_city,
        "igloo": igloo,
        "jungle_temple": jungle_temple,
        "mineshaft": mineshaft,
        "nether_fortress": nether_fortress,
        "nether_fossil": nether_fossil,
        "ocean_monument": ocean_monument,
        "ocean_ruins": ocean_ruins,
        "pillager_outpost": pillager_outpost,
        "ruined_portal": ruined_portal,
        "shipwreck": shipwreck,
        "stronghold": stronghold,
        "swamp_hut": swamp_hut,
        "village": village,
        "wooden_mansion": wooden_mansion,
        "clear": clear
    }

    def settings():
        subprocess.Popen('explorer "settings.txt"')

    button_bastion_remnant = Button(text="Bastion Remnant", font=font, bg=bg, fg=fg, width=width, command=bastion_remnant)
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
    button_clear = Button(text="Clear", font=font, bg=bgs, fg=fgs, width=width, command=clear)
    button_settings = Button(text="Settings", font=font, bg=bgs, fg=fgs, width=width, command=settings)

    button_bastion_remnant.grid(row=0, column=0)
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

    env = {}
    file = open("settings.txt", mode="r")
    the_settings = file.readlines()
    for i in the_settings:
        if i[0] == "#":
            pass
        else:
            setting = i.split("=")
            setting[1] = setting[1].replace("\n", "")
            env[setting[0]] = setting[1]
    file.close()

    global display_number
    display_number = int(env["STRUCTURES_SHOWN"])
    background_color = str(env["OVERLAY_BACKGROUND"])
    displayed_icon = str(env["PREVIEWS"])
    scrolling_speed = float(env["SCROLLING_SPEED"])

    window_overlay_icon = pygame.image.load('assets/icon.png')
    window_overlay = pygame.display.set_mode((display_number*120, 140))
    pygame.display.set_caption('All Structures Overlay')
    pygame.display.set_icon(window_overlay_icon)
    global opened
    opened = True

    dict_images = {
        "bastion_remnant.png": pygame.image.load("assets/" + displayed_icon + "/bastion_remnant.png"),
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

        if keyboard.is_pressed(str(env["RESET_KEY"])):
            add_n_sup_functions["clear"]()

        pygame.display.flip()

    pygame.quit()

def twitch_function():
    if str(env["USE_TWITCH_BOT"]) == "True":
        bot.run()
        window_buttons.mainloop()
    else:
        pass

if __name__ == "__main__":
    thread3 = threading.Thread(target=twitch_function, args=())
    thread2 = threading.Thread(target=buttons_function, args=())
    thread = threading.Thread(target=overlay_function, args=())
    thread3.start()
    thread.start()
    thread2.start()


    window_buttons.mainloop()
    opened = False