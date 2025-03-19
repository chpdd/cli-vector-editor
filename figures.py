class Figure:

    def __repr__(self):
        return "Figure"

    @staticmethod
    def validation_converter(x, conv_type, positive_result=False):
        try:
            result = conv_type(x)
        except ValueError:
            raise ValueError(f'Argument in the place of "{x}" must be of type "{conv_type.__name__}"')
        if positive_result and result <= 0:
            raise ValueError(f'Argument in the place of "{x}" must be positive number')
        return result


class Point(Figure):
    args_n = 2

    def __init__(self, x, y):
        self._x = self.validation_converter(x, float)
        self._y = self.validation_converter(y, float)

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Line(Figure):
    args_n = 4

    def __init__(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            raise ValueError("Dots must be different")
        self._a = Point(x1, y1)
        self._b = Point(x2, y2)

    def __str__(self):
        return f'Line({self.a}, {self.b})'

    def __repr__(self):
        return f'Line({self.a.x}, {self.a.y}, {self.b.x}, {self.b.y})'

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b


class Circle(Figure):
    args_n = 3

    def __init__(self, x, y, radius):
        self._center = Point(x, y)
        self._radius = self.validation_converter(radius, float, positive_result=True)

    def __str__(self):
        return f'Circle(center={self.center}, radius={self.radius})'

    def __repr__(self):
        return f'Circle({self.center.x}, {self.center.y}, {self.radius})'

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius


class Square(Figure):
    args_n = 4

    def __init__(self, x1, y1, x2, y2):
        self._diagonal = Line(x1, y1, x2, y2)

    def __str__(self):
        return f'Square(diagonal={self.diagonal})'

    def __repr__(self):
        return f'Square({self.diagonal.a.x}, {self.diagonal.a.y}, {self.diagonal.b.x}, {self.diagonal.b.y})'

    @property
    def diagonal(self):
        return self._diagonal


class Oval(Figure):
    args_n = 5

    def __init__(self, x, y, radius_x, radius_y, angle):
        self._center = Point(x, y)
        self._radius_x = self.validation_converter(radius_x, float, positive_result=True)
        self._radius_y = self.validation_converter(radius_y, float, positive_result=True)
        self._angle = self.validation_converter(angle, float)

    def __str__(self):
        return f'Oval(center={self.center}, radius_x={self.radius_x}, radius_y={self.radius_y}, angle={self.angle})'

    def __repr__(self):
        return f'Oval({self.center.x}, {self.center.y}, {self.radius_x}, {self.radius_y}, {self.angle})'

    @property
    def radius_x(self):
        return self._radius_x

    @property
    def radius_y(self):
        return self._radius_y

    @property
    def angle(self):
        return self._angle

    @property
    def center(self):
        return self._center


class Rectangle(Figure):
    args_n = 5

    def __init__(self, x, y, length, width, angle):
        self._center = Point(x, y)
        self._length = self.validation_converter(length, float, positive_result=True)
        self._width = self.validation_converter(width, float, positive_result=True)
        self._angle = self.validation_converter(angle, float)

    def __str__(self):
        return f'Rectangle(center={self.center}, length={self.length}, width={self.width}, angle={self.angle})'

    def __repr__(self):
        return f'Rectangle({self.center.x}, {self.center.y}, {self.length}, {self.width}, {self.angle})'

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def angle(self):
        return self._angle

    @property
    def center(self):
        return self._center


class FiguresContainer:
    figures_classes_dict = {"point": Point, "line": Line, "circle": Circle, "square": Square, "oval": Oval,
                            "rectangle": Rectangle}

    def __init__(self, figures=None):
        if figures is not None:
            for figure in figures:
                if not isinstance(figure, Figure):
                    raise TypeError("FiguresContainer accepts only children of the Figure class")
        else:
            figures = []
        self._figures = figures

    def __str__(self):
        return f"FiguresContainer(figures={self._figures})"

    @classmethod
    def parse_object(cls, line):
        try:
            cls_end_index = line.find("(")
            figure_cls_name = line[:cls_end_index].strip().lower()
            figure_cls = cls.figures_classes_dict[figure_cls_name.lower()]
            args = map(lambda symb: symb.strip(), line[cls_end_index + 1:line.rfind(")")].split(","))
            return figure_cls(*args)
        except Exception:
            raise ValueError(f'The line "{line}" is incorrect')

    def append(self, elem):
        if not isinstance(elem, Figure):
            raise ValueError("FiguresContainer accepts only children of the Figure class")
        self._figures.append(elem)

    def create(self, *args):
        """
        Creates figures using arguments.
        :param: figure_type and special figure parameters
        :example: create square 1 2 3 4

        Types of figures and args:
        Point - 2 coordinates
        Line - 2 points(4 coordinates)
        Circle - center point(2 coordinates) and radius,
        Square - diagonal(4 coordinates)
        Oval - center point(2 coordinates), radius_x, radius_y and angle
        Rectangle - center point(2 coordinates), length, width and angle

        """
        if len(args) < 1:
            raise ValueError("This command should have minimum 3 arguments")

        figure_type = args[0].lower()
        args = args[1:]
        if figure_type not in self.figures_classes_dict.keys():
            raise ValueError("Unknown figure type")

        figure_class = self.figures_classes_dict[figure_type]
        if len(args) != figure_class.args_n:
            raise ValueError(f'"create {figure_type}" needs {figure_class.args_n} parameters')

        figure = figure_class(*args)
        self.append(figure)
        return f"{figure} created"

    def delete(self, *args):
        """
        Deletes a figure by key
        :param: key
        :example: delete 1
        """
        if len(args) != 1:
            raise ValueError("This command should have 1 argument")

        key = Figure.validation_converter(args[0], int)
        if key >= len(self._figures):
            raise TypeError('The key must be in the range of valid indexes')

        figure = self._figures.pop(int(key))
        return f"{figure} deleted"

    def list_figures(self, *args):
        """
        Outputs a list of all figures with their indexes
        :param: No params
        :example: list
        """
        if len(args) != 0:
            raise ValueError("This command should have 0 arguments")

        if not self._figures:
            return "No figures"
        result = "List of figures:"
        for i in range(len(self._figures)):
            result += f"\n{i}) {self._figures[i]}"
        return result

    def save_in_file(self, *args):
        """
        Saves a list of all figures to “figures_save.txt” or to a specified file
        :param: file_name
        :example: save save_2.txt
        """
        if len(args) > 1:
            raise ValueError("This command should have maximum 1 argument")
        if not self._figures:
            return "No figures to save"
        file_name = args[0] if args else "figures_save.txt"
        with open(file_name, "w", encoding="UTF-8") as file:
            for figure in self._figures:
                file.write(f"{figure.__repr__()}\n")
        return f'The figures are saved in file "{file_name}"'

    def load_from_file(self, *args):
        """
        Loads all figures from the “figures_save.txt” file or from the specified file
        :param: file_name
        :example: load save_2.txt
        """
        if len(args) > 1:
            raise ValueError("This command should have maximum 1 argument")

        file_name = args[0] if args else "figures_save.txt"
        try:
            with open(file_name, "r", encoding="UTF-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f'File "{file_name}" not found')

        for line in lines:
            try:
                figure = self.parse_object(line.strip())
                self.append(figure)
                print(f'Figure "{figure}" loaded')
            except ValueError as e:
                print(e)
        return f'The figures are loaded from file "{file_name}"'
