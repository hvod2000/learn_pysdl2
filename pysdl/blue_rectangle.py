#!/usr/bin/env python3
import sdl2.ext

width, height = 800, 450
sdl2.ext.init()
window = sdl2.ext.Window(
    "υ: window with a rectangle a the center", size=(width, height)
)
window.show()
render = sdl2.ext.Renderer(window)

done = False
while not done:
    for event in sdl2.ext.get_events():
        done |= event.type == sdl2.SDL_QUIT
    render.clear((0, 0, 0))
    rect = (width // 4, height // 4, width // 2, height // 2)
    render.fill([rect], (0, 0, 0x42))
    rect = (width // 3, height // 3, width // 3, height // 3)
    render.fill([rect], (0, 0, 0x21))
    render.present()
