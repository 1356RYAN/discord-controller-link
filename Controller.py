import asyncio

import vgamepad as vg
import time
controller = vg.VX360Gamepad()

# initilize controller
controller.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
controller.update()
time.sleep(0.25)
controller.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
controller.update()
time.sleep(0.25)


async def move_left_joystick(x_value, y_value, duration):
    controller.left_joystick_float(x_value_float = x_value, y_value_float = y_value)
    controller.update()
    await asyncio.sleep(duration)
    controller.left_joystick_float(x_value_float = 0, y_value_float = 0)
    controller.update()

async def move_right_joystick(x_value, y_value, duration):
    controller.right_joystick_float(x_value_float = x_value, y_value_float = y_value)
    controller.update()
    await asyncio.sleep(duration)
    controller.right_joystick_float(x_value_float = 0, y_value_float = 0)
    controller.update()

async def left_trigger_click(duration):
    controller.left_trigger_float(value_float = 1)
    controller.update()
    await asyncio.sleep(duration)
    controller.left_trigger_float(value_float = 0)
    controller.update()

async def right_trigger_click(duration):
    controller.right_trigger_float(value_float = 1)
    controller.update()
    await asyncio.sleep(duration)
    controller.right_trigger_float(value_float = 0)
    controller.update()

async def gamepad_left(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    controller.update()

async def gamepad_right(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    controller.update()

async def gamepad_down(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    controller.update()

async def gamepad_up(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    controller.update()

async def press_A(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    controller.update()

async def press_B(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    controller.update()

async def press_X(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    controller.update()

async def press_Y(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    controller.update()

async def press_left_shoulder(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    controller.update()

async def press_right_shoulder(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    controller.update()

async def press_left_joystick(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    controller.update()

async def press_right_joystick(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    controller.update()

async def start(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    controller.update()

async def back(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    controller.update()

async def guide(duration):
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
    controller.update()
    await asyncio.sleep(duration)
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
    controller.update()

async def reset():
    controller.reset()
    controller.update()