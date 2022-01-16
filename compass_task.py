def direction(facing, turn):
    dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    index = (turn//45 + dirs.index(facing)) % len(dirs)

    return dirs[index]
