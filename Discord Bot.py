import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import Controller
import os
from pathlib import Path
import sys

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='c', intents=intents)
controller_lock = asyncio.Lock()
active_controller_task = None

async def run_controller(function, *args):
    global active_controller_task

    async with controller_lock:
        active_controller_task = asyncio.current_task()
        try:
            await function(*args)
        finally:
            active_controller_task = None

@bot.command()
async def left_stick(ctx, x_value: float, y_value: float, duration: float = 1):
    await run_controller(Controller.move_left_joystick, x_value, y_value, duration)

@bot.command()
async def right_stick(ctx, x_value: float, y_value: float, duration: float = 1):
    await run_controller(Controller.move_right_joystick, x_value, y_value, duration)

@bot.command()
async def left_trigger(ctx, duration: float = .1):
    await run_controller(Controller.left_trigger_click, duration)

@bot.command()
async def right_trigger(ctx, duration: float = .1):
    await run_controller(Controller.right_trigger_click, duration)

@bot.command()
async def left(ctx, duration: float = .1):
    await run_controller(Controller.gamepad_left, duration)

@bot.command()
async def right(ctx, duration: float = .1):
    await run_controller(Controller.gamepad_right, duration)

@bot.command()
async def down(ctx, duration: float = .1):
    await run_controller(Controller.gamepad_down, duration)

@bot.command()
async def up(ctx, duration: float = .1):
    await run_controller(Controller.gamepad_up, duration)

@bot.command()
async def A(ctx, duration: float = .1):
    await run_controller(Controller.press_A, duration)

@bot.command()
async def B(ctx, duration: float = .1):
    await run_controller(Controller.press_B, duration)

@bot.command()
async def X(ctx, duration: float = .1):
    await run_controller(Controller.press_X, duration)

@bot.command()
async def Y(ctx, duration: float = .1):
    await run_controller(Controller.press_Y, duration)

@bot.command()
async def left_shoulder(ctx, duration: float = .1):
    await run_controller(Controller.press_left_shoulder, duration)

@bot.command()
async def right_shoulder(ctx, duration: float = .1):
    await run_controller(Controller.press_right_shoulder, duration)

@bot.command()
async def right_stickpress(ctx, duration: float = 1):
    await run_controller(Controller.press_right_joystick, duration)

@bot.command()
async def left_stickpress(ctx, duration: float = 1):
    await run_controller(Controller.press_left_joystick, duration)

@bot.command()
async def start(ctx, duration: float = 1):
    await run_controller(Controller.start, duration)

@bot.command()
async def back(ctx, duration: float = 1):
    await run_controller(Controller.back, duration)

@bot.command()
async def guide(ctx, duration: float = 1):
    await run_controller(Controller.guide, duration)

@bot.command()
async def reset(ctx):
    global active_controller_task

    if active_controller_task is not None:
        active_controller_task.cancel()
        try:
            await active_controller_task
        except asyncio.CancelledError:
            pass

    await run_controller(Controller.reset)

class GroupedHelpCommand(commands.HelpCommand):
    command_groups = {
        "Joysticks": {"left_stick", "right_stick", "left_stickpress", "right_stickpress"},
        "Triggers": {"left_trigger", "right_trigger"},
        "D-pad": {"left", "right", "up", "down"},
        "Buttons": {"A", "B", "X", "Y", "left_shoulder", "right_shoulder"},
    }

    async def send_bot_help(self, mapping):
        grouped_commands = {group: [] for group in self.command_groups}
        grouped_commands["Other"] = []

        for command in self.context.bot.commands:
            group = next(
                (name for name, commands_in_group in self.command_groups.items()
                 if command.name in commands_in_group),
                "Other",
            )
            grouped_commands[group].append(command)

        lines = ["**Commands**"]
        for group, commands_in_group in grouped_commands.items():
            if not commands_in_group:
                continue

            lines.append(f"\n**{group}**")
            for command in sorted(commands_in_group, key=lambda item: item.name.lower()):
                signature = f" {command.signature}" if command.signature else ""
                description = f" - {command.help}" if command.help else ""
                lines.append(f"`c{command.name}{signature}`{description}")

        await self.get_destination().send("\n".join(lines))


bot.help_command = GroupedHelpCommand()

if getattr(sys, 'frozen', False):

    base_dir = Path(sys.executable).parent
else:
    base_dir = Path(__file__).parent

load_dotenv(base_dir / "Bot.env")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))