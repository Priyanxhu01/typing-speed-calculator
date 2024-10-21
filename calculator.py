from time import *
import random as r

def mistake(paragraph,user):
    error = 0
    for i in range(len(paragraph)):
        # try and except use for the ignoring the error
        try:
            if paragraph[i] != user[i]:
                error += 1
        except:
           error += 1
    return error
    




def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_round = round(time_delay,2)
    speed = len(userinput)/time_round
    return round(speed)

if __name__ == "__main__":   
    while True:
        check = input("ready to test : yes / no: ")
        if check == "yes":
                test = ["A paragraph is a self-contained unit of diiscourse in writing with a particular point or idea.",
                        "my name is Priyanshu", "welcom in my leptop"]

                test1 = r.choice(test)
                print("     ***** typing speed *****   ")
                print(test1)
                print() # break one line
                print() # break one line

                time_1 = time()
                testinput = input("Enter any to else : ")
                time_2 = time()

                print("speed :" ,speed_time(time_1, time_2, testinput),"w/sec") # "w/sec" = word/second
                print("Error : ",mistake(test1,testinput))
        
        elif check == "no":
            print("Thank you ")
            break

        else:
            print("Invalid input")
