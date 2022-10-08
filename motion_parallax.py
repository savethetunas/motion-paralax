from graphics import graphics


def main():
    gui = graphics(666, 666, 'parallax')
    sky(gui)
    sun(gui)
    mountains(gui)
    grass(gui)
    gui.draw()


def sky(gui):
    gui.rectangle(0, 0, 665, 665, 'blue')


def sun(gui):
    gui.ellipse(500, 100, 100, 100, 'yellow')


def mountains(gui):
    gui.triangle(133, 666, 566, 666, 333, 300, 'pink')
    gui.triangle(-100, 666, 333, 666, 130, 233, 'orange')
    gui.triangle(300, 666, 777, 666, 533, 233, 'purple')


def grass(gui):
    gui.rectangle(0, 533, 665, 665, 'green')
    i = 10
    while i <= 666:
        gui.rectangle(i, 483, 5, 50, 'white')
        i += 20
    gui.rectangle(420, 520, 33, 75, 'brown')
    gui.ellipse(434, 450, 100, 150, 'black')



main()
