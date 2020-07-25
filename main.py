import time, os, pyautogui
from twitchio.ext import commands

# Safety stuff from pyautogui
pyautogui.PAUSE = 2.5
pyautogui.FAILSALE = True

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=os.environ['IRC_TOKEN'], 
            client_id=os.environ['CLIENT_ID'], 
            nick=os.environ['USERNAME'], 
            prefix='!',
            initial_channels=[os.environ['USERNAME']])

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

    # Testing pyautogui
    @commands.command(name='pyautogui')
    async def pyautogui(self, ctx):
        print("Testing pyautogui")
        time.sleep(2)
        pyautogui.typewrite('Hello world!', interval=0.25)
        await ctx.send(f'Thank you for testing {ctx.author.name}!')

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

    # Tap shoot
    @commands.command(name='tap')
    async def tap(self, ctx):
        print("Tap Shooting")
        pyautogui.click()

    # Burst shoot
    @commands.command(name='burst')
    async def burst(self, ctx):
        print("Burst Shooting")
        pyautogui.click(clicks=3, interval=0.75)

    # Spray shoot
    @commands.command(name='spray')
    async def spray(self, ctx):
        print("Spray Shooting")
        pyautogui.mouseDown()
        pyautogui.mouseUp()



# time.sleep(2)
# pyautogui.typewrite('Hello world!', interval=0.25)



bot = Bot()
bot.run()