#Enables the graphical display of the database
#Set to False to disable
import traceback, time
enable_turtle = True
if enable_turtle:
    import turtle


#Takes Database object database, and Robot object robot
#Inserts robot into database.  This requires inserting robot
#into all three hash tables within the Database.
#Use hash_function, defined below, to determine which slot a given
#robot should be hashed into for each table.
def database_insert(database,robot):
    nameSlot = hash_function(robot.name)
    colorSlot = hash_function(robot.color)
    shapeSlot = hash_function(robot.shape)
    
    database.name_table[nameSlot].append(robot)
    database.color_table[colorSlot].append(robot)
    database.shape_table[shapeSlot].append(robot)

#Takes Database object database, string field (must be "name","shape","color")
#and string value, representing what value for the given field to search for
#Returns a list containing every Robot element in database with a matching
#value in the given field.
#E.g. database_search(data,"shape","circle") would return a list of all
#circle robots within data.
#Note: Do NOT search the entire database: you must use hash_function to
#determine which slot in the corresponding table to search.
def database_search(database,field,value):
    retList = []
    slotNumber = hash_function(value)
    if (field == "name"):
        for i in range(len(database.name_table[slotNumber])):
            currRobot = database.name_table[slotNumber][i]
            if (currRobot.name == value):
                retList.append(currRobot)
    elif (field == "shape"):
        for i in range(len(database.shape_table[slotNumber])):
            currRobot = database.shape_table[slotNumber][i]
            if (currRobot.shape == value):
                retList.append(currRobot)
    elif (field == "color"):
        database.color_table[slotNumber]
        for i in range(len(database.color_table[slotNumber])):
            currRobot = database.color_table[slotNumber][i]
            if (currRobot.color == value):
                retList.append(currRobot)
    return retList

#Takes Database object database, string field (must be "name","shape","color")
#and string value, representing what value for the given field to search for
#Removes all Robots with a matching value in the given field from the database
#This will require removing them from all three tables.
def database_delete(database,field,value):
    robotList = database_search(database,field,value)
    for i in range(len(robotList)):
        robot = robotList[i]
        nameSlot = hash_function(robot.name)
        colorSlot = hash_function(robot.color)
        shapeSlot = hash_function(robot.shape)
        index = 0
        print(database.name_table[nameSlot])
        for j in range(len(database.name_table[nameSlot])):
            if (database.name_table[nameSlot][j] == robot):
                index = j
        database.name_table[nameSlot].pop(index)
        for j in range(len(database.color_table[colorSlot])):
            if (database.color_table[colorSlot][j] == robot):
                index = j
        database.color_table[colorSlot].pop(index)
        for j in range(len(database.shape_table[shapeSlot])):
            if (database.shape_table[shapeSlot][j] == robot):
                index = j
        database.shape_table[shapeSlot].pop(index)

## DO NOT EDIT BELOW THIS LINE

    
#Hash function that works for all three attributes
#Takes in a string, outputs an integers between 0 and 4 inclusive
#This represents which slot the Robot should be hashed into
#for each attribute
def hash_function(string):
    total = 0
    for i in string:
        total *= 2
        total += ord(i)
        total %= 5
    return total

#Robot class
#self.name is a string representing the name of the robot
#self.shape is a string representing the shape of the robot
#self.color is a string representing the color of the robot
#self.data is a list with all three attributes, in order name, shape, color

class Robot:
    def __init__(self,name,shape,color):
        self.name = name
        self.shape = shape
        self.color = color
        self.data = [self.name,self.shape,self.color]
        
    def __repr__(self):
        return self.name + ":" + self.shape + ":" + self.color
    
    def draw(self,x,y,table_index):
        self.turtles = [turtle.Turtle(),turtle.Turtle(),turtle.Turtle()]
        for t in self.turtles:
            t.hideturtle()
            t.penup()
        self.turtles[table_index].goto(x,y)
        self.turtles[table_index].shape(self.shape)
        self.turtles[table_index].color(self.color)
        self.turtles[table_index].showturtle()

    def __eq__(self,other):
        return type(self) == type(other) and \
               self.name == other.name and \
               self.shape == other.shape and \
               self.color == other.color

    def copy(self):
        return Robot(self.name,self.shape,self.color)

    #THIS IS NOT THE HASH FUNCTION YOU'RE LOOKING FOR.
    def __hash__(self):
        total = 0
        for i in self.name:
            total *= 26
            total += ord(i)
        return total


#Database class: consists of three hash tables of Robot objects
#self.name_table is a hash table of Robot objects, indexed by name
#self.shape_table is a hash table of Robot objects, indexed by shape
#self.color_table is a hash table of Robot objects, indexed by color
#Each Hash table is implemented as a list of 5 slots.
#Each slot is itself a list (since we're doing collision by chaining)
#self.tables is a list of all three tables, in the order name, shape, color

