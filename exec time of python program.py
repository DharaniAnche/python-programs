#getting execution without modify the code using decorators
#measure execution time of any function
#independent of the number of args passed in those functions
import time
def time_measure(function):
    def inner(*args):
        starting_time=time.time()
        x=function(*args)
        ending_time=time.time()
        time_taken=ending_time-starting_time
        print(f'Execution time: {time_taken}')
        return x
    return inner
#write the functions you want and use a decorator here
@time_measure
def myfunction1(a,b):
    time.sleep(2)
    return a+b
a=myfunction1(3,6)    
print(a)