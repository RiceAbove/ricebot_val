import os, time, pyautogui
from twitchio.ext import commands

# Things to finish for bot:
# - [X] Fix burst
# - [NO] Camera movement
# - [X] Abilities
# - [X] Plant/Defuse Spike

# Safety stuff from pyautogui
pyautogui.PAUSE = 2.5
pyautogui.FAILSALE = True

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=os.environ['IRC_TOKEN'], 
            client_id=os.environ['CLIENT_ID'], 
            nick='rice_above', 
            prefix='!',
            initial_channels=['rice_above'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')
        ws = bot._ws
        await ws.send_privmsg('rice_above', f"/me has landed!")

    # Bot reads messages from chat
    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name='test')
    async def my_command(self, ctx):
        print("This is a test")
        await ctx.send(f'Hello {ctx.author.name}!')

    # Move character left
    @commands.command(name='a')
    async def move_left(self, ctx):
        print("Moving left")
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        # await ctx.send(f'You have moved left for 2 second!')

    # Move character right
    @commands.command(name='d')
    async def move_right(self, ctx):
        print("Moving right")
        pyautogui.keyDown('d')
        pyautogui.keyUp('d')
        # await ctx.send(f'You have moved right for 2 second!')

    # Move character forward
    @commands.command(name='w')
    async def move_forward(self, ctx):
        print("Moving forward")
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
        # await ctx.send(f'You have moved forward for 2 second!')

    # Move character back
    @commands.command(name='s')
    async def move_back(self, ctx):
        print("Moving back")
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')
        # await ctx.send(f'You have moved back for 2 second!')

    # Make character jump
    @commands.command(name='space')
    async def jump(self, ctx):
        print("Jump")
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        # await ctx.send(f'You have moved back for 2 second!')

    # Primary weapon
    @commands.command(name='primary')
    async def primary(self, ctx):
        print("Primary weapon")
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')

    # Secondary weapon
    @commands.command(name='pistol')
    async def pistol(self, ctx):
        print("Secondary weapon")
        pyautogui.keyDown('2')
        pyautogui.keyUp('2')

    # Knife
    @commands.command(name='knife')
    async def knife(self, ctx):
        print("Knife")
        pyautogui.keyDown('3')
        pyautogui.keyUp('3')

    # Tap shoot once
    @commands.command(name='one_tap')
    async def tap(self, ctx):
        print("One Tap Shooting")
        pyautogui.click()

    # Tap shoot three times
    @commands.command(name='three_taps')
    async def burst(self, ctx):
        print("Three Tap Shooting")
        pyautogui.click(clicks=3, interval=0.99)

    # Spray shoot
    @commands.command(name='spray')
    async def spray(self, ctx):
        print("Spray Shooting")
        pyautogui.moveTo(960, 540)
        pyautogui.dragTo(960, 1080, 1, button='left')

    # Plant Spike
    @commands.command(name='plant')
    async def plant(self, ctx):
        print("Planting spike")
        pyautogui.keyDown('4')
        time.sleep(2)
        pyautogui.keyUp('4')


    # Defuse Spike
    @commands.command(name='defuse')
    async def defuse(self, ctx):
        print("Defusing Spike")
        pyautogui.keyDown(w'4')
        time.sleep(10)
        pyautogui.keyUp('4')

    # We will be using Phoenix's abilities, but you can
    # change the control accordingly based on your keyboard
    # set up and character that you choose

    # Blaze
    @commands.command(name='blaze')
    async def blaze(self, ctx):
        print("Blaze")
        pyautogui.press('c')

    # Curveball
    @commands.command(name='curveball')
    async def curveball(self, ctx):
        print("Curveball")
        pyautogui.press('q')


    # Hot Hands
    @commands.command(name='hot_hands')
    async def hot_hands(self, ctx):
        print("Hot Hands")
        pyautogui.press('e')


    # Run It Back
    @commands.command(name='ult')
    async def run_it_back(self, ctx):
        print("Run It Back")
        pyautogui.press('x')

    


bot = Bot()
bot.run()