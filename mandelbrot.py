import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """
    Gets the escape time for a complex number c, by calculating what c will be for each iteration of the mandelbrot set formula.
    If the number of iterations exceeds max_iterations without escaping, None is returned.
    If the magnitude is greater than two, the total calls are reported as the escape time.

    :param c: complex number to use in the Mandelbrot set
    :param max_iterations: int value to limit the number of iterations checked

    :return: int of the number of iterations to escape the set | None if it never escapes in the max limit of iterations
    """

    caylee = c
    total_call = 0
    if abs(c) > 2:
        return 0
    else:
        while max_iterations > 0:
            if abs(caylee) > 2:
                return total_call
            else:
                max_iterations -= 1
                total_call += 1
                caylee = (caylee) ** 2 + c   
        return None



def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    """
    Generate a 2D NumPy array of complex numbers forming a grid from top_left to bottom_right.
    The real part increases by step along columns, and the imaginary part decreases by step along rows.

    :param top_left: complex number for the top left value of the grid
    :param bottom_right: complex number for the (excluded) bottom right value of the grid
    :param step: float distance between columns and rows

    :return: ndarray representing the complex grid created
    """
    # Generate real and imaginary parts
    real_values = np.arange(top_left.real, bottom_right.real, step)
    imag_values = np.arange(top_left.imag, bottom_right.imag, -step)  # Decreasing order

    # Create a grid using broadcasting
    real_grid, imag_grid = np.meshgrid(real_values, imag_values)

    return real_grid + 1j * imag_grid




def get_escape_time_color_arr(
        c_arr: np.ndarray,
        max_iterations: int
) -> np.ndarray:
    """
    Draws the Mandelbrot set based on the escape times of each point by assigning it a color-associated value: 0 (black), 1 (white), or something 0 < x < 1 (various grey).
    
    :param c_arr: ndarray of complex numbers
    :param max_iterations: int for the number of iterations before stopping
    
    :return: ndarray of color values
    """
    # Create an empty grid with the same shape as the inputted complex grid.
    color_grid = np.empty(c_arr.shape)

    # Obtain the escape time of each point in the grid and assign it a value from 0 to 1 based on escape times.
    for index, c in np.ndenumerate(c_arr):
        escape_time = get_escape_time(c, max_iterations)
        
        if escape_time is None:
            escape_time = max_iterations + 1
            
        color_grid[index] = (max_iterations - escape_time + 1) / (max_iterations + 1)

    return color_grid



def get_julia_color_arr(
        complex_arr: np.ndarray,
        c: complex,
        max_iterations: int
) -> np.ndarray:
    """
    Returns a grid with escape times, converted to colors based on the 'speed' of their escape.
    """
    colored_grid = np.empty(complex_arr.shape)
    for ind,z in np.ndenumerate(complex_arr):
        counter = 0
        z_val = z
        while abs(z_val) <=2 and counter < max_iterations:
            z_val = z_val**2 +c
            counter+=1
        if count<max_iterations:
            colored_grid[ind] = (max_iterations - count +1)/(max_iterations+1)
        else:
            colored_grid[index] = 0
    return colored_grid
