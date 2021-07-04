def get_maze_paths_jumps(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        bres = []
        bres.append("")
        return bres
    paths=[]

    for hs in range(1,dc-sc+1):
        vpaths = get_maze_paths_jumps(sr, sc+hs, dr, dc)
        for path in vpaths:
            paths.append("h"+str(hs)+path)

    for vs in range(1,dr-sr+1):
        vpaths = get_maze_paths_jumps(sr + vs, sc, dr, dc)
        for path in vpaths:
            paths.append("v"+str(vs)+path)


    for ds in range(1,dr-sr+1):
        if ds<=dc-sc:
            dpaths = get_maze_paths_jumps(sr + ds, sc + ds, dr, dc)
            for path in dpaths:
                paths.append("d" + str(ds) + path)
    return paths

def get_maze_paths_jumps(sr, sc, dr, dc,path):
    if sr == dr and sc == dc:
        print(path)
        return
    for vs in range(1,dr-sr+1):
        get_maze_paths_jumps(sr + vs, sc, dr, dc,path+"v"+str(vs))
    for hs in range(1,dc-sc+1):
        get_maze_paths_jumps(sr, sc+hs, dr, dc,path+"h"+str(sr))
    for ds in range(1,dr-sr+1):
        if ds<=dc-sc:
            get_maze_paths_jumps(sr + ds, sc + ds, dr, dc, path + "d" + str(ds))
    return
dr = int(input("enter destination row"))
dc = int(input("enter destination column"))
print(get_maze_paths_jumps(0, 0, dr-1, dc-1))
