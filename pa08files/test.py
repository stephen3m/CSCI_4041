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

# def insert_bee(tree,bee):
#     # #Check if tree is full, if so split it
#     if len(tree) == 7:
#         newTree = []
#         newTree.append(tree[0:3])
#         newTree.append(tree[3])
#         newTree.append(tree[4:7])
#         tree = newTree
    
#     #Check if tree is leaf node
#     x = 0
#     isLeafNode = True
#     while x < len(tree):
#         if tree[x] != None:
#             isLeafNode = False
#         x += 2 
    
#     #If tree not leaf node, we don't want to insert. We want to find which child node to insert at
#     if (not isLeafNode):
#         i = len(tree)-2 #index of last bee in list, Note that len(tree) will always be >= 3 since it is not leaf node
#         while i >= 0 and bee.key < tree[i].key:
#             i -= 2
#         child_node_to_insert_at = tree[i+1]
#         if (len(child_node_to_insert_at) == 7):
#             middlePart = insert_bee(child_node_to_insert_at, bee)
#             return tree[0:i+1] + [middlePart[0]] + [middlePart[1]] + [middlePart[2]] + tree[i+2:]
#         else:
#             return tree[0:i+1] + [insert_bee(child_node_to_insert_at, bee)] + tree[i+2:]
    
#     #If tree is leaf node, we want find which index to insert at
#     else:
#         if (len(tree) == 1): #Empty tree
#             tree.insert(1, None)
#             tree.insert(1, bee)
#         else: #Tree is of length 3 or 5
#             i = len(tree)-2 #index of last bee in tree
#             while i >= 0 and bee.key < tree[i].key:
#                 i -= 2
#             tree.insert(i+2, None)
#             tree.insert(i+2, bee)
#         return tree
    
# l1 = [[None, Bee('Ch',20), None, Bee('Ed',35), None],
#          Bee('Ay',42),
#  [None, Bee('Bo',83), None, Bee('Da',86), None, Bee('Ze', 89), None]]

# print(insert_bee(l1, Bee('De',43)))

    
l = [[[None, Bee('Mm',12), None, Bee('Si',19), None, Bee('Wo',22), None],
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

print(l[0])
print("\n")
print(l[1])
print("\n")
print(l[2])
print("\n")
print(l[3])
print("\n")
print(l[4])