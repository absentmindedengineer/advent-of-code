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
