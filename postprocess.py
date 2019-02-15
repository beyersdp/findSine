'''
Iterate throw all directorys of all participants
    - Iterate over all trys of each participant
        - Iterate over x and y over ech participant
            - For x show function and eqs x3
            - For y show function and eqs x3
        - Add eqs form all x and y
        - Add eqs for xi i={1,2,3} and yi i={1,2,3}
    - Add eqs from all trys for x and y
    - Add eqs from all trys for xi i={1,2,3} and yi i={1,2,3}
Add eqs from all participants from all trys for x and y
Add eps form all participants from all trys for xi and yi i={1,2,3}

Compute for each sum the mean
'''

import sys


p_start = int(input("Enter starting p: "))
p_end   = int(input("Enter ending   p: "))
p_num   = p_end - p_start + 1
data_path = "./data/"
res_file  = input("Enter filepath for saving the results: ")

sys.stdout = open(res_file, "w")

xtotal_sum = 0
xitotal_sum = dict()

ytotal_sum = 0
yitotal_sum = dict()

while p_start <= p_end:
    
    xi_sum = dict()
    xp_sum = 0

    yi_sum = dict()
    yp_sum = 0

    # Iterate over Trys
    for t in range(1,4): #DEBUG, sonst 1,8

        x_sum  = 0
        y_sum  = 0

        print("\n[P{}][T{}][ X ] Matching Sine Functions:".format(p_start,t))
        # Iterate over X
        for x in range(1,4):
            with open(data_path + "p" + str(p_start) + "/t" + str(t) + "/x/" + str(x) + "res.txt") as res:
                for line in res:
                    print("[P{}][T{}][X={}] ".format(p_start, t, x) + line[:-1])

                    if line[0] != 'y':
                        x_sum += float(line)
                        xp_sum += float(line)
                        xtotal_sum += float(line)

                        if "x{0}_sum".format(str(x)) in xi_sum:
                            xi_sum["x{0}_sum".format(str(x))] += float(line)
                        else:
                            xi_sum["x{0}_sum".format(str(x))] = float(line)

                        if "x{0}_sum".format(str(x)) in xitotal_sum:
                            xitotal_sum["x{0}_sum".format(str(x))] += float(line) 
                        else:
                            xitotal_sum["x{0}_sum".format(str(x))] = float(line) 

    
        print("[P{}][T{}][ X ] Mean(x)  = {}".format(p_start,t, x_sum / 3))

        print("\n[P{}][T{}][ Y ] Matching Cosine Functions:".format(p_start,t))
        # Iterate over Y
        for y in range(1,4):
            with open(data_path + "p" + str(p_start) + "/t" + str(t) + "/y/" + str(y) + "res.txt") as res:
                for line in res:
                    print("[P{}][T{}][Y={}] ".format(p_start, t, y) + line[:-1])
                    
                    if line[0] != 'y':
                        y_sum += float(line)
                        yp_sum += float(line)
                        ytotal_sum += float(line)

                        if "y{0}_sum".format(str(y)) in yi_sum:
                            yi_sum["y{0}_sum".format(str(y))] += float(line)
                        else:
                            yi_sum["y{0}_sum".format(str(y))] = float(line)
                        
                        if "y{0}_sum".format(str(y)) in yitotal_sum:
                            yitotal_sum["y{0}_sum".format(str(y))] += float(line) 
                        else:
                            yitotal_sum["y{0}_sum".format(str(y))] = float(line) 
        
        print("[P{}][T{}][ Y ] Mean(x) = {}".format(p_start,t, y_sum / 3))


    print("")
    for (kx, vx), (ky, vy) in zip(xi_sum.items(), yi_sum.items()):
        print("[P{}]          Mean({}) = {}".format(p_start, kx, vx / 3)) #DEBUG sonst vx / 7
        print("[P{}]          Mean({}) = {}".format(p_start, ky, vy / 3)) #DEBUG sonst vx / 7
    
    print("[P{}]          Mean(x) = {}".format(p_start, xp_sum / 3)) #DEBUG sonst / 7
    print("[P{}]          Mean(y) = {}".format(p_start, yp_sum / 3)) #DEBUG sonst / 7
    
    p_start += 1


print("")
for (kx, vx), (ky, vy) in zip(xitotal_sum.items(), yitotal_sum.items()):
    print("[]            Mean({}) = {}".format(kx, vx / p_num)) #DEBUG sonst vx / 31
    print("[]            Mean({}) = {}".format(ky, vy / p_num)) #DEBUG sonst vx / 31

print("[]            Mean(x) = {}".format(xtotal_sum / p_num)) 
print("[]            Mean(y) = {}".format(ytotal_sum / p_num))

res.close()
