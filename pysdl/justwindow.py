import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("Very original window title", size=(800, 450))
window.show()
sdl2.ext.TestEventProcessor().run(window)