class Database:
    def __init__(self):
        self.name_table = [list() for i in range(5)]
        self.shape_table = [list() for i in range(5)]
        self.color_table = [list() for i in range(5)]
        self.tables = [self.name_table,self.shape_table,self.color_table]

    def draw(self):
        table_labels = ["Name Table", "Shape Table", "Color Table"]
        draw_turtle = turtle.Turtle()
        draw_turtle.penup()
        draw_turtle.hideturtle()
        y = 250
        for i in range(3):
            table = self.tables[i]
            draw_turtle.goto(-160,y+17)
            draw_turtle.write(table_labels[i],align="right",font=("Arial",16,"normal"))
            for j in range(len(table)):
                slot = table[j]
                x = -200
                draw_turtle.goto(x-20,y-13)
                draw_turtle.write(j,align="right",font=("Arial",16,"normal"))
                for item in slot:
                    item.draw(x,y,i)
                    x += 30
                y -= 25
            y -= 60

    def __repr__(self):
        table_labels = ["Name Table", "Shape Table", "Color Table"]
        outstr = ""
        for i in range(3):
            outstr += table_labels[i] +"\n"
            for j in range(5):
                outstr += "Row "+str(j)+ " : "+str(self.tables[i][j])+"\n"
            outstr += "\n"
        return outstr

    def __eq__(self,other):
        fields = ["Name","Shape","Color"]
        assert type(self) == type(other),\
               "comparing Database to non-Database"
        for i in range(3):
            for j in range(5):
                assert(set(self.tables[i][j]) == set(other.tables[i][j])),\
                                       fields[i]+" Table incorrect.\nExpected:\n"+\
                                       str(self)+"\nGot:\n"+str(other)
        return True
    


if __name__ == '__main__':



    robot1 = Robot("Ani","turtle","green")
    robot2 = Robot("Bob","square","purple")
    robot3 = Robot("Cap","turtle","grey")
    robot4 = Robot("Din","circle","red")
    robot5 = Robot("Ent","square","brown")
    robot6 = Robot("Fox","triangle","orange")
    robot7 = Robot("Gil","turtle","blue")
    robot8 = Robot("Han","square","blue")
    robot9 = Robot("Ick","turtle","brown")
    robot10 = Robot("Jon","square","black")
    robot11 = Robot("Kat","turtle","orange")
    robot12 = Robot("Lou","triangle","green")
    robot13 = Robot("Map","square","red")
    robot14 = Robot("Nop","circle","black")
    robot15 = Robot("Ooo","triangle","purple")
    robot16 = Robot("Pam","turtle","red")
    robot17 = Robot("Que","square","green")
    robot18 = Robot("Rem","circle","blue")
    robot19 = Robot("Sol","triangle","grey")
    robot20 = Robot("Tod","circle","orange")
    robot21 = Robot("Uno","triangle","black")
    robot22 = Robot("Viv","turtle","purple")
    robot23 = Robot("Wow","circle","brown")
    robot24 = Robot("Xor","square","orange")
    robot25 = Robot("Yay","triangle","red")
    robot26 = Robot("Zed","circle","purple")

    robots = [robot1, robot2, robot3, robot4, robot5,
              robot6, robot7, robot8, robot9, robot10,
              robot11, robot12, robot13, robot14, robot15,
              robot16, robot17, robot18, robot19, robot20,
              robot21, robot22, robot23, robot24, robot25, robot26]

    copy_robots = list(map(lambda x: x.copy(),robots))


    count = 0

    operations = "isdiisdsisddisds"

    inp = [[0],["shape","turtle"],["color","green"],[1],
           [2,3,4],["color","orange"],["name","Bob"],["color","red"],
           [5,6,7,8,9,10],["shape","square"],["shape","turtle"],["name","Fox"],
           list(range(11,25)),["name","Uno"],["shape","triangle"],["color","red"]]

    corr = [["a####","##a##","#a###"],
            "a",
            ["####","####","####"],
            ["####b","#b###","###b#"],
            ["##de##c","#e#c#d#","##e#cd#"],
            "",
            ["##de##c","#e#c#d#","##e#cd#"],
            "d",
            ["k##fghi#j#","f#hj#gik##","j#gh#i##fk"],
            "hj",
            ["##fh#j#","f#hj###","j#h###f"],
            ["##h#j#","#hj###","j#h###"],
            ["#nuy#sv#lptx#moqrw","losuy#mqx#pv#nrtw#","nu#lqr#w#mopsvy#tx"],
            "u",
            ["#n#v#ptx#mqrw","#mqx#pv#nrtw#","n#qr#w#mpv#tx"],
            "mp"]

    def st_to_robot(st):
        outls = []
        for ch in st:
            outls.append(copy_robots[ord(ch)-97])
        return outls

    def expand_corr(corr_ls):
        d = Database()
        for i in range(len(corr_ls)):
            slots = corr_ls[i].split("#")
            table = list(map(st_to_robot,slots))
            d.tables[i] = table
        return d
            
                
            
    try:
        d = Database()
        for i in range(len(operations)):
            print("\n---------------------------------------\n")
            print("TEST #",i+1)
            if operations[i] == "i":
                inslist = list(map(lambda x: robots[x],inp[i]))
                for robot in inslist:
                    print("Inserting:",robot)
                    database_insert(d,robot)
                    #print(d)
                corr_database = expand_corr(corr[i])
            elif operations[i] == "s":
                print("Search:",inp[i][0],inp[i][1])
                out = database_search(d,inp[i][0],inp[i][1])
                corr_list = st_to_robot(corr[i])
                print("Expected:", corr_list)
                print("Got:     ", out)
                assert set(out)==set(corr_list),"Search Result incorrect"
            elif operations[i] == "d":
                print("Delete:",inp[i][0],inp[i][1])
                database_delete(d,inp[i][0],inp[i][1])
                corr_database = expand_corr(corr[i])
            if enable_turtle:
                turtle.clearscreen()
                turtle.tracer(0,0)
                d.draw()
                turtle.update()
            if operations[i] != "s":
                corr_database == d
            count += 1
            if (i%4) == 3:
                print("\n---------------------------------------\n")
                print("Reseting Database...")
                d = Database()
    except AssertionError as e:
        print("\nFAIL: ",e)
    except Exception:
        print("\nFAIL: ",traceback.format_exc())

    print("\n---------------------------------------\n")
    print(count,"out of",16,"tests passed.")


