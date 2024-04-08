import traceback, time

#Change this value to adjust the time between turtle actions in seconds
draw_delay = 0.05

#Set this to False to turn off turtle entirely.
enable_turtle = False

if enable_turtle:
    import turtle

#Takes as input a Square object node in a graph of Square nodes.
# This will always be the Square node representing (0,0), the start position
#Performs DFS until the goal Square is found (the Square with color = "blue").
#Returns a list containing each Square node in the path from the start
# (0,0) to the goal node, inclusive, in order from start to goal.

#Global variables used in functions
goal = None
found = False #goal node has been found

def dfs_find_path(start_node):
    #allows us to access global variables
    global goal
    global found
    #initialize list to return
    ret_list = []
    #call dfs visit function 
    dfs_visit(start_node)
    #add path of nodes to list
    curr_node = goal
    while(curr_node.prev != None):
        ret_list.append(curr_node)
        curr_node = curr_node.prev
    ret_list.append(start_node)
    ret_list.reverse()
    #Reinitialize global variables
    goal = None
    found = False
    return ret_list
    
def dfs_visit(node):
    global found
    if (node.get_color() == "white") and (not found):
        node.set_color("gray")
        for v in node.adj:
            if v.get_color() == "white":
                v.prev = node
                dfs_visit(v)
            elif v.get_color() == "blue":
                v.prev = node
                global goal
                goal = v
                found = True
        node.set_color("black")

#  DO NOT EDIT BELOW THIS LINE

#Square class
#A single square on the grid, which is a single node in the graph.
#Has several instance variables:
# self.t: The turtle object used to draw this square
# self.x: The integer x coordinate of this square
# self.y: The integer y coordinate of this square
# self.adj: A list representing all non-blocked squares adjacent
#   to this one. (This is the node's adjacency list)
# self.__color: A private string representing the color of the square
#   Must be accessed using set_color and get_color because it's private
#   The color of the square is purple if it's a blocked square.
#   The color of the square is blue if it's the goal square.
#   Otherwise, it starts as white, and then progresses to grey and then
#   black according to the DFS algorithm.
# self.depth: An integer representing the depth of the node within DFS.
#   You don't really have to use this, but it may be helpful.
# self.prev: A Square object pointing to the node from which this node
#   was discovered from within DFS.
class Square:
    def __init__(self,x,y,val,t):
        self.t = t
        self.x = x
        self.y = y
        self.adj = []
        if val == 1:
            self.__color = "white"
        elif val == 2:
            self.__color = "blue"
        else:
            self.__color = "purple"
        self.depth = float("inf")
        self.prev = None
        
    #Getters and setters for color variable.  You MUST use these rather
    #  than trying to change color directly: it causes the squares to
    #  actually update color within the graphics window.
    def set_color(self,color):
        if color != self.__color:
            self.__color = color
            if enable_turtle:
                self.draw()
                turtle.update()
                time.sleep(draw_delay)
    def get_color(self):
        return self.__color
    
    #Draws the square
    def draw(self):
        t = self.t
        t.hideturtle()
        t.speed(0)
        t.pencolor("blue")
        if self.__color == "purple":
            t.pencolor("purple")
        t.fillcolor(self.__color)
        t.penup()
        t.setpos(self.x-.5,self.y-.5)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(1)
            t.left(90)
        t.end_fill()
        
    #String representation of a Square object: (x,y)
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    #Check equality between two Square objects.
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.x == other.x and self.y == other.y

#Takes as input a 2D list of numbers and a turtle object
#Outputs a 2D list of Square objects, which have their adjacency
#  lists initialized to all adjacent Square objects that aren't
#  blocked (so their val isn't 0).
def grid_to_squares(grid,t):
    square_grid = []
    for j in range(len(grid)):
        square_row = []
        for i in range(len(grid[j])):
            square_row.append(Square(i,j,grid[j][i],t))
        square_grid.append(square_row)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            adj = []
            if j+1 < len(grid) and grid[j+1][i]:
                adj.append(square_grid[j+1][i])
            if i+1 < len(grid[j]) and grid[j][i+1]:
                adj.append(square_grid[j][i+1])
            if j-1 >= 0 and grid[j-1][i]:
                adj.append(square_grid[j-1][i])
            if i-1 >= 0 and grid[j][i-1]:
                adj.append(square_grid[j][i-1])
            square_grid[j][i].adj = adj
    return square_grid

