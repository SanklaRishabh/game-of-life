import numpy as np
import pygame
import time
import universe


# Define window resolution.
WINDOW_RES: tuple[int] = (800, 600)


def main() -> None:
    pygame.init()

    # Create a window instance.
    window_surface: pygame.Surface = pygame.display.set_mode(WINDOW_RES)
    icon: pygame.Surface = pygame.image.load("src/icon.png")

    pygame.display.set_icon(icon)
    pygame.display.set_caption("Conway's Game of Life")

    # Create a matrix to represent the cellular universe.
    grid: np.ndarray = np.zeros(
        tuple(size // 10 for size in reversed(WINDOW_RES)))
    cell_size: int = 10

    # Fill the entire screen with a color other than the background color.

    # This will create the borders for the cells
    # when the background color is applied.
    window_surface.fill(universe.COLOR_GRID)

    # Update the grid.
    universe.update_grid(window_surface, grid, cell_size)

    pygame.display.flip()

    # Create a flag to check game status.
    is_running: bool = False

    # Create game loop.
    while True:
        # Check for user interaction with the GUI.
        for event in pygame.event.get():
            # Trigger event for when user clicks close button.
            if event.type == pygame.QUIT:
                pygame.quit()

                return None

            # Trigger event for when user presses a key.
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_running = not is_running  # Plays/pauses the game.

                universe.update_grid(window_surface, grid, cell_size)

                pygame.display.update()

            # Trigger event for when user interacts with mouse.
            elif any(pygame.mouse.get_pressed()):
                # Get cursor position.
                x_pos, y_pos = pygame.mouse.get_pos()

                # Update the cell that was clicked.
                grid[y_pos // 10, x_pos // 10] = 1

                universe.update_grid(window_surface, grid, cell_size)

                pygame.display.update()

        if is_running:
            grid = universe.update_grid(
                window_surface, grid, cell_size, with_progress=True
            )

            pygame.display.update()

            time.sleep(0.005)


# Driver code.
if __name__ == "__main__":
    main()
