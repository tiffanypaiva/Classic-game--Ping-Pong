import collections
import math
import os


def floor(Value, Size, Offset=200):

    return float(((Value + Offset) // Size) * Size - Offset)


def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath




def square(X_Axis, Y_Axis, Size, name):

    import turtle
    turtle.up()
    turtle.goto(X_Axis, Y_Axis)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(Size)
        turtle.left(90)

    turtle.end_fill()
def line(a, b, X_Axis, Y_Axis):
    import turtle
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(X_Axis, Y_Axis)


class vector(collections.Sequence):

    PRECISION = 6

    __slots__ = ('_X_Axis', '_Y_Axis', '_hash')

    def __init__(Self, X_Axis, Y_Axis):

        Self._hash = None
        Self._X_Axis = round(X_Axis, Self.PRECISION)
        Self._Y_Axis = round(Y_Axis, Self.PRECISION)

    @property
    def X_Axis(Self):

        return Self._X_Axis

    @X_Axis.setter
    def X_Axis(Self, Value):
        if Self._hash is not None:
            raise ValueError('set X_Axis cannot be set after hashing')
        Self._X_Axis = round(Value, Self.PRECISION)

    @property
    def Y_Axis(Self):

        return Self._Y_Axis

    @Y_Axis.setter
    def Y_Axis(Self, Value):
        if Self._hash is not None:
            raise ValueError(' set y cannot be set after hashing')
        Self._Y_Axis = round(Value, Self.PRECISION)

    def __hash__(Self):

        if Self._hash is None:
            pair = (Self.X_Axis, Self.Y_Axis)
            Self._hash = hash(pair)
        return Self._hash

    def __len__(Self):

        return 2

    def __getitem__(Self, indeX_Axis):

        if indeX_Axis == 0:
            return Self.X_Axis
        if indeX_Axis == 1:
            return Self.Y_Axis
        raise IndeX_AxisError

    def copy(Self):

        type_Self = type(Self)
        return type_Self(Self.X_Axis, Self.Y_Axis)

    def __eq__(Self, other):

        if isinstance(other, vector):
            return Self.X_Axis == other.X_Axis and Self.Y_Axis == other.Y_Axis
        return NotImplemented

    def __ne__(Self, other):

        if isinstance(other, vector):
            return Self.X_Axis != other.X_Axis or Self.Y_Axis != other.Y_Axis
        return NotImplemented

    def __iadd__(Self, other):

        if Self._hash is not None:
            raise ValueError('addition of vector cannot after hashing')
        elif isinstance(other, vector):
            Self.X_Axis += other.X_Axis
            Self.Y_Axis += other.Y_Axis
        else:
            Self.X_Axis += other
            Self.Y_Axis += other
        return Self

    def __add__(Self, other):

        copy = Self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(Self, other):

        Self.__iadd__(other)

    def __isub__(Self, other):

        if Self._hash is not None:
            raise ValueError('subtraction of  vector cannot  happen after hashing')
        elif isinstance(other, vector):
            Self.X_Axis -= other.X_Axis
            Self.Y_Axis -= other.Y_Axis
        else:
            Self.X_Axis -= other
            Self.Y_Axis -= other
        return Self

    def __sub__(Self, other):

        copy = Self.copy()
        return copy.__isub__(other)

    def __imul__(Self, other):

        if Self._hash is not None:
            raise ValueError(' multiplication of vector cannot happen  after hashing')
        elif isinstance(other, vector):
            Self.X_Axis *= other.X_Axis
            Self.Y_Axis *= other.Y_Axis
        else:
            Self.X_Axis *= other
            Self.Y_Axis *= other
        return Self

    def __mul__(Self, other):

        copy = Self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(Self, other):

        Self.__imul__(other)

    def __itruediv__(Self, other):

        if Self._hash is not None:
            raise ValueError(' division of  vector cannot happen after hashing')
        elif isinstance(other, vector):
            Self.X_Axis /= other.X_Axis
            Self.Y_Axis /= other.Y_Axis
        else:
            Self.X_Axis /= other
            Self.Y_Axis /= other
        return Self

    def __truediv__(Self, other):

        copy = Self.copy()
        return copy.__itruediv__(other)

    def __neg__(Self):

        copy = Self.copy()
        copy.X_Axis = -copy.X_Axis
        copy.Y_Axis = -copy.Y_Axis
        return copy

    def __abs__(Self):

        return (Self.X_Axis ** 2 + Self.Y_Axis ** 2) ** 0.5



    def __repr__(Self):

        type_Self = type(Self)
        name = type_Self.__name__
        return '{}({!r}, {!r})'.format(name, Self.X_Axis, Self.y)
