import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    ...



def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    ...



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