'''
-------------------------------------------------------------------------
|	Project			: findSine											|
|	Program name	: automatic.py										|
|	Author			: P. Beyersdorffer									|
|	Date created	: 14.02.2019 (09:25:07)       						|
|	Purpose			: Execute the workflow automatically				|
|	Dependencies    : findSineMain, preprocessARGS.py					|
-------------------------------------------------------------------------
'''

import os


# set range by user input (which participants should by analized?)
p_start = int(input("[AUTO][INIT] Enter the number of the participant for starting: "))
p_stop = int(input("[AUTO][INIT] Enter the number of the participant for stopping: "))



while p_start < p_stop:
    print("[AUTO][INIT] Start process for participant {}".format(p_start))

    for i in range(1,7):     
        command_preprocess = "python3 preprocessARGS.py"
        command_preprocess_a1 = " ./data/p" + str(p_start) + "/t" + str(i) + "/x.txt"
        command_preprocess_a2 = " ./data/p" + str(p_start) + "/t" + str(i) + "/z.txt"
        command_preprocess_a3 = " ./data/p" + str(p_start) + "/t" + str(i) + "/x/"

        os.system(command_preprocess + command_preprocess_a1 + command_preprocess_a2 + command_preprocess_a3)

        for j in range(1,3):
            command_findSineMain = "./findSineMain"
            command_findSineMain_a1 = " ./data/p" + str(p_start) + "/t" + str(i) + "/x/" + str(j) + ".txt"
            command_findSineMain_a2 = " ./data/p" + str(p_start) + "/t" + str(i) + "/x/" + str(j) + "sine.txt"
            command_findSineMain_a3 = " ./data/p" + str(p_start) + "/t" + str(i) + "/x/" + str(j) + "res.txt"
            command_findSineMain_a4 = " sin"

            os.system(command_findSineMain+command_findSineMain_a1+command_findSineMain_a2+command_findSineMain_a3+command_findSineMain_a4) 

        command_preprocess = "python3 preprocessARGS.py"
        command_preprocess_a1 = " ./data/p" + str(p_start) + "/t" + str(i) + "/y.txt"
        command_preprocess_a2 = " ./data/p" + str(p_start) + "/t" + str(i) + "/z.txt"
        command_preprocess_a3 = " ./data/p" + str(p_start) + "/t" + str(i) + "/y/"
    
        os.system(command_preprocess + command_preprocess_a1 + command_preprocess_a2 + command_preprocess_a3)
        
        for k in range(1,3):
            command_findSineMain = "./findSineMain"
            command_findSineMain_a1 = " ./data/p" + str(p_start) + "/t" + str(i) + "/y/" + str(k) + ".txt"
            command_findSineMain_a2 = " ./data/p" + str(p_start) + "/t" + str(i) + "/y/" + str(k) + "sine.txt"
            command_findSineMain_a3 = " ./data/p" + str(p_start) + "/t" + str(i) + "/y/" + str(k) + "res.txt"
            command_findSineMain_a4 = " cos"

            os.system(command_findSineMain+command_findSineMain_a1+command_findSineMain_a2+command_findSineMain_a3+command_findSineMain_a4)  

    p_start += 1

print("[AUTO][INIT] Process finished")
