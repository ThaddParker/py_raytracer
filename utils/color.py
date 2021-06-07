import numpy as np
import numbers

from utils.vector import Vector


class Color:
    """An rbg color that comprises of floating point 0 to 1 values per component"""

    def __init__(self, r=0., g=0., b=0.):
        """ """
        self.red = r
        self.green = g
        self.blue = b

    def __str__(self):
        # Used for debugging. This method is called when you print an instance  
        return "(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"

    def __repr__(self):
        return f"Color ({self.red!r},{self.green!r},{self.blue!r})"

    def __setitem__(self, key, value):
        if isinstance(key, int) and (isinstance(value, int) or isinstance(value, numbers.Number)):
            if key == 0:
                self.red = value
            elif key == 1:
                self.green = value
            elif key == 2:
                self.blue = value
        elif isinstance(key, str) and (isinstance(value, int) or isinstance(value, numbers.Number)):
            if key == 'red':
                self.red = value
            elif key == 'green':
                self.green = value
            elif key == 'blue':
                self.blue = value
        else:
            raise ValueError(f"The key: {key} and value: {value} is invalid. Either use an integer or string for the key and use float value for the value field")

    def __getitem__(self, item):
        if isinstance(item, int):
            if item == 0:
                return self.red
            elif item == 1:
                return self.green
            elif item == 2:
                return self.blue
            else:
                raise IndexError(f"The provided index: {item} is invalid. Please provide [0, 1, 2] only")
        elif isinstance(item, str):
            if item == 'red':
                return self.red
            elif item == 'green':
                return self.green
            elif item == 'blue':
                return self.blue
            raise IndexError(f"The provided index name: {item} is invalid. Please provide either 'red','green','blue'")

    def __add__(self, v):
        if isinstance(v, Color):
            return Color(self.red + v.red, self.green + v.green, self.blue + v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red + v, self.green + v, self.blue + v)
        elif isinstance(v, np.ndarray):
            return Color(v[0] + self.red, v[1]+self.green, v[2] + self.blue)
        elif isinstance(v, Vector):
            return Color(v[0] + self.red, v[1]+self.green, v[2] + self.blue)

    def __radd__(self, v):
        if isinstance(v, Color):
            return Color(self.red + v.red, self.green + v.green, self.blue + v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red + v, self.green + v, self.blue + v)
        elif isinstance(v, np.ndarray):
            return Color(v[0] + self.red, v[1]+self.green, v[2] + self.blue)
        elif isinstance(v, Vector):
            return Color(v[0] + self.red, v[1]+self.green, v[2] + self.blue)

    def __sub__(self, v):
        if isinstance(v, Color):
            return Color(self.red - v.red, self.green - v.green, self.blue - v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red - v, self.green - v, self.blue - v)
        elif isinstance(v, np.ndarray):
            return Color(self.red - v[0], self.green - v[1], self.blue - v[2])
        elif isinstance(v, Vector):
            return Color(self.red - v[0], self.green - v[1], self.blue - v[2])

    def __rsub__(self, v):
        if isinstance(v, Color):
            return Color(self.red - v.red, self.green - v.green, self.blue - v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red - v, self.green - v, self.blue - v)
        elif isinstance(v, np.ndarray):
            return Color(self.red - v[0], self.green - v[1], self.blue - v[2])
        elif isinstance(v, Vector):
            return Color(self.red - v[0], self.green - v[1], self.blue - v[2])

    def __mul__(self, v):
        if isinstance(v, Color):
            return Color(self.red * v.red, self.green * v.green, self.blue * v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red * v, self.green * v, self.blue * v)
        elif isinstance(v, np.ndarray):
            return Color(self.red * v[0], self.green * v[1], self.blue * v[2])
        elif isinstance(v, Vector):
            return Color(self.red * v[0], self.green * v[1], self.blue * v[2])
         
    def __rmul__(self, v):
        if isinstance(v, Color):
            return Color(self.red * v.red, self.green * v.green, self.blue * v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red * v, self.green * v, self.blue * v)
        elif isinstance(v, np.ndarray):
            return Color(self.red * v[0], self.green * v[1], self.blue * v[2])
        elif isinstance(v, Vector):
            return Color(self.red * v[0], self.green * v[1], self.blue * v[2])

    def __truediv__(self, v):
        if isinstance(v, Color):
            return Color(self.red / v.red, self.green / v.green, self.blue / v.blue)
        elif isinstance(v, numbers.Number):
            return Color(self.red / v, self.green / v, self.blue / v)
        elif isinstance(v, np.ndarray):
            return Color(self.red / v[0], self.green / v[1], self.blue / v[2])
        elif isinstance(v, Vector):
            return Color(self.red / v[0], self.green / v[1], self.blue / v[2])

    def __rtruediv__(self, v):
        if isinstance(v, Color):
            return Color(v.red / self.red, v.green / self.green, v.blue / self.blue)
        elif isinstance(v, numbers.Number): 
            return Color(self.red / v, self.green / v, self.blue / v)
        elif isinstance(v, np.ndarray):
            return Color(self.red /v[0], self.green / v[1], self.blue / v[2])
        elif isinstance(v, Vector):
            return Color(self.red / v[0], self.green / v[1], self.blue / v[2])

    def __abs__(self):
        return Color(np.abs(self.red), np.abs(self.green), np.abs(self.blue))

    def __pow__(self, a):
        return Color(self.red ** a, self.green ** a, self.blue ** a)

    def to_array(self):
        return np.array([self.red, self.green, self.blue])

    def components(self):
        return self.red, self.green, self.blue

    @staticmethod
    def where(cond, out_true, out_false):
        return Color(np.where(cond, out_true.red, out_false.red),
                     np.where(cond, out_true.green, out_false.green),
                     np.where(cond, out_true.blue, out_false.blue))

    @staticmethod
    def select(mask_list, out_list):
        out_list_x = [i.x for i in out_list]
        out_list_y = [i.y for i in out_list]
        out_list_z = [i.z for i in out_list]

        return Color(np.select(mask_list, out_list_x),
                     np.select(mask_list, out_list_y),
                     np.select(mask_list, out_list_z))

    def clip(self, _min_, _max_):
        return Color(np.clip(self.red, _min_, _max_),
                     np.clip(self.green, _min_, _max_),
                     np.clip(self.blue, _min_, _max_))

    def place(self, cond):
        r = Color(np.zeros(cond.shape), np.zeros(cond.shape), np.zeros(cond.shape))
        np.place(r.red, cond, self.red)
        np.place(r.green, cond, self.green)
        np.place(r.blue, cond, self.blue)
        return r

    def mean(self, axis):
        return Color(np.mean(self.red, axis=axis), np.mean(self.green, axis=axis), np.mean(self.blue, axis=axis))

    def __eq__(self, other):
        return (self.red == other.x) & (self.green == other.y) & (self.blue == other.z)

    @staticmethod
    def array_to_color(array):
        return Color(array[0], array[1], array[2])

    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        return cls(x, y, z)

    def to_ppm_color(self):
        return Color()


class Colors:
    Black = Color(0., 0., 0.)
    White = Color(1., 1., 1.)
    Red = Color(1., 0., 0.)
    Green = Color(0., 1., 0.)
    Blue = Color(0., 0., 1.)
