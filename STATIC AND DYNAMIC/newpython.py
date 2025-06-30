

#recursion uniques in python
import sys 
sys.setrecursionlimit(100)
def vignan():
    global i
    i+=1 
    print(i)
    vignan()
i=0
vignan()