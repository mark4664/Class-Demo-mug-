#!/usr/bin/python3

# Script name: mug_class_3.py

# Mark Bradley
# 12/12/19

# demo of a class object built to show the use of a commom tea mug
# converted to a module

class mug:
    ''' Class to describe the common Mug.
        Size is capacity in ml.
        Decoration,colour picture etc.
        State how many ml are in the mug at the moment.
        Clean, True if the mug has not been used
        Content, whats in the mug'''
    
    def __init__(self,size=350,decoration='',state=0,clean=True):
        # Initalize an instance of mug
        '''This builds the 'mug' using the default parameter unless new ones are supplied.
        '''
        self.size=size
        self.decoration=decoration
        self.state=state
        self.clean=clean
        self.content='nothing'      # Mugs have no contentat the start
        
    def fill(self,quantity,content='Tea'):
        # quantity is the amount to put in the mug. It cannot exceed the size!
        ''' fill adds a quantity in ml of the beverage specified in content to your mug
        '''
        self.content=content
        
        if quantity > (self.size - self.state):
            self.state = self.size
            return('Oh dear some of that over flowed!')
            
        else:
            self.state = quantity
            
        self.clean = False
        
    def __add__(self,quantity):   #Operator overload for '+'
        return('Sorry you cannot topup that way!')
        
    def empty(self):
        # Pour away the contents - state=0
        ''' empty the content of the mug
        '''
        self.state=0
        
    def sip(self,sip_size=30):
        # Take a sip of the drink, default is 30ml
        ''' Take a sip of your beverage, a standard sip is 30ml
            If you have drunk it all you will get an appropriate warning.
        '''
        if self.state==0:
            return('Your mug is already empty!')
        elif sip_size >= self.state:
            self.state = 0
            return('Oh dear all your '+self.content+' has gone!')
            
        else:
            self.state = self.state - sip_size
    
    def wash(self):
        ''' wash uses the built in empty function and sets clean back to true.
        '''
        self.empty()
        self.clean=True
        
    def whatsleft(self):
        # Print the current state of the mug
        ''' This function tells you about the contents of your mug.
        '''
        if self.state==0:        #state_s holds a string describing the state of the mug
            state_s = 'is empty.'
        elif self.state==self.size:
            state_s = 'is full of ' + self.content + '.'
        else:
            state_s = 'has ' + str(self.state) + 'ml of ' + self.content + ' left.'
        
        return('The ' + self.decoration + ' mug ' + state_s)
    
if __name__ == '__main__':
    
    print('Class mug test')
    #'Create an object of class mug - mymug, holds a maximun of 450ml and has a picture of a blue bird'
    mymug=mug(450,'Blue Bird')
    # Fill the mymug with 400ml of coffee
    mymug.fill(400,'Coffee')
    # Check mymug
    print(mymug.whatsleft())
    # Have a sip from my mug - default sip size is 30ml
    mymug.sip()
    print(mymug.whatsleft())
    # Have a big sip
    mymug.sip(100)
    print(mymug.whatsleft())
    mymug.sip(50)
    # Have another sip
    print(mymug.whatsleft())
    