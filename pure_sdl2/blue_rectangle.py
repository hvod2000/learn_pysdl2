#!/usr/bin/env python3

from sdl2 import *

SDL_Init(SDL_INIT_VIDEO)
width, height = 800, 450
window = SDL_CreateWindow(
    "υ: window with a rectangle a the center".encode(),
    SDL_WINDOWPOS_CENTERED,
    SDL_WINDOWPOS_CENTERED,
    width,
    height,
    SDL_WINDOW_SHOWN,
)
render = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)

done = False
while not done:
    e = SDL_Event()
    while SDL_PollEvent(e):
        done |= e.type == SDL_QUIT
    SDL_SetRenderDrawColor(render, 0, 0, 0, 0xFF)
    SDL_RenderClear(render)
    SDL_SetRenderDrawColor(render, 0, 0, 0x42, 0xFF)
    rect = SDL_Rect(width // 4, height // 4, width // 2, height // 2)
    SDL_RenderFillRect(render, rect)
    SDL_SetRenderDrawColor(render, 0, 0, 0x21, 0xFF)
    rect = SDL_Rect(width // 3, height // 3, width // 3, height // 3)
    SDL_RenderFillRect(render, rect)
    SDL_RenderPresent(render)
SDL_DestroyWindow(window)
SDL_Quit()
