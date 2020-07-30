# RiceBot Valorant
A Twitch chatbot that lets users in chat play VALORANT

## About
I was inspired by DougDoug when he had Twitch chat beat a single level of Mario 64. [Video here](https://youtu.be/VqlDyEwtFlY).
Because of this, I was inspired to create a Twitch bot that also took commands from Twitch chat in order to play Riot's new
FPS shooter VALORANT. If you guys are interested in checking out my stream, you can check it out [here](https://www.twitch.tv/rice_above).

## Built With
- Python
- [TwitchIO](https://github.com/TwitchIO/TwitchIO)
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [pydirectinput](https://github.com/learncodebygaming/pydirectinput) - Not implemented, but could be used for future updates to replace PyAutoGUI

## License
This project is licensed under the [GPL-3.0](LICENSE) - see the LICENSE file for details

## Contributors 
- **Gico Carlo Evangelista** - [RiceAbove](https://github.com/RiceAbove), evangelistagico@gmail.com - Creator 

# Commands 
### Character Movement

- !a: Left
- !d: Right
- !w: Forward
- !s: Backwards
- !space: Jump

### Camera Movement
Sadly no Python libraries support camera movement in Valorant. If you find a fix for this please submit a PR. Thank you!

### Switching Weapons

- !rifle
- !pistol
- !knife

### Shooting Weapon

- !one_tap
- !three_tap
- !spray

### Spike Related Commands

- !plant
- !defuse

### Character Abilities
NOTE: We will be using Phoenix's abilities, but you can
change the controls accordingly based on your keyboard
set up and character that you choose

- !blaze: Blaze
- !curve: Curveball
- !hot: Hot Hands
- !ult: Run It Back
