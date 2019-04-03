

tree = [1,2,3,3,3,2,5,4,5,3,4]


def main(self, tree):
    res = [] 
    print("start")
    amount = 0
    i = 0
    j = 1
    while tree[i] == tree[j]:
        i += 1
        j += 1
    t1 = tree[i]
    t2 = tree[j]
    length = len(tree)
    for t in range(length-1):
        if tree[t] == t1 or tree[t] == t2:
            amount += 1
            continue
        elif tree[t] != t1 and tree[t] != t2:
            res.append(amount)
            amount = 2
            t1 = tree[t]
            t2 = tree[t-1]
            continue
    print( max(res))

