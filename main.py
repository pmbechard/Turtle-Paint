import turtle


class Paint:
    def __init__(self):
        self.screen = turtle.Screen()
        turtle.title("Turtle Painting")
        self.screen.cv._rootwindow.resizable(False, False)

        # Directions
        self.screen.onkeypress(self.go_up, 'Up')
        self.screen.onkeypress(self.go_down, 'Down')
        self.screen.onkeypress(self.go_left, 'Left')
        self.screen.onkeypress(self.go_right, 'Right')

        # Clear and Exit
        self.screen.onkeypress(self.clear_screen, 'space')
        self.screen.onkeypress(self.quit_app, 'q')
        self.screen.onkeypress(self.quit_app, 'Escape')

        # Width
        self.screen.onkeypress(self.increase_width, '.')
        self.screen.onkeypress(self.decrease_width, ',')

        # Color
        self.colors = ['black', 'blue', 'green', 'red', 'yellow', 'orange', 'pink', 'purple']
        self.screen.onkeypress(self.change_color, 'c')

        # Pen up/down
        self.pen_down = True
        self.screen.onkeypress(self.pen_up_down, '/')

        # MENU:
        # Colors
        self.color = f'Color (c): {self.colors[0]}'
        self.color_pen = turtle.Pen(visible=False)
        self.color_pen.penup()
        self.color_pen.setpos(-300, -300)
        self.color_pen.write(self.color)

        # Width
        self.width = f'Width (, or .): {turtle.width()}'
        self.width_pen = turtle.Pen(visible=False)
        self.width_pen.penup()
        self.width_pen.setpos(-200, -300)
        self.width_pen.write(self.width)

        # Pen up/down
        self.pen_pen = turtle.Pen(visible=False)
        self.pen_pen.penup()
        self.pen_pen.setpos(-100, -300)
        self.pen_pen.write("Pen (/): down")

        # Clear screen and Exit
        self.clear_exit_pen = turtle.Pen(visible=False)
        self.clear_exit_pen.penup()
        self.clear_exit_pen.setpos(175, -300)
        self.clear_exit_pen.write("Use arrow keys to move.\nPress space to clear screen.\nPress q or Esc to exit.")

        self.screen.listen()
        self.screen.mainloop()

    def go_up(self):
        current_y_pos = turtle.pos()[1]
        new_y_pos = current_y_pos + 3
        turtle.sety(new_y_pos)

    def go_down(self):
        current_y_pos = turtle.pos()[1]
        new_y_pos = current_y_pos - 3
        turtle.sety(new_y_pos)

    def go_left(self):
        current_x_pos = turtle.pos()[0]
        new_x_pos = current_x_pos - 3
        turtle.setx(new_x_pos)

    def go_right(self):
        current_x_pos = turtle.pos()[0]
        new_x_pos = current_x_pos + 3
        turtle.setx(new_x_pos)

    def clear_screen(self):
        turtle.clear()

    def quit_app(self):
        turtle.bye()

    def increase_width(self):
        current_width = turtle.width()
        new_width = current_width + 1
        turtle.width(new_width)

        self.width = f'Width (, or .): {turtle.width()}'
        self.width_pen.clear()
        self.width_pen.write(self.width)

    def decrease_width(self):
        if turtle.width() != 1:
            current_width = turtle.width()
            new_width = current_width - 1
            turtle.width(new_width)

        self.width = f'Width (, or .): {turtle.width()}'
        self.width_pen.clear()
        self.width_pen.write(self.width)

    def change_color(self):
        current_index = self.colors.index(turtle.color()[0])
        new_index = current_index + 1
        if new_index >= len(self.colors):
            new_index = 0
        turtle.color(self.colors[new_index])
        self.color = f'Color (c): {self.colors[new_index]}'
        self.color_pen.clear()
        self.color_pen.write(self.color)

    def pen_up_down(self):
        if self.pen_down:
            turtle.penup()
            self.pen_down = False
            self.pen_pen.clear()
            self.pen_pen.write("Pen (/): up")
        else:
            turtle.pendown()
            self.pen_down = True
            self.pen_pen.clear()
            self.pen_pen.write("Pen (/): down")


if __name__ == '__main__':
    Paint()
