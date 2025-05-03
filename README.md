# Game of Life V2

## Overview

This is an implementation of Conway's Game of Life. I developed this project using my Pygame template. The game features a grid of cells that evolve based on a set of rules.

## Key Features

* Classic Game of Life simulation.
* Interactive cell activation/deactivation with mouse clicks.
* Manual step-by-step evolution using the Enter key.
* Automatic running of the simulation with Spacebar toggle.
* Uses Pygame for graphics and event handling.

## Prerequisites

This project **requires** my custom Pygame framework, `pygame_template`, to function correctly. **This framework is currently hosted on my personal GitHub and will need to be installed directly from there.**

## Installation

1.  **Clone the Game of Life V2 repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the `pygame_template` framework from GitHub:**

    * **Note:** As `pygame_template` is not available on PyPI, you will need to install it directly from my GitHub repository. The command will look something like this:

        ```bash
        pip install git+[https://github.com/FINN-2005/pygame_template.git](https://github.com/FINN-2005/pygame_template.git)
        ```

## How to Run

1.  **Navigate to the project directory (if you haven't already):**

    ```bash
    cd <repository_directory>
    ```

2.  **Run the game:**

    ```bash
    python main.py
    ```

## Important Notes

* This project is built upon my custom `pygame_template` framework, which needs to be installed directly from my GitHub repository as outlined in the Installation section.
* Press Spacebar to toggle between manual stepping and automatic running.
* Click the mouse to activate or deactivate cells.
* Press Enter to manually step the simulation.
