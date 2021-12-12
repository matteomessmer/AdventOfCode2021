file2 = [
"EG-bj",
"LN-end",
"bj-LN",
"yv-start",
"iw-ch",
"ch-LN",
"EG-bn",
"OF-iw",
"LN-yv",
"iw-TQ",
"iw-start",
"TQ-ch",
"EG-end",
"bj-OF",
"OF-end",
"TQ-start",
"TQ-bj",
"iw-LN",
"EG-ch",
"yv-iw",
"KW-bj",
"OF-ch",
"bj-ch",
"yv-TQ"
]
file3 = [
    "fs-end",
"he-DX",
"fs-he",
"start-DX",
"pj-DX",
"end-zg",
"zg-sl",
"zg-pj",
"pj-he",
"RW-he",
"fs-DX",
"pj-RW",
"zg-RW",
"start-pj",
"he-WI",
"zg-he",
"pj-fs",
"start-RW"
]
file =[
    "start-A",
"start-b",
"A-c",
"A-b",
"b-d",
"A-end",
"b-end"
]

nodes = []


for s in file2:
    nn = s.split("-")
    i1 = next((i for i, item in enumerate(nodes) if item["node"] == nn[0]), -1)
    i2 = next((i for i, item in enumerate(nodes) if item["node"] == nn[1]), -1)


    if i1 == -1:
        nodes.append({"id":len(nodes), "node": nn[0], "links":[]})
        i1 = len(nodes) - 1

    if i2 == -1:
        nodes.append({"id":len(nodes),"node": nn[1], "links":[]})
        i2 = len(nodes) - 1
    
    if i2 not in nodes[i1]["links"]:
        nodes[i1]["links"].append(i2)
    
    if i1 not in nodes[i2]["links"]:
        nodes[i2]["links"].append(i1)

print(str(nodes))

start = next((i for i, item in enumerate(nodes) if item["node"] == "start"), -1)
end = next((i for i, item in enumerate(nodes) if item["node"] == "end"), -1)

paths = []

def visit(cur_pos, p, visited_small_twice):
    global paths
    
    path = p.copy()

    if cur_pos == end:
        #print("end\n")
        #print(path)
        paths.append(path)
    else:
        for n in nodes[cur_pos]["links"]:
            if nodes[n]["node"].islower():
                if n not in path:
                    anotherpath = path.copy()
                    anotherpath.append(n)
                    visit(n, anotherpath, visited_small_twice)
                elif not visited_small_twice and path.count(n)<2 and n!=start:
                    anotherpath = path.copy()
                    anotherpath.append(n)
                    visit(n, anotherpath, True)
                
            else:
                anotherpath = path.copy()
                anotherpath.append(n)
                visit(n, anotherpath, visited_small_twice)
                

p = []
p.append(start)
visit(start, p,False)
print(str(len(paths)))