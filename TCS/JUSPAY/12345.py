def spiral(n,m,l):
    top=0
    bottom=m-1
    left=0
    right=n-1
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            print(l[top][i],end=" ")
        top+=1
        for i in range(top,bottom+1):
            print(l[i][right],end=" ")
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(l[bottom][i],end=" ")
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(l[i][left],end=" ")
            left+=1

if __name__=="__main__":
    #matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
    # Function call to print matrix elements in spiral order
    #spiral(len(matrix), len(matrix[0]), matrix)
    t=int(input())
    for _ in range(t):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        matrix = []
        print("Enter the entries rowwise:")
        for i in range(rows):
            a =[]
            for j in range(cols):
                a.append(int(input()))
            matrix.append(a)
        spiral(len(matrix),len(matrix[0]),matrix)