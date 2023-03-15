
import sys
from PIL import Image, ImageDraw
from tqdm import tqdm
import heapq
import math
from dfs import dfs
from a_star import a_star
from list_transform import list_transform
def solution(file_path,alg,make_gif = False):
    images = [] # array of images to reproduce a gif
    result = list_transform(file_path) # transformation to an array
    if(alg == "dfs"):
        path , visited = dfs(result) # get path and list of visited nodes
    elif(alg == "a_star"):
        path , visited = a_star(result) # get path and list of visited nodes
    else:
        print("No such algorithm is available atm!")
        return

    def draw_maze(result):
        width, height = len(result[0]),len(result)
        cell_size = int(4000/width)
        img = Image.new('RGB', (width*cell_size, height*cell_size), color='white')
        draw = ImageDraw.Draw(img)

        for i in range(height):
            for j in range(width):
                x0, y0 = j*cell_size, i*cell_size
                x1, y1 = (j+1)*cell_size, (i+1)*cell_size
                if result[i][j] == '#':
                    draw.rectangle((x0, y0, x1, y1), fill='black')
                elif result[i][j] == '-':
                    draw.rectangle((x0, y0, x1, y1), fill='white')
                elif result[i][j] == '*':
                    draw.rectangle((x0,y0,x1,y1),fill = 'red')
                elif result[i][j] == 'x':
                    draw.rectangle((x0,y0,x1,y1),fill = 'yellow')
        images.append(img)

    def show_gif(filename):
        # Open the GIF file
        with Image.open(filename) as im:
            print("frame")
            # Loop through each frame of the GIF
            for frame in ImageSequence.Iterator(im):
                # Show the frame
                frame.show()

    if visited:
        for pos in tqdm(visited):
            row , col = pos
            result[row][col] = "x"
            if(make_gif):
                draw_maze(result)
    if path is not None:
        print("The path taken to reach the goal is:")
        move_count =0
        for pos in tqdm(path):
            move_count+=1
            row, col = pos
            result[row][col] = '*'
            #print("Move count is "+str(move_count))
            if(make_gif):
                draw_maze(result)
        if(make_gif):
            images[0].save('images/maze.gif',
                   save_all=True, append_images=images[1:],
                   optimize=False, duration=100, loop=0)
        else:
            draw_maze(result)
            images[0].save(f'images/maze{file_path}.jpg')
            images[0].show()
        print(path)
        return path
    else:
        print("No path found!")
        return("No path found!")

if __name__ == "__main__":

    if len(sys.argv) != 4 and len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <algorithm_name> <use_gif>")
        sys.exit(1)
    try:
        file_name = str(sys.argv[1])
        algorithm  = str(sys.argv[2])
        if(len(sys.argv) == 4):
            if(sys.argv[3] == "True"):
                gif = True
        else:
            gif = False
    except ValueError:
        print("Arguments should be strings.")
        sys.exit(1)

    solution(file_name , algorithm,gif)