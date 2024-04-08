import copy, traceback, time
#float value representing amount of time, in seconds, to delay after
#   each time the tree changes.  Adjust as you wish, but set it back
#   to 0.0 before submitting.
draw_delay = 0.0

#Set this to False to turn off turtle entirely.
enable_turtle = True


#find_bee: takes in a B-Tree tree, and a key value to search for.
#  returns the Bee object within the tree with that key,
#  or None if there is no such object.
#See PA08 instructions for how B-Trees are formatted with nested lists.
def find_bee(tree,key):
    x = 0
    i = 1
    isLeafNode = True
    while x < len(tree):
        if tree[x] != None:
            isLeafNode = False
        x += 2    
    while i < len(tree) and key > tree[i].key:
        i += 2
    if i < len(tree) and key == tree[i].key:
        return tree[i]
    elif isLeafNode:
        return None     
    else:
        return find_bee(tree[i-1], key)

#insert_bee: takes in a B-Tree tree, and a Bee object to insert to the B-Tree
#  returns the new B-Tree with the Bee object inserted, as demonstrated in
#  lecture/the textbook.
#See PA08 instructions for how B-Trees are formatted with nested lists
#Hint: look up how the .insert list method and list slicing work in Python.
#  These will be very helpful for inserting keys into nodes, and breaking nodes
#  into multiple pieces, respectively.

#I would not recommend trying to copy paste the textbook pseudocode in
#for this, since the nested list implementation is quite different
#from how the textbook sets up node objects. Instead, look at pictures of
#how the insertion algorithm works, and try to implement that.

def insert_bee(tree,bee):
    # #Check if tree is full, if so split it
    if len(tree) == 7:
        newTree = []
        newTree.append(tree[0:3])
        newTree.append(tree[3])
        newTree.append(tree[4:7])
        tree = newTree
    
    #Check if tree is leaf node
    x = 0
    isLeafNode = True
    while x < len(tree):
        if tree[x] != None:
            isLeafNode = False
        x += 2 
    
    #If tree not leaf node, we don't want to insert. We want to find which child node to insert at
    if (not isLeafNode):
        i = len(tree)-2 #index of last bee in list, Note that len(tree) will always be >= 3 since it is not leaf node
        while i >= 0 and bee.key < tree[i].key:
            i -= 2
        child_node_to_insert_at = tree[i+1]
        if (len(child_node_to_insert_at) == 7): #If child node full, anticipate split
            middlePart = insert_bee(child_node_to_insert_at, bee)
            return tree[0:i+1] + [middlePart[0]] + [middlePart[1]] + [middlePart[2]] + tree[i+2:]
        else: #If child node is not full, concatenate normally
            return tree[0:i+1] + [insert_bee(child_node_to_insert_at, bee)] + tree[i+2:]
    
    #If tree is leaf node, we want to find which index to insert at
    else:
        if (len(tree) == 1): #Empty tree
            tree.insert(1, None)
            tree.insert(1, bee)
        else: #Tree is of length 3 or 5, Note that tree will never be full since we checked that at beginning of function
            i = len(tree)-2 #index of last bee in tree
            while i >= 0 and bee.key < tree[i].key:
                i -= 2
            tree.insert(i+2, None)
            tree.insert(i+2, bee)
        return tree

#DO NOT EDIT BELOW THIS LINE

#Bee class
#self.name is a string representing the name of the bee
#self.key is an integer representing the identification key of the bee

class Bee:
    def __init__(self,name,key):
        self.name = name
        self.key = key
    def __repr__(self):
        return self.name + ":" + str(self.key)
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.name == other.name and \
               self.key == other.key
    def __lt__(self,other):
        return self.key < other.key
    def copy(self):
        return Bee(self.name,self.key)

#Set up turtle, if enabled
if enable_turtle:
    import turtle
    turtle.setworldcoordinates(-400,-400,400,400)
    turtle.speed(0)
    turtle.delay(0)
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.tracer(0,0)

