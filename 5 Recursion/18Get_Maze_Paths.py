def get_maze_paths(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        return [""]
    else:
        if sr>dr or sc>dc:
            return []

    hpath=get_maze_paths(sr+1, sc, dr, dc)
    vpath=get_maze_paths(sr, sc+1, dr, dc)
    paths = []
    for path in hpath:
        paths.append("h" + path)

    for path in vpath:
        paths.append("v" + path)
    return paths

def get_maze_paths(sr, sc, dr, dc, path):
    if sr == dr and sc == dc:
        print(path)
        return
    if sr+1 <= dr:
        get_maze_paths(sr + 1, sc, dr, dc,path+"v")
    if sc+1 <= dc:
        get_maze_paths(sr, sc + 1, dr, dc,path+"h")
    return
dr = int(input("enter destination row"))
dc = int(input("enter destination column"))
print(get_maze_paths(1, 1, dr, dc))
