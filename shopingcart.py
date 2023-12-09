class item:
    def __init__(self,prod,pri):
        self.prod=prod
        self.price=pri
    

class shoppingcart:
    sum=0
    cart=[]
 

    def adcart(self,itom):
    
         for k in objects:
                  if k==itom:
                      self.sum+=((objects[k]).price)
                      self.cart.append(k)
                      print('added successfully')


    def total(self):
        print("total :",self.sum)

    def length(self):
        print("length of cart :",len(self.cart))
        
        

                      
                      
                  
              

                
              

           
n_items=int(input('entrer items'))
l=[]
objects=dict()
operations=[]
obj=shoppingcart()

for i in range(n_items):
    k=list(input('').split())
    l.append(k)
# print(l) items selected   
for i in l:
    itm,price=i
    k=itm
    itm=item(itm,int(price))
    objects[k]=itm
n_ops=int(input(''))
for i in range(n_ops):
    z=list(input('').split())
    operations.append(z)
# print(operations) operations to be performed in cart

for i in operations:
    if i[0]=='add':
        arg=i[1]
        obj.adcart(arg)

        
    elif i==['total'] :
                 obj.total()
    elif i==['len']:
                 obj.length()


         
        
    
    





        
        
        
    
