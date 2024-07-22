# This is a snake game

# define variable as global variable
global tkinter
global random

import tkinter
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tkinter.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.restart_button = tkinter.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.init_game()
        self.root.bind("<KeyPress>", self.change_direction)
        self.root.mainloop()

    def init_game(self):
        self.snake = [(20, 20), (30, 20), (40, 20)]
        self.snake_dir = "Right"
        self.food = self.create_food()
        self.game_over = False
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.snake_dir = event.keysym

    def move_snake(self):
        head_x, head_y = self.snake[-1]

        if self.snake_dir == "Up":
            new_head = (head_x, head_y - 10)
        elif self.snake_dir == "Down":
            new_head = (head_x, head_y + 10)
        elif self.snake_dir == "Left":
            new_head = (head_x - 10, head_y)
        else:  # self.snake_dir == "Right"
            new_head = (head_x + 10, head_y)

        if (
            new_head[0] < 0 or new_head[0] >= 400 or
            new_head[1] < 0 or new_head[1] >= 400 or
            new_head in self.snake
        ):
            self.game_over = True
        else:
            self.snake.append(new_head)
            if new_head == self.food:
                self.food = self.create_food()
            else:
                self.snake.pop(0)

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.canvas.delete("all")
            for segment in self.snake:
                self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green")
            self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red")
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(200, 200, text="GAME OVER", fill="white", font=("Helvetica", 24))

    def restart_game(self):
        self.canvas.delete("all")
        self.init_game()


root = tkinter.Tk()
game = SnakeGame(root)

