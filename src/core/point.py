class Point:
    '''
    A Point class to represent a point in 2D space.
    '''

    def __init__(self, x: float, y: float):
        '''
        Initialize a point instance.

        Args:
            x (float): The x-coordinates of the point.
            y (float): The y-coordinates of the point.
        '''
        self.x = x
        self.y = y

    def __add__(self, other: 'Point') -> 'Point':
        '''
        Adds two Point instances component-wise.

        Args:
            other (Point): The other point to add.

        Returns:
            Point: A new Point instance with summed coordinates.
        '''

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        '''
        Subtracts one Point instance from another component-wise.

        Args:
            other (Point): The other point to subtract.

        Returns:
            Point: A new Point instance with the difference of coordinates.
        '''

        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Point | float') -> 'Point':
        '''
        Multiplies a Point instance by either a scalar or another Point.

        Args:
            other (Point | float): The scalar value or another Point.

        Returns:
            Point: A new Point instance with multiplied coordinates.

        Raises:
            TypeError: If the operand is not a float or Point.
        '''

        if isinstance(other, (int, float)):  # Scalar multiplication
            return Point(self.x * other, self.y * other)
        elif isinstance(other, Point):  # Element-wise multiplication
            return Point(self.x * other.x, self.y * other.y)
        else:
            raise TypeError(f'Unsupported operand type(s) for *: "Point" and "{type(other).__name__}"')
    
    def __truediv__(self, other: 'Point') -> 'Point':
        '''
        Divides a Point instance by either a scalar or another Point element-wise.

        Args:
            other (Point | float): The scalar value or another Point.

        Returns:
            Point: A new Point instance with divided coordinates.

        Raises:
            ZeroDivisionError: If dividing by zero.
            TypeError: If the operand is not a float or Point.
        '''

        if isinstance(other, (int, float)):  # Scalar division
            if other == 0:
                raise ZeroDivisionError('Cannot divide by zero.')
            return Point(self.x / other, self.y / other)
        elif isinstance(other, Point):  # Element-wise division
            if other.x == 0 or other.y == 0:
                raise ZeroDivisionError('Cannot divide by a Point with zero components.')
            return Point(self.x / other.x, self.y / other.y)
        else:
            raise TypeError(f'Unsupported operand type(s) for /: "Point" and "{type(other).__name__}"')

    def __repr__(self) -> str:
        '''
        Returns a string representation of the Point instance for debugging.

        Returns:
            str: A string representation in the format "Point(x, y)".
        '''

        return f'Point({self.x}, {self.y})'

    def __str__(self) -> str:
        '''
        Returns a user-friendly string representation of the Point instance.

        Returns:
            str: A formatted string representing the point coordinates.
        '''

        return f'({self.x}, {self.y})'

    def clone(self) -> 'Point':
        '''
        Creates and returns a new Point instance with the same coordinates.

        Returns:
            Point: A new instance with the same x and y values.
        '''

        return Point(self.x, self.y)