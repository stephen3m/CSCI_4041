def find_closest(filename):
    fp = open(filename, 'r')
    skipline = fp.readline() #skip first line
    dict = {}
    for line in fp: #store info in dictionary
        entry_name = (line.split(','))[0]
        entry_amount = float((line.split(','))[1])
        dict[entry_amount] = entry_name
    fp.close()

    sorted_amounts = sorted(dict)
    sorted_dict = {amount: dict[amount] for amount in sorted_amounts} #sorted dictionary

    arr = []
    for amount, name in sorted_dict.items(): #move dictionary information to an array
        arr.append([amount, name])

    min = abs(arr[0][0]-arr[1][0])
    ret_names = [arr[0][1], arr[1][1]]
    for i in range(len(dict)-2):
        num = abs(arr[i][0]-arr[i+1][0])
        if (num < min):
            min = num
            ret_names = [arr[i][1], arr[i+1][1]]

    return ret_names
