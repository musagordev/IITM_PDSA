# Huffman Coding function that accepts a string of characters without any space.
# The function should generate prefix based on frequency for each letter and generate huffman tree.

class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
    def __lt__(self,other):
        if self.frequency==other.frequency:
            return self.symbol < other.symbol
        return self.frequency < other.frequency

def Huffman(word):
    frequency={}
    for char in word:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    nodes = [Node(freq,symbol) for symbol,freq in frequency.items()]
    nodes.sort()
    
    while len(nodes)>1:
        x=nodes.pop(0)
        y=nodes.pop(0)
        
        if x < y:
            new_nodes= Node(x.frequency+y.frequency,x.symbol+y.symbol,x,y)
        else:
            new_nodes= Node(y.frequency+x.frequency,y.symbol+x.symbol,y,x)
        nodes.append(new_nodes)
        nodes.sort()
    root = nodes[0]
    huffman_codes={}
    def assign_codes(node,code=''):
        if node is not None:
            if node.symbol and len(node.symbol) == 1:
                huffman_codes[node.symbol]=code
            assign_codes(node.left,code+'0')
            assign_codes(node.right,code+'1')
    assign_codes(root)
    return huffman_codes
            
        
s = input()
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])
