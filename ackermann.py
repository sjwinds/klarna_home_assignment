# define a function to calculate Ackermann values
from datetime import datetime

def ackermann(m,n):
    
    try:
        if m <0 or n < 0:
            return " must be greatern than 0"
    except:
            return " Input integr must be greater than 0"
    
    if m == 0:
        print(n+1)
        return (n + 1)
    elif n == 0:
        print ("ackermann(",m-1,",",1,")")
        return (ackermann(m - 1, 1))
    else:
        print ("Ackermann(",m-1,",","Ackermann(",m,",",n-1,")",")")
        return (ackermann(m - 1, ackermann(m, n - 1)))
          