octops = [[5,4,2,1,4,5,1,7,4,1 ],
[3,8,7,7,3,2,1,5,6,8 ],
[7,5,8,3,2,7,3,8,6,4 ],
[3,4,5,1,7,1,7,7,7,8 ],
[2,6,5,1,6,1,5,1,5,6 ],
[6,3,7,7,1,6,7,5,2,6 ],
[5,1,8,2,8,5,2,8,3,1 ],
[4,7,6,6,8,5,6,6,7,6 ],
[3,4,3,7,1,8,7,5,8,3 ],
[3,6,3,3,3,7,1,5,8,6]]

octops = [
[5,4,8,3,1,4,3,2,2,3],
[2,7,4,5,8,5,4,7,1,1],
[5,2,6,4,5,5,6,1,7,3],
[6,1,4,1,3,3,6,1,4,6],
[6,3,5,7,3,8,5,4,7,8],
[4,1,6,7,5,2,4,6,4,5],
[2,1,7,6,8,4,1,7,2,1],
[6,8,8,2,8,8,1,1,3,4],
[4,8,4,6,8,4,8,5,5,4],
[5,2,8,3,7,5,1,5,2,6]]

step = 0


def incNeigh(r,c):
    global octops
    if r -1 >= 0:
        if c-1>=0:
            if octops[r-1][c-1] <=9:
                octops[r-1][c-1] = octops[r-1][c-1] + 1
                if octops[r-1][c-1] > 9:
                    incNeigh(r-1, c-1)
        if octops[r-1][c] <=9:
            octops[r-1][c] = octops[r-1][c] + 1
            if octops[r-1][c] > 9:
                incNeigh(r-1, c)
        if c+1<len(octops[r]):
            if octops[r-1][c+1] <=9:
                octops[r-1][c+1] = octops[r-1][c+1] + 1
                if octops[r-1][c+1] > 9:
                    incNeigh(r-1, c+1)

    if c-1>=0:
        if octops[r][c-1] <=9:
            octops[r][c-1] = octops[r][c-1] + 1
            if octops[r][c-1] > 9:
                incNeigh(r, c-1)
    
    if c+1<len(octops[r]):
        if octops[r][c+1] <=9:
            octops[r][c+1] = octops[r][c+1] + 1
            if octops[r][c+1] > 9:
                incNeigh(r, c+1)
    
    if r +1 < len(octops):
        if c-1>=0:
            if octops[r+1][c-1] <=9:
                octops[r+1][c-1] = octops[r+1][c-1] + 1
                if octops[r+1][c-1] > 9:
                    incNeigh(r+1, c-1)
        if octops[r+1][c] <=9:
            octops[r+1][c] = octops[r+1][c] + 1
            if octops[r+1][c] > 9:
                incNeigh(r+1, c)
        if c+1<len(octops[r]):
            if octops[r+1][c+1] <=9:
                octops[r+1][c+1] = octops[r+1][c+1] + 1
                if octops[r+1][c+1] > 9:
                    incNeigh(r+1, c+1)


flash =0
for step in range(2):
    for r in range(len(octops)):
        for c in range(len(octops[r])):
            octops[r][c] = octops[r][c] + 1
            if octops[r][c] > 9:
                incNeigh(r,c)
    for r in range(len(octops)):
        for c in range(len(octops[r])):
            if octops[r][c] > 9:
                octops[r][c] = 0
                flash = flash + 1

print(str(flash))

print(str(octops))
