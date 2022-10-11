from graphics import graphics
import random


def sky(gui):
    gui.rectangle(0, 0, 700, 750, 'PowderBlue')  # Sky


def sun(gui):
    x = gui.mouse_x / 50 + 600
    y = gui.mouse_y / 50 + 150
    gui.ellipse(x - 50, y - 50, 100, 100, 'yellow')


def mountains(gui, color_string):
    x = gui.mouse_x / 15
    y = gui.mouse_y / 15

    gui.triangle(x, y + 750, x + 700, y + 750, x + 350, y + 200, color_string)


def mountains0(gui,color_string0, color_string1):
    x = gui.mouse_x / 10
    y = gui.mouse_y / 10
    gui.triangle(x - 300, y + 750, x + 525, y + 750, x + 150, y + 275, color_string0)  # left mountain
    gui.triangle(x + 100, y+750, x+900, y + 750, x + 525, y + 275, color_string1)  # right mountain


def foreground(gui):
    x = gui.mouse_x / 5
    y = gui.mouse_y / 5 + 525
    gui.rectangle(x - 200, y, 900, 400, 'medium spring green')  # grass field
    i = -1
    while i <= 751:
        y = gui.mouse_y / 5 + 475
        gui.rectangle(i, y, 3, 50, 'forest green')  # grass blades
        i += 3 ** 2
    gui.rectangle(x + 420, y + 50, 33, 75, 'saddle brown')  # tree trunk
    gui.ellipse(x + 434,  y, 100, 150, 'dark green')  # tree top
    gui.ellipse(x + 400, y + 170, 170, 90, 'royal blue')  # pond

    ''' START BORBS '''
    x = gui.mouse_x/10 + 40
    y = gui.mouse_y/10 + 90
    x2 = gui.mouse_x/10 + 80
    y2 = gui.mouse_y/10 + 107
    i = 0
    while i < 5:
        gui.line(x, y, x2, y2, 'black', 2)
        gui.line(x2, y2, x2 + 40, y, 'black', 2)
        x = x + 100
        y = y + 20
        x2 = x2 + 100
        y2 = y2 + 20
        i += 1
    ''' END BORBS '''


def main():
    gui = graphics(700, 750, 'Parallax')

    '''  COLORS FOR MOUNTAINS  '''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    red_0 = random.randint(0, 255)
    red_1 = random.randint(0, 255)
    green_0 = random.randint(0, 255)
    green_1 = random.randint(0, 255)
    blue_0 = random.randint(0, 255)
    blue_1 = random.randint(0, 255)
    color_string0 = gui.get_color_string(red_0, green_0, blue_0)
    color_string1 = gui.get_color_string(red_1, green_1, blue_1)
    color_string = gui.get_color_string(red, green, blue)
    '''  END MOUNTAIN COLOR  '''

    while True:
        gui.clear()
        sky(gui)
        sun(gui)
        mountains(gui, color_string)
        mountains0(gui,color_string0,color_string1)
        foreground(gui)
        gui.update_frame(30)



main()
