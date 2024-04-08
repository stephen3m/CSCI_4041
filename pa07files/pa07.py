#Folder and File classes
#Do not edit the __init__ method for either class
#Feel free to add your own methods, though
class Folder:
    def __init__(self, name, files, subfolders):
        self.name = name
        self.files = files
        self.subfolders = subfolders

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def total_memory(root):
    folder_tot_mem = 0
    for i in range(len(root.files)):
        folder_tot_mem += (root.files)[i].size
    for i in range(len(root.subfolders)):
        folder_tot_mem += total_memory((root.subfolders)[i])
    return folder_tot_mem  

def search(root, target):
    subfolders = root.subfolders
    subfiles = root.files
    file_name = root.name

    for i in range(len(subfiles)):
        if ((subfiles)[i].name == target):
            return file_name + "/" + target
    for i in range(len(subfolders)):
        if (search(subfolders[i], target) != False):
            return file_name + "/" + search(subfolders[i], target) 

    return False


if __name__ == '__main__':
    root1 = Folder('courses',[File('CSCI_1133', 205),
                              File('CSCI_3041', 7)], [])

    root2 = Folder('empty',[], [])

    root3 = Folder('root', [File('resume.txt',607),
                File('cat.jpg',607)],
               [Folder('hws', [], []),
                Folder('plans',
                       [File('vacation.txt', 636)],
                       [Folder('evil',
                               [File('world_domination.txt',766)], [])]
                      ),
                Folder('labs',[File('lab1.txt',223),
                               File('lab2.txt',251),
                               File('lab3.txt',317)], [])])


    

