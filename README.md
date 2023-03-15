
# ECM2423 - Maze Solver

## Overview

ECM2423 Maze Solver is a Python application that solves mazes using various pathfinding algorithms. It takes a text file containing a maze representation as input and outputs the solution as an image. The application currently supports Depth-First Search (DFS) and A* algorithms. Additionally, it can generate a GIF to visualize the solving process.

## Table of Contents

1. [Installation](#installation)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Customizing Input](#customizing-input)
5. [Contributing](#contributing)

## Installation

1. Clone the repository to your local machine:
```git clone https://github.com/qwazzarr/ECM2423.git```

2. Navigate to the newly-created `ECM2423` directory:

``` cd ECM2423 ```
## Requirements

- Python 3.7 or later
- Pillow
- tqdm

You can install the required dependencies using pip:
``` pip install Pillow tqdm ```
## Usage

Run the application using the following command:

``` python solution.py <file_name> <algorithm_name> <use_gif> ```
- `<file_name>`: The name of the text file containing the maze representation.
- `<algorithm_name>`: The name of the pathfinding algorithm to use (either "dfs" or "a_star").
- `<use_gif>` (optional): Set to "True" to generate a GIF visualization of the solving process. Defaults to "False" if not provided.

For example:

``` python solution.py maze-Easy.txt dfs ```

The solved maze will be saved as an image in the `images/` directory, and a GIF will be generated if the `<use_gif>` option is set to "True".

## Customizing Input

You can create your own maze by following these conventions in a text file:

- `#`: Walls
- `-`: Open paths
- `-` on the first line: Start point
- `-` on the last line: End point

For example:

``` 
# - # # # # # # # # # # # # # # # # # # 
# - - - - - - - - - - - - - - - - - # # 
# # # # # - # # - # # - # # # - # - - #
# - # # # - # - - # # - # # - - # - # # 
# - # - - - # # # # # # # # # - # - - # 
# - - - # - - - - # - # # - # - # # # #
# - # # # # - # - - - - - - - - - - - #
# - # # - - - # # # # # # # # # # - # #
# - - - - # - - # # - - - - - - - - - #
# # # # # # # # # # # # # # # # # # - # 
```

## Contributing

Contributions to the ECM2423 Maze Solver project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes to the new branch.
4. Create a pull request with a detailed description of your changes.