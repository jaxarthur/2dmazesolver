class node:
    def __init__(self, position, parent):
        self.position = position
        self.parent = parent

def solve(maze, start, end):
    width = len(maze[0])
    height = len(maze)

    unprocessed = [node(start, None)]
    processed = []
    found = False
    while not found and len(unprocessed) > 0:
        selectednode = unprocessed[0]
        position = selectednode.position

        # check position
        if selectednode.position == end:
            return(getpath(selectednode))

        # gen new nodes
        if search(maze, (position[0] + 1, position[1]), processed, unprocessed):
            unprocessed.append(node((position[0] + 1, position[1]), selectednode))
        if search(maze, (position[0] - 1, position[1]), processed, unprocessed):
            unprocessed.append(node((position[0] - 1, position[1]), selectednode))
        if search(maze, (position[0], position[1] + 1), processed, unprocessed):
            unprocessed.append(node((position[0], position[1] + 1), selectednode))
        if search(maze, (position[0], position[1] - 1), processed, unprocessed):
            unprocessed.append(node((position[0], position[1] - 1), selectednode))

        #delete selected
        processed.append(selectednode)
        unprocessed.remove(selectednode)
    
    return None

def search(maze, position, array1, array2):

    if maze[position[1]][position[0]] == 0 and not searchlist(position, array1) and not searchlist(position, array2):
        return True
    return False

def searchlist(position, array):
    for thing in array:
        if thing.position == position:
            return True
    
    return False

def getpath(endnode):
    foundstart = False
    currentnode = endnode
    path = [currentnode.position]

    while not foundstart:
        #check if at start
        if currentnode.parent != None:
            currentnode = currentnode.parent
            path.insert(0, currentnode.position)
        else:
            foundstart = True
    
    return(path)

        