import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    ...



def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    """
        Generate a 2D NumPy array of complex numbers forming a grid from top_left to bottom_right.
        The real part increases by step along columns, and the imaginary part decreases by step along rows.
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
    ...



def get_julia_color_arr(
        complex_arr: np.ndarray,
        c: complex,
        max_iterations: int
) -> np.ndarray:
    ...