#Draws the entire grid of Square objects.
def draw_grid(square_grid):
    for j in range(len(square_grid)):
        for i in range(len(square_grid[j])):
            square_grid[j][i].draw()

#Test cases
if __name__ == '__main__':
    if enable_turtle:
        square_turtle = turtle.Turtle()
        square_turtle.hideturtle()
        square_turtle.speed(0)
        square_turtle.pencolor("blue")
    else:
        square_turtle = None
    grid0 = [[1,2],
             [0,0]]
    grid1 = [[1,0,2],
             [1,0,1],
             [1,1,1]]
    grid2 = [[1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1],
             [1,1,1,0,0,0,0],
             [1,1,1,0,2,1,1],
             [1,1,1,0,1,1,1],
             [1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1]]
    grid3 = [[1,1,0,0,0,0,0,0,0,0],
             [1,1,1,0,1,1,1,1,1,0],
             [0,1,1,0,1,0,1,1,1,0],
             [0,1,1,1,1,0,1,1,1,0],
             [0,1,0,0,0,0,0,0,1,0],
             [0,1,1,0,1,2,1,1,1,0],
             [0,0,1,0,1,0,1,0,1,0],
             [0,0,1,0,1,0,1,1,1,0],
             [0,1,1,1,1,1,1,1,1,0],
             [0,0,0,0,0,0,0,0,0,0]]
    grid4 = [[1,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,1,1,1,1,0],
             [0,1,0,1,1,1,0,0,1,0],
             [0,1,1,1,0,1,0,0,1,0],
             [0,1,0,1,0,1,1,0,0,0],
             [0,0,1,1,1,1,0,1,1,0],
             [0,0,1,0,0,1,1,1,0,0],
             [0,0,1,1,1,0,0,1,0,0],
             [0,0,1,0,1,0,2,1,1,0],
             [0,0,0,0,0,0,0,0,0,0]]
    grid5 = [
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 2, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]]

    map0d = grid_to_squares(grid0,square_turtle)
    map1d = grid_to_squares(grid1,square_turtle)
    map2d = grid_to_squares(grid2,square_turtle)
    map3d = grid_to_squares(grid3,square_turtle)
    map4d = grid_to_squares(grid4,square_turtle)
    map5d = grid_to_squares(grid5,square_turtle)

    path0d = [map0d[0][0],
             map0d[0][1]]
    path1d = [map1d[0][0],
             map1d[1][0],
             map1d[2][0],
             map1d[2][1],
             map1d[2][2],
             map1d[1][2],
             map1d[0][2]]
    path2d = [map2d[0][0],
             map2d[1][0],
             map2d[2][0],
             map2d[3][0],
             map2d[4][0],
             map2d[5][0],
             map2d[6][0],
             map2d[6][1],
             map2d[6][2],
             map2d[6][3],
             map2d[6][4],
             map2d[6][5],
             map2d[6][6],
             map2d[5][6],
             map2d[4][6],
             map2d[3][6],
             map2d[3][5],
             map2d[4][5],
             map2d[5][5],
             map2d[5][4],
             map2d[4][4],
             map2d[3][4]]
    path2dalt = [map2d[0][0],
             map2d[1][0],
             map2d[2][0],
             map2d[3][0],
             map2d[4][0],
             map2d[5][0],
             map2d[6][0],
             map2d[6][1],
             map2d[6][2],
             map2d[6][3],
             map2d[6][4],
             map2d[6][5],
             map2d[6][6],
             map2d[5][6],
             map2d[4][6],
             map2d[3][6],
             map2d[3][5],
             map2d[3][4]]
    path3d = [map3d[0][0],
             map3d[1][0],
             map3d[1][1],
             map3d[2][1],
             map3d[3][1],
             map3d[4][1],
             map3d[5][1],
             map3d[5][2],
             map3d[6][2],
             map3d[7][2],
             map3d[8][2],
             map3d[8][3],
             map3d[8][4],
             map3d[8][5],
             map3d[8][6],
             map3d[8][7],
             map3d[8][8],
             map3d[7][8],
             map3d[6][8],
             map3d[5][8],
             map3d[5][7],
             map3d[5][6],
             map3d[5][5]]
    path4d = [map4d[0][0],
             map4d[1][0],
             map4d[1][1],
             map4d[2][1],
             map4d[3][1],
             map4d[3][2],
             map4d[3][3],
             map4d[4][3],
             map4d[5][3],
             map4d[5][4],
             map4d[5][5],
             map4d[6][5],
             map4d[6][6],
             map4d[6][7],
             map4d[7][7],
             map4d[8][7],
             map4d[8][6]]
    path5d = [map5d[0][0],
             map5d[1][0],
             map5d[2][0],
             map5d[2][1],
             map5d[2][2],
             map5d[2][3],
             map5d[3][3],
             map5d[3][4],
             map5d[3][5],
             map5d[4][5],
             map5d[5][5],
             map5d[6][5],
             map5d[7][5],
             map5d[8][5],
             map5d[8][6],
             map5d[8][7],
             map5d[7][7],
             map5d[6][7],
             map5d[6][8],
             map5d[5][8],
             map5d[4][8],
             map5d[4][9],
             map5d[4][10],
             map5d[4][11],
             map5d[3][11],
             map5d[3][10],
             map5d[3][9],
             map5d[3][8],
             map5d[2][8],
             map5d[1][8],
             map5d[1][7],
             map5d[1][6]]
    path5dalt = [map5d[0][0],
             map5d[1][0],
             map5d[2][0],
             map5d[2][1],
             map5d[2][2],
             map5d[2][3],
             map5d[3][3],
             map5d[3][4],
             map5d[3][5],
             map5d[4][5],
             map5d[5][5],
             map5d[6][5],
             map5d[7][5],
             map5d[8][5],
             map5d[8][6],
             map5d[8][7],
             map5d[7][7],
             map5d[6][7],
             map5d[6][8],
             map5d[5][8],
             map5d[4][8],
             map5d[3][8],
             map5d[2][8],
             map5d[1][8],
             map5d[1][7],
             map5d[1][6]]


    tests = [map0d, map1d, map2d, map3d, map4d, map5d]
    grids = [grid0, grid1, grid2, grid3, grid4, grid5]
    correct = [path0d, path1d, path2d, path3d, path4d, path5d]
    #Test cases 3 and 6 give a different path if you check neighbors
    #for the goal squaure before recursing
    correctalt = [path0d, path1d, path2dalt, path3d, path4d, path5dalt]


    #Run test cases, check whether output path correct
    count = 0

    alg_short = ['DFS']
    alg_name = ['dfs_find_path']
    alg_pointers = [dfs_find_path]    


    try:
        for alg in range(1):
            for i in range(len(tests)):
                print("\n---------------------------------------\n")
                print(alg_short[alg]+" TEST #",i+1)
                square_grid = tests[i+alg*6]
                if enable_turtle:
                    turtle.resetscreen()
                    turtle.setworldcoordinates(-1,-1,len(tests[i][0]),len(tests[i]))
                    turtle.delay(0)
                    turtle.tracer(0,0)
                    draw_grid(square_grid)
                else:
                    print("\nTesting "+alg_name[alg]+" on the following grid:")
                    for row in grids[i][::-1]:
                        print(row)
                    print("Lower left corner is (0,0)")
                    print("0 is a swamp tile")
                    print("1 is a normal tile")
                    print("2 is the goal tile\n")
                pathlst = alg_pointers[alg](square_grid[0][0])
                print("Expected:",correct[i+alg*6],"\nGot     :",pathlst)
                assert type(pathlst) == list, "Return value is not of type list"
                if enable_turtle:
                    square_turtle.penup()
                    square_turtle.goto(0,0)
                    square_turtle.pendown()
                    square_turtle.color("green")
                    square_turtle.shape("turtle")
                    square_turtle.left(90)
                    square_turtle.showturtle()
                    for square in pathlst:
                        square_turtle.goto(square.x,square.y)
                        turtle.update()
                        time.sleep(draw_delay)
                assert pathlst == correct[i+alg*6] or pathlst == correctalt[i+alg*6], "Path incorrect"
                print("Test Passed!\n")
                count += 1
    except AssertionError as e:
        print("\nFAIL: ",e)
    except Exception:
        print("\nFAIL: ",traceback.format_exc())


    print(count,"out of",len(tests),"tests passed.")


