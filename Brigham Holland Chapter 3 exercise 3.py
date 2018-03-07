#Brigham Holland - Python Chapter 4 - Exercise 7
error_msg_invalid = ('Wrong Input')
Grade = input('What is the grade?')
try:
        float(Grade)
        if float(Grade) < 0.6 :
                print ('F')
        elif float(Grade) < .7 :
                print ('D')
        elif float(Grade) < .8 :
                print ('C')
        elif float(Grade) < .9 :
                print ('B')
        elif float(Grade) < 1 :
                print ('A')
        else : 
                print (error_msg_invalid)
                Grade = raw_input('What is the grade?')
except: 
	print (error_msg_invalid)


