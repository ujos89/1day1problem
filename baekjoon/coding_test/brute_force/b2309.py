height = []
for i in range(9):
    height.append(int(input()))
height.sort()

def find_err(height):
    err = sum(height)- 100


    for i in range(len(height)):
        for j in range(i, len(height)):
            print(i,j,height[i]+height[j])
            if(height[i] + height[j] == err):
                del height[j]
                del height[i]
                return

find_err(height)
for h in height:
    print(h)