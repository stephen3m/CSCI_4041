import random, timeit

# def mystery1(vals):
#     diff = 0
#     for i in range(len(vals)):
#         for j in range(len(vals)):
#             if(vals[i] - vals[j] > diff):
#                 diff = vals[i] - vals[j]
#     return diff

def mystery1(vals):
    min = vals[0]
    max = vals[0]
    for i in range(len(vals)): 
        if (vals[i] < min):
            min = vals[i]
    for i in range(len(vals)):
        if (vals[i] > max):
            max = vals[i]
    return max-min


# def mystery2(filename): //returns dictionary that shows how many times each character shows up in file
#     time = {} //dictionary
#     with open(filename) as fp: //error handling
#         text = fp.read() //text is an entire string
#         for ltr in text: //Loop through each character in string
#             time[ltr] = text.count(ltr) //count() returns # of instances ltr occurs in text
#     return time

def mystery2(filename):
    time = {}
    with open(filename) as fp:
        text = fp.read()
        for ltr in text:
            if (ltr in time.keys()):
                time[ltr] += 1
            else:
                time[ltr] = 1
    return time
    

# def mystery3(filename): #['Gimli', 'Boromir', 'Merry', 'Pippin', 'Legolas', 'Sam', 'Gandalf', 'Aragorn', 'Frodo']
#     storage = []
#     with open(filename) as fp:
#         for line in fp:
#             items = line.split()
#             name = items[0]
#             time = int(items[1])
#             if time >= len(storage): #Need more spots in storage
#                 x = time - len(storage) + 1
#                 extend = ['']*x #Makes a list of x empty strings
#                 storage = storage + extend
#             storage[time] = name
#     sort_list = []
#     for spot in storage:
#         if spot != '': #Ignore empty spots
#             sort_list.append(spot)
#     return sort_list

def mystery3(filename):
    two_dim_storage = [] #2d list that contains info for each character & their screen time 
    sorted_list = []
    with open(filename) as fp:
        for line in fp:
            items = line.split()
            name = items[0]
            time = int(items[1])
            two_dim_storage.append([name, time])
        for i in range(len(two_dim_storage)-1): #use bubble sort to sort list
            for j in range(len(two_dim_storage)-1, i, -1):
                if two_dim_storage[j][1] < two_dim_storage[j-1][1]:
                    tmp = two_dim_storage[j-1]
                    two_dim_storage[j-1] = two_dim_storage[j]
                    two_dim_storage[j] = tmp
        for i in range(len(two_dim_storage)):
            sorted_list.append(two_dim_storage[i][0])
    return sorted_list

if __name__ == '__main__':
    lst = [random.randint(0, 9999999) for i in range(1000)]
    time1 = timeit.timeit('mystery1(lst)', globals=globals(), number = 10)
    out = mystery1(lst)
    print("mystery1(lst) output:", out)
    print("mystery1(lst) runtime:", time1, "seconds")
    print('\n------------------\n')
    time2 = timeit.timeit('mystery2("wizard.txt")', globals=globals(), number = 10)
    out = mystery2('wizard.txt')
    print("mystery2('wizard.txt') output:", out)
    print("mystery2('wizard.txt') runtime:", time2, "seconds")
    print('\n------------------\n')
    time3 = timeit.timeit('mystery3("screentime_ms.txt")', globals=globals(), number = 10)
    out = mystery3("screentime_ms.txt")
    print("mystery3('screentime_ms.txt') output:", out)
    print("mystery3('screentime_ms.txt') runtime:", time3, "seconds")
