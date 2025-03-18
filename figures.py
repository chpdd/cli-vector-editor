class Figure:

    def __repr__(self):
        return "Figure"

    @staticmethod
    def custom_float(x):
        try:
            return float(x)
        except ValueError:
            raise ValueError(f'Argument with value="{x}" must be a number')


class Point(Figure):
    args_n = 2

    def __init__(self, x, y):
        self._x = self.custom_float(x)
        self._y = self.custom_float(y)

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

    def __repr__(self):
        return f'Line({self.a}, {self.b})'

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b


class Circle(Figure):
    args_n = 3

    def __init__(self, x, y, radius):
        self._radius = self.custom_float(radius)
        if self.radius <= 0:
            raise ValueError("Radius must be positive number")
        self._center = Point(x, y)

    def __repr__(self):
        return f'Circle(center={self.center}, radius={self.radius})'

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

    def __repr__(self):
        return f'Square(diagonal={self.diagonal})'

    @property
    def diagonal(self):
        return self._diagonal


class FiguresContainer:
    figures_classes_dict = {"point": Point, "line": Line, "circle": Circle, "square": Square}

    def __init__(self, figures=None):
        if figures is not None:
            for figure in figures:
                if not isinstance(figure, Figure):
                    raise TypeError("FiguresContainer accepts only children of the Figure class")
        else:
            figures = []
        self._figures = figures

    def __repr__(self):
        return f"FiguresContainer(figures={self._figures})"

    def create(self, *args):
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
        self._figures.append(figure)
        return f"{figure} created"

    def delete(self, *args):
        if len(args) != 1:
            raise ValueError("This command should have 1 argument")

        key = args[0]
        if not key.isdigit():
            raise TypeError("The key must be of type int")

        key = int(key)
        if key >= len(self._figures):
            raise ValueError("Key outside the range of acceptable values")

        figure = self._figures.pop(key)
        return f"{figure} deleted"

    def list_figures(self, *args):
        if len(args) != 0:
            raise ValueError("This command should have 0 arguments")

        if not self._figures:
            return "No figures"
        result = "List of figures:"
        for i in range(len(self._figures)):
            result += f"\n{i}) {self._figures[i]}"
        return result
