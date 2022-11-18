import time 
def countdown(n):
    if n==0:
        print ("time up!")
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)
n=int(input ("enter a limit"))
countdown(n)