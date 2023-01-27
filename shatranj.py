def shatranji ():
    soton=int(input("enter num of soton:"))
    radif=int(input("enter num of radif"))
    matrix=[]
    for k in range (soton):
        m=[]
        n=[]
        for j in range (radif):
            m.append("#")
            m.append("*")
            n.append("#")
            n.append("*")
        matrix.append(m)
        matrix.append(n)

    for k in range (soton):
        for j in range (radif):
            print(matrix[k][j], end="") 
        print()
shatranji()

        