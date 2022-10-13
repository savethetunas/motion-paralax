from graphics import graphics
import random


def sky(gui):
    gui.rectangle(0, 0, 700, 750, 'PowderBlue')  # Sky


def night(gui):
    gui.rectangle(0, 0, 700, 750, 'midnightblue')  # Night sky


def sun(gui):
    x = gui.mouse_x / 50 + 600
    y = gui.mouse_y / 50 + 150
    gui.ellipse(x - 50, y - 50, 100, 100, 'yellow')


def moon(gui):
    x = gui.mouse_x / 25 + 167
    y = gui.mouse_y / 25 + 250
    gui.ellipse(x - 50, y - 50, 100, 100, 'linen')


def mountains(gui, color_string):
    x = gui.mouse_x / 15
    y = gui.mouse_y / 15
    gui.triangle(x, y + 750, x + 700, y + 750, x + 350, y + 200, color_string)


def mountains0(gui,color_string0, color_string1):
    x = gui.mouse_x / 10
    y = gui.mouse_y / 10
    gui.triangle(x - 300, y + 750, x + 525, y + 750, x + 150, y + 275, color_string0)  # left mountain
    gui.triangle(x + 100, y+750, x+900, y + 750, x + 525, y + 275, color_string1)  # right mountain


def night_mountains(gui, n_color_string):
    ''' START STARS '''
    gui.ellipse(10 + gui.mouse_x/100, 210 + gui.mouse_y/100, random.randint(0,7), random.randint(0,2), 'white')
    gui.ellipse(110+ gui.mouse_x/100, 350+ gui.mouse_y/100, random.randint(0,3), random.randint(0,2), 'white')
    gui.ellipse(210+ gui.mouse_x/100, 50+ gui.mouse_y/100, random.randint(0,1), random.randint(0,3), 'white')
    gui.ellipse(430+ gui.mouse_x/100, 250+ gui.mouse_y/100, random.randint(0,5), random.randint(0,4), 'white')
    gui.ellipse(530+ gui.mouse_x/100, 350+ gui.mouse_y/100, random.randint(0,6), random.randint(0,1), 'white')
    gui.ellipse(650+ gui.mouse_x/100, 220+ gui.mouse_y/100, random.randint(0,4), random.randint(0,2), 'white')
    gui.ellipse(698+ gui.mouse_x/100, 509+ gui.mouse_y/100, random.randint(0,3), random.randint(0,4), 'white')
    gui.ellipse(635+ gui.mouse_x/100, 42+ gui.mouse_y/100, random.randint(0,7), random.randint(0,4), 'white')
    gui.ellipse(305+ gui.mouse_x/100, 410+ gui.mouse_y/100, random.randint(0,6), random.randint(0,3), 'white')
    gui.ellipse(250+ gui.mouse_x/100, 220+ gui.mouse_y/100, random.randint(0,1), random.randint(0,2), 'white')
    gui.ellipse(4100+ gui.mouse_x/100, 450+ gui.mouse_y/100, random.randint(0,5), random.randint(0,1), 'white')
    gui.ellipse(50+ gui.mouse_x/100, 450+ gui.mouse_y/100, random.randint(0,7), random.randint(0,3), 'white')
    gui.ellipse(450+ gui.mouse_x/100, 80+ gui.mouse_y/100, random.randint(0,3), random.randint(0,4), 'white')
    gui.ellipse(30+ gui.mouse_x/100, 100+ gui.mouse_y/100, random.randint(0,7), random.randint(0,4), 'white')
    ''' END STARS '''
    x = gui.mouse_x / 15
    y = gui.mouse_y / 15
    gui.triangle(x, y + 750, x + 700, y + 750, x + 350, y + 200, n_color_string)


def night_mountains0(gui,n_color_string0, n_color_string1):
    x = gui.mouse_x / 10
    y = gui.mouse_y / 10
    gui.triangle(x - 300, y + 750, x + 525, y + 750, x + 150, y + 275, n_color_string0)  # left mountain
    gui.triangle(x + 100, y+750, x+900, y + 750, x + 525, y + 275, n_color_string1)  # right mountain


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
    gui.ellipse(x + 434,  y, 100, 150, 'chartreuse3')  # tree top
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


def night_foreground(gui):
    x = gui.mouse_x / 5
    y = gui.mouse_y / 5 + 525
    gui.rectangle(x - 200, y, 900, 400, 'palegreen4')  # grass field
    i = -1
    while i <= 751:
        y = gui.mouse_y / 5 + 475
        gui.rectangle(i, y, 3, 50, 'palegreen4')  # grass blades
        i += 3 ** 2
    gui.rectangle(x + 420, y + 50, 33, 75, 'firebrick4')  # tree trunk
    gui.ellipse(x + 434,  y, 100, 150, 'darkgreen')  # tree top
    gui.ellipse(x + 400, y + 170, 170, 90, 'navy')  # pond


    ''' START STARS '''

    ''' END STARS '''





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


    '''NIGHT MOUNTAIN COLOUR'''
    n_red = random.randint(0, 50)
    n_green = random.randint(0, 50)
    n_blue = random.randint(0, 50)
    n_red_0 = random.randint(0, 50)
    n_red_1 = random.randint(0, 50)
    n_green_0 = random.randint(0, 50)
    n_green_1 = random.randint(0, 50)
    n_blue_0 = random.randint(0, 50)
    n_blue_1 = random.randint(0, 50)
    n_color_string0 = gui.get_color_string(n_red_0, n_green_0, n_blue_0)
    n_color_string1 = gui.get_color_string(n_red_1, n_green_1, n_blue_1)
    n_color_string = gui.get_color_string(n_red, n_green, n_blue)

    while True:
        gui.clear()
        while gui.mouse_y <= 250:
            sky(gui)
            sun(gui)
            mountains(gui, color_string)
            mountains0(gui,color_string0,color_string1)
            foreground(gui)
            gui.update_frame(30)
        while gui.mouse_y > 250:
            night(gui)
            moon(gui)
            night_mountains(gui, n_color_string)
            night_mountains0(gui,n_color_string0,n_color_string1)
            night_foreground(gui)
            gui.update_frame(30)



main()
