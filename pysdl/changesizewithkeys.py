#!/usr/bin/env python3
import sdl2.ext

window_size = [800, 450]
resizing_speed = 50

sdl2.ext.init()
window = sdl2.ext.Window("ζ : use arrows to resize window!", size=window_size)
window.show()

done = False
while not done:
    size_changed = False
    for event in sdl2.ext.get_events():
        done |= event.type == sdl2.SDL_QUIT
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_UP:
                window_size[1] += 50
                size_changed = True
            elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                window_size[1] -= 50
                size_changed = True
    if size_changed:
        window.size = window_size
    window.refresh()
