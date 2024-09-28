import numpy as np
import pygame


# Define color codes.
COLOR_BG: tuple[int] = (10, 10, 10)
COLOR_GRID: tuple[int] = (40, 40, 40)
COLOR_DIE_NEXT: tuple[int] = (170, 170, 170)
COLOR_ALIVE_NEXT: tuple[int] = (255, 255, 255)


def update_grid(
    screen: pygame.Surface,
    cells: np.ndarray,
    size: int,
    with_progress: bool = False,
) -> np.ndarray:
    # Create a matrix to store the new state.
    updated_cells: np.ndarray = np.zeros(cells.shape)

    for row, col in np.ndindex(cells.shape):
        # Determine the number of alive neighbors for each cell.
        alive: np.ndarray = (
            np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
        )

        # Select a default color.
        color: tuple[int] = COLOR_BG if not cells[row,
                                                  col] else COLOR_ALIVE_NEXT

        if cells[row, col]:
            if (alive < 2 or alive > 3) and with_progress:
                color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1

                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1

                if with_progress:
                    color = COLOR_ALIVE_NEXT

        # Draw cells on the surface.
        pygame.draw.rect(screen, color, (col * size,
                         row * size, size - 1, size - 1))

    return updated_cells
