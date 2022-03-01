from sdl2 import *

SDL_Init(SDL_INIT_VIDEO)
window = SDL_CreateWindow(
    "Very original window title with unicode: αβγ".encode(),
    SDL_WINDOWPOS_CENTERED,
    SDL_WINDOWPOS_CENTERED,
    800,
    450,
    SDL_WINDOW_SHOWN,
)

done = False
while not done:
    e = SDL_Event()
    while SDL_PollEvent(e):
        done |= e.type == SDL_QUIT
SDL_DestroyWindow(window)
SDL_Quit()
