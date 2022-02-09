import random
from tkinter import (
    ttk, Tk, StringVar, Frame, Label, Button, Canvas
)

from algorithms.sorting import SortingAlgorithm
from colors import WHITE, LIGHT_GRAY, BLUE


class SortingVisualizerFramework:

    SPEED_LIST = ["Fast", "Medium", "Slow"]

    windowWidth = 1000
    windowHeight = 700

    frameWidth = 900
    frameHeight = 300

    canvasWidth = 800
    canvasHeight = 400
    canvasOffset = 4
    canvasSpacing = 2

    def __init__(self, algorithm_list):
        """
        The creation order in the constructor is of paramount importance.
        """
        self.algorithm_list = algorithm_list
        self.data = []
        self.window = self._setup_window()

        self.algorithm_name = StringVar()
        self.speed_value = StringVar()

        self.frame = self._setup_ui_frame()
        self.canvas = self._setup_canvas()

        self.speed_menu = self._setup_speed_dropdown()
        self.algo_menu = self._setup_algorithm_dropdown()

        self._sort_button()
        self._generate_button()

    def _setup_window(self):
        window = Tk()
        window.title("Sorting Visualizer")
        window.maxsize(self.windowWidth, self.windowHeight)
        window.config(bg=WHITE)
        return window

    def _setup_ui_frame(self):
        ui_frame = Frame(self.window, width=self.frameWidth, height=self.frameHeight, bg=WHITE)
        ui_frame.grid(row=0, column=0, padx=10, pady=5)
        return ui_frame

    def _setup_algorithm_dropdown(self):
        l1 = Label(self.frame, text="Algorithm: ", bg=WHITE)
        l1.grid(row=0, column=0, padx=10, pady=5, sticky="W")

        algo_menu = ttk.Combobox(self.frame, textvariable=self.algorithm_name, values=list(self.algorithm_list.keys()))
        algo_menu.grid(row=0, column=1, padx=5, pady=5)
        algo_menu.current(0)
        return algo_menu

    def _setup_speed_dropdown(self):
        l2 = Label(self.frame, text="Sorting Speed: ", bg=WHITE)
        l2.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        speed_menu = ttk.Combobox(self.frame, textvariable=self.speed_value, values=self.SPEED_LIST)
        speed_menu.grid(row=1, column=1, padx=5, pady=5)
        speed_menu.current(0)
        return speed_menu

    def _sort_button(self):
        b1 = Button(self.frame, text="Sort", command=self.sort, bg=LIGHT_GRAY)
        b1.grid(row=2, column=1, padx=5, pady=5)

    def _generate_button(self):
        b2 = Button(self.frame, text="Generate Array", command=self.generate, bg=LIGHT_GRAY)
        b2.grid(row=2, column=0, padx=5, pady=5)

    def _setup_canvas(self):
        canvas = Canvas(self.window, width=self.canvasWidth, height=self.canvasHeight, bg=WHITE)
        canvas.grid(row=1, column=0, padx=10, pady=5)
        return canvas

    def drawData(self, data, colorArray):
        self.canvas.destroy()
        self.canvas = self._setup_canvas()

        x_width = self.canvasWidth / (len(data) + 1)
        normalizedData = [i / max(data) for i in data]

        for index, height in enumerate(normalizedData):
            x0 = index * x_width + self.canvasOffset + self.canvasSpacing
            y0 = self.canvasHeight - height * 390
            x1 = (index + 1) * x_width + self.canvasOffset
            y1 = self.canvasHeight
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[index])

        self.window.update_idletasks()

    def generate(self):
        self.data = []
        for i in range(0, 100):
            random_value = random.randint(1, 150)
            self.data.append(random_value)

        self.drawData(self.data, [BLUE for x in range(len(self.data))])

    def set_speed(self):
        speed = self.speed_menu.get()
        match speed:
            case "Slow":
                return 0.3
            case "Medium":
                return 0.1
            case "Fast":
                return 0.001
            case _:
                pass

    def sort(self):
        algorithm = SortingAlgorithm(self.algorithm_list[self.algo_menu.get()])
        algorithm.sort(self.data, self.set_speed(), self)

    def start(self):
        self.window.mainloop()
