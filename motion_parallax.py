from graphics import graphics
import random


def main():
    gui = graphics(666, 666, 'parallax')
    sky(gui)
    sun(gui)
    mountains(gui)
    mountains_0(gui)
    foreground(gui)
    gui.draw()


def sky(gui):
    gui.rectangle(0, 0, 665, 665, 'PowderBlue')  # Sky


def sun(gui):
    gui.ellipse(585, 95, 100, 100, 'yellow')



def mountains(gui):
    red_0 = random.randint(0, 255)
    green_0 = random.randint(0, 255)
    blue_0 = random.randint(0, 255)
    color_string_0 = gui.get_color_string(red_0, green_0, blue_0)
    gui.triangle(58, 666, 600, 699, 320, 183, color_string_0)


def mountains_0(gui):
    red_1 = random.randint(0, 255)
    red_2 = random.randint(0, 255)
    green_1 = random.randint(0, 255)
    green_2 = random.randint(0, 255)
    blue_1 = random.randint(0, 255)
    blue_2 = random.randint(0, 255)
    color_string_1 = gui.get_color_string(red_1, green_1, blue_1)
    color_string_2 = gui.get_color_string(red_2, green_2, blue_2)
    gui.triangle(-250, 666, 500, 666, 123, 233, color_string_1)
    gui.triangle(123, 666, 888, 666, 482, 233, color_string_2)


def foreground(gui):
    gui.rectangle(0, 480, 665, 665, 'medium spring green')  # grass field
    i = -1
    while i <= 667:
        gui.rectangle(i, 430, 2, 50, 'forest green')  # grass blades
        i += 3 ** 2
    gui.rectangle(420, 520, 33, 75, 'saddle brown')  # tree trunk
    gui.ellipse(434, 450, 100, 150, 'dark green')  # tree top
    gui.ellipse(200, 550, 150, 100, 'royal blue')  # pond

    ### START BORBS ###
    x = 40
    y = 90
    x2 = 80
    y2 = 107
    i = 0
    while i < 5:
        gui.line(x, y, x2, y2, 'black', 2)
        gui.line(x2, y2, x2 + 40, y, 'black', 2)
        x = x + 100
        y = y + 20
        x2 = x2 + 100
        y2 = y2 + 20
        i += 1
    ### END BORBS ###


main()
