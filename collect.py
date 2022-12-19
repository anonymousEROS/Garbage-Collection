import re #Regular Expressions

# Jaidan Dovala
# C3400
# 23 April 2022
# Collect.py
# Mark and Sweep program 

# Function takes in a filename
def collect(filename):
    nodesptr, node = [], {}
    with open(filename) as file:
        n = 0
        for line in file:
            # grabs num of nodes in the first line
            if n == 0:
                n = int(line)
            else:
                splitLine = line.rstrip()
                splitLine = re.split(r'[,]', splitLine)
                nodesptr.append([splitLine[0], splitLine[1]])
        count = 0
        while count < n:
            node[str(count)] = [0, 0]
            count += 1
        for item in nodesptr:
            if not is_int(item[0]):
                node_trace(item, nodesptr, node) 
    return node
    
# Determines if given string contains an integer value
def is_int(s):
    try:
        return int(s)
    except ValueError:
        return False
    
#recursive function that traces through a mem-node structure
def node_trace(pointer, nodesptr, nodes):
    if is_int(pointer[0]):
        if nodes[pointer[0]][1] == 1:
            return
        else:
            #checks the current node as marked and traversed
            nodes[pointer[0]][0] = 1
            nodes[pointer[0]][1] = 1
    for x in nodesptr:
        #repeats for each node the current node points to
        if x[0] == pointer[1] and nodes[x[0]][1] == 0:
            node_trace(x, nodesptr, nodes)
        #catches the node at the end of a chain
        if is_int(x[0]):
            if nodes[x[0]][1] == 1:
                nodes[x[1]][0] = 1
                nodes[x[1]][1] = 1
        else:
            #catches a single link chain 
            nodes[x[1]][0] = 1
            nodes[x[1]][1] = 1
            

#    prints marked nodes if value = 1
#    prints reclaimed nodes if value = 0           
def printCol(message, value, nodes):
    print(message)
    for item in sorted(nodes.items()):
        if item[1][1] == value:
            print(item[0])

def main():
    
    ## Define filename 
    filename = input("Type the name of file or hit Enter to accept default:")
    if filename == '':
        filename = 'sample.txt'# Set a default name if none provided'

    
    n = collect(filename)
   
    printCol('\nMarked \n-------', 1, n)
    printCol('\nReclaimed \n---------- ', 0, n)
    

if __name__ == "__main__":
    main()
