import numpy as np 

def main():
    with open('Day3/input_day3.txt','r') as f:
        lines = f.readlines()

        x_axis = 0
        y_axis = 0
        trees_in_the_way = 0
        #flip the map!
        flipped_stuff = zip(*lines)
        try:
            for i in range(999999):
                if (flipped_stuff[y_axis][x_axis]) == "#":
                    trees_in_the_way += 1
                x_axis += 3
                y_axis += 1           
        except IndexError:
            pass

    print(trees_in_the_way)
    
    #tried 6 - incorrect



if __name__ == "__main__":
    main()    