#Draws one node in the B-Tree
def draw_node(lst,x,y):
    try:
        turtle.color('black')
        turtle.penup()
        turtle.setpos(x-(len(lst)*10-10),y-10)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(len(lst)*20-20)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
        turtle.end_fill()
        turtle.color('yellow')
        to_write = [x.key for x in lst[1::2]]
        turtle.write(str(to_write),align="left",font=("Courier",14,"bold"))
    except Exception:
        print("\nError while drawing node:", lst, traceback.format_exc())

#Draws entire B-Tree, recursively
def draw_tree(T,level,left,right,up):
    try: 
        draw_node(T,(left+right)//2,100-level*50+up)
        if T[0] != None:
            divs = len(T[::2])
            steps = (right-left)/(divs)
            i = 0
            for node in T[::2]:
                turtle.penup()
                startx = (left+right)//2 - (len(T)*10-10) + i*40
                turtle.setpos(startx,90-level*50+up)
                turtle.pendown()
                new_left = left+steps*i
                new_right = left+steps*(i+1)
                turtle.color('black')
                turtle.setpos((new_left+new_right)//2,60-level*50+up)
                draw_tree(node, level+1, new_left, new_right, up)
                i += 1
    except Exception:
        print("\nError while drawing node:", T, traceback.format_exc())

#Test cases

#Most of these are valid two-letter words in Scrabble.
names = ['Ay', 'Bo', 'Ch', 'Da', 'Ed', 'Fe', 'Gi', 'Ha', 'Id', 'Jo',
         'Ki', 'Lo', 'Mm', 'Nu', 'Op', 'Pa', 'Qi', 'Re', 'Si', 'Ta',
         'Ut', 'Vi', 'Wo', 'Xu', 'Ye', 'Za']

keys = [42, 83, 20, 86, 35, 89, 32, 30, 61, 87,
        52, 79, 12, 70, 49, 95, 26, 48, 19, 29,
        93, 69, 22, 55, 46, 40]

#Note the structure of B-Trees being used: even indexes represent child pointers,
# odd indexes represent keys.  If the given node is a leaf node, then all child
# pointers are None rather than another nested list.

tree1 = [[None, Bee('Ch',20), None, Bee('Ed',35), None],
         Bee('Ay',42),
         [None, Bee('Bo',83), None, Bee('Da',86), None]]

tree2 = [
    [[None, Bee('Mm',12), None, Bee('Si',19), None, Bee('Wo',22), None],
        Bee('Qi',26),
        [None, Bee('Ta',29), None, Bee('Ha',30), None]],
    Bee('Gi',32),
        [[None, Bee('Za',40), None, Bee('Ye',46), None, Bee('Re',48), None],
        Bee('Op',49),
        [None, Bee('Ki',52), None, Bee('Xu',55), None]],
    Bee('Id',61),
        [[None, Bee('Vi',69), None, Bee('Nu',70), None],
        Bee('Lo',79),
        [None, Bee('Jo',87), None, Bee('Ut',93), None, Bee('Pa',95), None]]]

tree3 = [[None, Bee('Ch',20), None, Bee('Ed',35), None],
         Bee('Ay',42),
         [None, Bee('Bo',83), None, Bee('Da',86), None, Bee('Fe',89), None]]

tree4 = [[None, Bee('Ch',20), None, Bee('Ha',30), None, Bee('Ed',35), None],
         Bee('Ay',42),
         [None, Bee('Bo',83), None, Bee('Da',86), None, Bee('Fe',89), None]]

tree5 = [[None, Bee('Ch',20), None],
         Bee('Ha',30),
         [None, Bee('Gi',32), None, Bee('Ed',35), None],
         Bee('Ay',42),
         [None, Bee('Bo',83), None, Bee('Da',86), None, Bee('Fe',89), None]]

tree6 =  [[None, Bee('Ch',20), None],
         Bee('Ha',30),
         [None, Bee('Gi',32), None, Bee('Ed',35), None],
         Bee('Ay',42),
         [None, Bee('Id',61), None, Bee('Bo',83),None],
         Bee('Da',86),
         [None, Bee('Fe',89), None]]

tree7 = [[[None, Bee('Ch',20), None],
         Bee('Ha',30),
         [None, Bee('Gi',32), None, Bee('Ed',35), None]],
        Bee('Ay',42),
         [[None, Bee('Id',61), None, Bee('Bo',83),None],
         Bee('Da',86),
         [None, Bee('Jo', 87), None, Bee('Fe',89), None]]]


input_trees = [tree1, tree1, tree1, tree2, tree2, tree2, tree1, tree3, tree4, tree5, tree6, [None]]
input_bees = [42, 38, 86, 61, 46, 97, Bee('Fe',89), Bee('Ha',30), Bee('Gi',32), Bee('Id',61), Bee('Jo',87)]
corr = [Bee('Ay',42), None, Bee('Da',86), Bee('Id',61), Bee('Ye',46), None, tree3, tree4, tree5, tree6, tree7, tree2]

count = 0

try:
    for i in range(len(input_trees)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1,":")
        testtree = copy.deepcopy(input_trees[i])
        if enable_turtle:
            turtle.clearscreen()
            turtle.tracer(0,0)
            turtle.hideturtle()
            draw_tree(testtree, 0, -400, 400, 0)
            turtle.update()
            
        if i < 6:
            print("Running find_bee("+str(testtree)+",\n"+str(input_bees[i])+")")
            actual = find_bee(testtree,input_bees[i])
            assert corr[i] == actual,\
                   "Search result incorrect \nExpected: " + \
                   str(corr[i]) + "\nGot:      " + str(actual)
        elif i < 11:
            print("Running insert_bee("+str(testtree)+",\n"+str(input_bees[i])+")")
            actual = insert_bee(testtree,input_bees[i])
            
            if enable_turtle:
                turtle.clearscreen()
                turtle.tracer(0,0)
                turtle.penup()
                turtle.setpos(-300, 300)
                turtle.color("black")
                turtle.write("Expected",align="left",font=("Courier",20,"bold"))
                draw_tree(copy.deepcopy(corr[i]), 0, -400, 400, 200)
                turtle.penup()
                turtle.setpos(-300, -100)
                turtle.color("black")
                turtle.write("Got",align="left",font=("Courier",20,"bold"))
                draw_tree(actual, 0, -400, 400, -200)
                turtle.update()
                time.sleep(draw_delay)
            assert copy.deepcopy(corr[i]) == actual,\
                   "Insert result incorrect \nExpected: " + \
                   str(corr[i]) + "\nGot:      " + str(actual)
        else:
            print("Inserting all of the following, in order:",
                  [Bee(names[x],keys[x]) for x in range(6,26)])
            for x in range(6,26):
                print("Inserting", Bee(names[x],keys[x]))
                testtree = insert_bee(testtree,Bee(names[x],keys[x]))
                print("Resulting tree", testtree)
                if enable_turtle:
                    turtle.clearscreen()
                    turtle.tracer(0,0)
                    turtle.hideturtle()
                    draw_tree(testtree, 0, -400, 400, 0)
                    turtle.update()
                    time.sleep(draw_delay)
            if enable_turtle:
                turtle.clearscreen()
                turtle.tracer(0,0)
                turtle.penup()
                turtle.setpos(-300, 300)
                turtle.color("black")
                turtle.write("Expected",align="left",font=("Courier",20,"bold"))
                draw_tree(copy.deepcopy(corr[i]), 0, -400, 400, 200)
                turtle.penup()
                turtle.setpos(-300, -100)
                turtle.color("black")
                turtle.write("Got",align="left",font=("Courier",20,"bold"))
                draw_tree(testtree, 0, -400, 400, -200)
                turtle.update()
                time.sleep(draw_delay)
            assert copy.deepcopy(corr[i]) == testtree,\
                   "Insert result incorrect \nExpected: " + \
                   str(corr[i]) + "\nGot:      " + str(actual)
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print("\n---------------------------------------\n")
print(count,"out of",12,"tests passed.")
