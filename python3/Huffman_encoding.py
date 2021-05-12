class node:
    def __init__(self, freq, char, left=None, right=None):
        # creating node
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huff = ""


class huffman:
    def __init__(self, charlist=None, freqlist=None, text=None):
        # haffman operation tarminal
        if charlist is None:
            if freqlist is None:
                if text is None:
                    raise Exception("Error !! No parameter found.")

        if text:
            charlist = list(set(list(text)))
            freqlist = [text.count(x) for x in charlist]

        tree = self.encoding(charlist, freqlist)
        self.display(tree)
        
        # total time complexity : O(nlogn)

    @staticmethod
    def encoding(charlist, freqlist):

        # creating empty list to store nodes
        mynodes = []

        # creating node containing freq and char and pusing into list
        for i in range(len(charlist)):
            mynodes.append(node(freqlist[i], charlist[i]))

        # running while to create a tree out of leaf nodes

        while len(mynodes) > 1:
            # sorting node followed by frequency 
            # time complexity O(n) 
            mynodes=sorted(mynodes,key=lambda x: x.freq)
            # getting node with minimal frequency
            left = mynodes[0]
            right=mynodes[1]
            
            # removing node with minimal frequency
            mynodes.remove(left)
            mynodes.remove(right)

            # setting left & right pathcodes
            left.huff = 0
            right.huff = 1

            # creating and pushing new parent node of tree
            # merging left and right child nodes
            newnode = node(left.freq + right.freq, left.char + right.char, left, right)
            mynodes.append(newnode)

        # now tree is created
        # tree is the first node of mynode list
        return mynodes[0]

    def display(self, thisnode, val=""):
        # using recurssion method to encode tree
        # visualizing the tree and printing encoded values
        global ans
        # storing the pathcodes as encoded value in newval
        newval = val + str(thisnode.huff)

        if thisnode.left:
            self.display(thisnode.left, newval)

        if thisnode.right:
            self.display(thisnode.right, newval)

        if not thisnode.left and not thisnode.right:
            print(thisnode.char, ":", newval)
            ans[thisnode.char]=newval


# ..............................................

# two option to launching huffman encoder
# 1. proving character list and there frequency list
# 2. providing the raw text message
# dis: only one way at a time.
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [40, 30, 20, 5, 3, 2]
ans={}
mytext = "aaaasssddfgggghhhjjk ll"

huffman(chars, freq)
# huffman(text=mytext)
# print(ans)
