def user_input():
    p=int(input("Enter number of processes: "))
    r=int(input("Enter number of resources: "))

    alloc=[]
    max=[]
    avail=[]
    for i in range(p):
        temp1=[]
        temp2=[]
        for j in range(r):
            x=int(input(f"Enter resource {j+1} allocated for process {i+1}: "))
            y=int(input(f"Enter resource {j+1} max for process {i+1}: "))
            temp1.append(x)
            temp2.append(y)
        alloc.append(temp1)
        max.append(temp2)
        

    for i in range(r):
        avail.append(int(input(f"Enter available resource {i+1}: ")))
    return alloc,max,avail,p,r
def bankersAlgorithm(alloc,max,avail,p,r):
    f = [0]*p
    ans = [0]*p
    ind = 0
    for k in range(p):
        f[k]=0
    need= [[ 0 for i in range(r)]for i in range(p)]
    for i in range(p):
        for j in range(r):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0
    for k in range(p):
        for i in range(p):
            if (f[i] == 0):
                flag = 0
                for j in range(r):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break
                if (flag == 0):
                    ans [ind] = i
                    ind += 1
                    for y in range(r):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    if(ind==p):
        
        print("Following is the SAFE Sequence")
        for i in range(p - 1):
            print("P", ans[i], "->", sep="", end="")
        print("P", ans[p-1], sep="")
    else:
        print("deadlock detected no safe sequence")

def main():
    choice=input("User Inputs(Y/n)")
    if(choice=='y'or choice=='Y'):
        alloc,max,avail,p,r=user_input()
    else :
        alloc= [[1, 0, 2, 1],
                [0, 1, 1, 0],
                [1, 1, 0, 1]]
        max= [[2, 2, 3, 2],
                [1, 2, 2, 1],
                [2, 2, 1, 2]]
        avail=[1, 2, 1, 1]
        p=3
        r=4
    bankersAlgorithm(alloc,max,avail,p,r)
    
    

if __name__ == "__main__":
    main()