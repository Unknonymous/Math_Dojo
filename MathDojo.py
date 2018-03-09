# Create a Python class called MathDojo...
class MathDojo(object):
    def __init__(self):
        self.totx = 0

    # that has the methods add and subtract. #
    # Have these 2 functions take at least 1 parameter.
    def add(self, *args):
        for a in args:
            if type(a) == int or type(a) == float:
                self.totx += a  
            if type(a) == list or type(a) == tuple:
                for item in a:
                    self.totx += item
        return self
    
    def subtract(self, *args):
        neg = 0
        for s in args:
            if type(s) == int or type(s) == float:
                neg += s
            if type(s) == list or type(s) == tuple:
                for item in s:
                    neg += item
        self.totx -= neg
        return self

    def result(self):
        print ('The Result is : '+ str(self.totx))
        return self.totx
            

# Then create a new instance called md.             
md = MathDojo()

# It should be able to do the following task:  
#md.add(2).add([2,5]).result()
# which should perform 0+2+(2+5)-(3+2) and return 4.

#Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. 
# It should now be able to perform the following tasks:
#md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
#should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result: 28.15

#Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
md.add(1, [2], (3,)).add(1, 2, [3, 4], (5, 6)).subtract(1, [1], (1,)).subtract(1, 1, [1, 1], (1, 1)).result()
#This combination of singletons, lists, and tuples should produce a result of 18