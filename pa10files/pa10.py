import traceback
import math

#huffman_encode: Takes in a single String input_string, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0s and 1s.
def huffman_encode(input_string):
    nodeList = get_NodeList(input_string) #list containings nodes, each node has information on char and char frequency 

    while(len(nodeList) > 1):
        lowNode = get_Minimum(nodeList)
        lowChar = lowNode.tuple[0]
        lowFreq = lowNode.tuple[1]

        lowNode2 = get_Minimum(nodeList)
        lowChar2 = lowNode2.tuple[0]
        lowFreq2 = lowNode2.tuple[1]

        superChar = lowChar + lowChar2
        superFreq = lowFreq + lowFreq2
        superNode = Node((superChar, superFreq))
        superNode.left = lowNode
        superNode.right = lowNode2
        nodeList.append(superNode)
    
    rootNode = nodeList[0]
    encodeDict = encode_Dict(input_string, rootNode)
    retEncodedString = ""
    for ch in input_string:
        retEncodedString += encodeDict[ch]
    return retEncodedString

# Helper function that return list of nodes, Node has member attributes binNum (0 or 1) 
# and tuple in this format: (character, character frequency) 
def get_NodeList(input_string):
    retNodeList = []
    dict = {}
    for c in input_string:
        if c in dict.keys():
            dict[c] += 1
        else:
            dict[c] = 1
    for key in dict:
        retNodeList.append(Node((key, dict[key])))
    return retNodeList

# Helper function that returns Node with minimum character frequency in list and removes it from list
def get_Minimum(input_list):
    charFrequency = math.inf
    retNode = None
    nodeIndex = 0

    for i in range(len(input_list)):
        currCharFrequency = input_list[i].tuple[1]
        if currCharFrequency <= charFrequency:
            charFrequency = currCharFrequency
            retNode = input_list[i]
            nodeIndex = i
    input_list.pop(nodeIndex)
    return retNode

# Helper function that returns dictionary with character as key and its binary encoding as value
def encode_Dict(input_string, rootNode):
    ret_dict = {}
    for ch in input_string:
        if not(ch in ret_dict.keys()):
            ret_dict[ch] = encode(ch, rootNode)
    return ret_dict

# Helper function that returns binary encoding of character given node
def encode(ch, rootNode):
    code = ""
    node = rootNode
    while (ch != node.tuple[0]):
        if (ch in node.left.tuple[0]):
            node = node.left
            code = code + "0"
        elif (ch in node.right.tuple[0]):
            node = node.right
            code = code + "1"
    return code

# Node class
class Node:
    def __init__(self, tuple):
        self.tuple = tuple #Tuple is in this format (character, character frequency)
        self.left = None #Left child node
        self.right = None #Right child node

#  DO NOT EDIT BELOW THIS LINE


if __name__ == '__main__':
    tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
             'message4.txt','message5.txt']
    correct = ['message0encoded.txt','message1encoded.txt',
               'message2encoded.txt','message3encoded.txt',
               'message4encoded.txt','message5encoded.txt']


    #Run test cases, check whether encoding correct
    count = 0

    try:
        for i in range(len(tests)):
            ("\n---------------------------------------\n")
            print("TEST #",i+1)
            print("Reading message from:",tests[i])
            fp = open(tests[i])
            message = fp.read()
            fp.close()
            print("Reading encoded message from:",correct[i])
            fp2 = open(correct[i])
            encoded = fp2.read()
            fp2.close()
            output = huffman_encode(message)
            if i < 5:
                print("Running: huffman_encode on '"+message+"'\n")
                print("Expected:",encoded,"\nGot     :",output)
            assert encoded == output, "Encoding incorrect!"
            print("Test Passed!\n")
            count += 1
    except AssertionError as e:
        print("\nFAIL: ",e)
    except Exception:
        print("\nFAIL: ",traceback.format_exc())


    print(count,"out of",len(tests),"tests passed.")


