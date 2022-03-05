#!/usr/bin/env python3

from sdl2 import *

window_size = [800, 450]
resizing_speed = 50

SDL_Init(SDL_INIT_VIDEO)
window = SDL_CreateWindow(
    "ζ : use arrows to resize window!".encode(),
    SDL_WINDOWPOS_CENTERED,
    SDL_WINDOWPOS_CENTERED,
    window_size[0],
    window_size[1],
    SDL_WINDOW_SHOWN,
)

done = False
while not done:
    size_changed = False
    e = SDL_Event()
    while SDL_PollEvent(e):
        done |= e.type == SDL_QUIT
        if e.type == SDL_KEYDOWN:
            if e.key.keysym.sym == SDLK_UP:
                window_size[1] += 50
                size_changed = True
            elif e.key.keysym.sym == SDLK_DOWN:
                window_size[1] -= 50
                size_changed = True
    if size_changed:
        SDL_SetWindowSize(window, window_size[0], window_size[1])
    SDL_UpdateWindowSurface(window)


SDL_DestroyWindow(window)
SDL_Quit()
