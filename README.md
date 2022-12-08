# All Structures Tracker

The **All Structures Tracker** is a tool to track your [All Structures](https://speedrun.com/mc_juice#All_Structures) runs.

## Installation

- Go to the [releases](https://github.com/Arthurprnt/AllStructuresTracker/releases) page and download the latest version of the tracker.
- Extract the files from the zip file
- Double click on `ASTracker.exe`

## Overlay

The tracker comes with an overlay for those who stream. To add it on OBS just add a window capture.

![windowcapture](https://user-images.githubusercontent.com/93857989/206451574-1116e001-5574-4e70-8c7d-c9e0801b0f4d.png)

Once done, don't forget to apply a color key filer on the source.

![filter](https://user-images.githubusercontent.com/93857989/206451940-3525e4a3-1b25-41fd-8a55-bb9c0e7f8e66.png)

## Twitch extension

You can use a Twitch extension to let yours Twitch mods switch the structures for you. All you have to do is fill the required informations in the `settings.txt`. To switch a structure use the command `!switch <structure>`. Here are all the structures names:
- bastion_remnant
- burried_treasure
- desert_pyramid
- end_city
- igloo
- jungle_temple
- mineshaft
- nether_fortress
- nether_fossil
- ocean_monument
- ocean_ruins
- pillager_outpost
- ruined_portal
- shipwreck
- stronghold
- swamp_hut
- village
- woodland_mansion
You can also clear all the structures with only one command : `!clear`.

## Settings

The tracker also comes with some settings, here they are:

- `CLICKED_BUTTONS`: Change the color of the button when the structure is checked.
- `DARK_MODE`: Allow you to choose if you want to use the dark mode (True for yes and False for no).
- `OVERLAY_BACKGROUND`: Change the background color of the overlay.
- `PREVIEWS`: Change the icons set that will be displayed on the overlay (ICONS or BLOCS).
- `SCROLLING_SPEED`: Change the scrolling speed of the icons on the overlay (can't be negative).
- `STRUCTURES_SHOWN`: Change the number of structures displayed on the overlay.
- `TWITCH_TOKEN`: Must be filled if you use the Twitch extension. The token can be find [here](https://twitchapps.com/tmi/) (you must be connected to the account you use to stream).
- `TWITCH_USERNAME`: Your Twitch channel name.
- `USE_TWITCH_BOT`: Allow you to choose if you want to use the Twitch extension (True for yes and False for no).
