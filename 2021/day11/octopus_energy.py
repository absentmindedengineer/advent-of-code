import numpy as np
import copy
#10x10 grid of octopi with their own energy level.


# Single step:
    #energy_level+=1
    #if energy_level>9:
        #all octopi surrounding it will gain an energy level.
        #thus a flashing octopus at coordinates.
        #cannot flash twice.

        #energy = 0 and does NOT gain any energy from others during this step.
        #a flash_flag would be appropriate maybe.
        
        #a function to take care of an octopus at certain coordinates would likely be appropriate as one will cause flashes within flashes and would want to do that recursively.

steps = 100
energy_grid = np.full((5,5),None)
raw_lst = []
with open('day11/example_ocotpus.txt','r') as f:
    raw_data = f.readlines()
    for row_idx in range(len(raw_data)):
        number_string = raw_data[row_idx].strip()
        for idx in range(len(number_string)):
            energy_grid[row_idx][idx] = int(number_string[idx])

# indices to increase
# [-1].-ö

#index_to_address = np.array([[-1,-1],[-1,0],[-1,1],[0,-1],[0,1], [1,-1],[1,0],[1,1]])

def flash_lightning(energy_grid, row_idx, column_idx, step_flashed_grid):
    step_flashed_grid[row_idx,column_idx] = True
    energy_grid[row_idx][column_idx] = 0


    #space handling
    index_to_address = np.array([[5,5]])#initial
    if row_idx != 0 and column_idx != 0:
        index_to_address = np.concatenate((index_to_address, np.array([[-1,-1],[-1,0]])))
        #index_to_address = np.concatenate((index_to_address, np.array([-1,0])))
    if row_idx != 0 and column_idx != len(energy_grid[row_idx]):
        index_to_address = np.concatenate((index_to_address, np.array([[-1,1]])))
    if column_idx != 0:
        index_to_address = np.concatenate((index_to_address, np.array([[0,-1]])))
    if column_idx != len(energy_grid[row_idx]):
        index_to_address = np.concatenate((index_to_address, np.array([[0,1]])))
    if row_idx != len(energy_grid) and column_idx != 0:
        index_to_address = np.concatenate((index_to_address, np.array([[1,-1]])))
        index_to_address = np.concatenate((index_to_address, np.array([[1,0]])))
    if row_idx != len(energy_grid) and column_idx != len(energy_grid[row_idx]):
        index_to_address = np.concatenate((index_to_address, np.array([[1,1]])))
    

    for position in index_to_address:
        if step_flashed_grid == False:
            energy_grid[row_idx+position[0]][column_idx+position[1]] += 1
            if energy_grid[row_idx+position[0]][column_idx+position[1]] > 9:
                flash_lightning(energy_grid, row_idx+position[0], column_idx+position[1], step_flashed_grid)
        else:
            #it did flash.
            pass
#initial_energy_grid = copy.copy(energy_grid)
for step in range(1,steps):
    step_flashed_grid = np.full((5,5),False) #only flash once so it resets every step.
    for row_idx in range(len(energy_grid)):
        for column_idx in range(len(energy_grid[row_idx])):
            energy_grid[row_idx][column_idx] += 1
            if energy_grid[row_idx][column_idx] > 9:
                #flash-functionality.
                flash_lightning(energy_grid, row_idx, column_idx, step_flashed_grid)
            else:
                #nothing
                pass