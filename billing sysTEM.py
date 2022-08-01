class bill():
    def __init__(self):
        self.item=input('enter ITEM name using comma-  ')
        self.quan=input('enter QUANTITY of item name using comma-  ')
        self.pri=input('enter PRIZE  of each item name using comma-  ')
        
    def call(self):
        self.a=list(self.item.split(','))
        self.b=list(self.quan.split(','))
        self.c=list(self.pri.split(','))
        self.tot=[]
        for i in  range(len(self.a)):
                 self.tot.append(float(self.b[i])  * float(self.c[i]))
        print('\nS.NO * ITEM * PRICE * QUANTITY * TOTAL PRICE \n')
        print('******************************************************************************')
        print('******************************************************************************\n')    
        for i in range(len(self.a)):
            print('',i+1,' .. ',self.a[i],' \t ',self.c[i],' \t ',self.b[i],' \t ',self.tot[i])
            print('------------------------------------------------------------------------------')
        print("\nTOTAL BILL \t",sum(self.tot),'\n')
        print('******************************************************************************')
        print('******************************************************************************\n')    
            
        
class cash(bill):
    def __init__(self):
        bill.__init__(self)
    def call(self):
        bill.call(self)
        print('**PAYMENT BY CASH**')

class othr(bill):
    def __init__(self):
              self.an=input('PAYMENT BY   ........')
              bill.__init__(self)
    def call(self):
        bill.call(self)
        print('**PAYMENT BY ',self.an.upper())
        
        
class chq(bill):
    def __init__(self):
        bill.__init__(self)
        self.bank=input('enter bank name')
        self.chq= input("Please enter cheque number: ")
    def call(self):
        bill.call(self)
        print('**PAYMENT BY CHEQUE \n BANK {} \n CHEQUE NO.  {}**]'.format(self.bank,self.chq))
        
ur=input('PAYMENT WILL BE BY CASH OR CHEQUE -- ')
if ur[-1]=='h' or ur[-1]=='H' or 's' in ur or 'S' in ur or 'cash' in ur:
    obj=cash()
    obj.call()
    
elif ur[-1]=='e' or ur[-1]=='E' or 'q' in ur or 'Q' in ur or 'cheque' in ur:
    obj=chq()
    obj.call()

else:
              obj=othr()
              obj.call()
              







