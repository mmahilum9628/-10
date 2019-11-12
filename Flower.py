from MahilumFunctions2 import*

turtle.bgcolor("orange")

turtle.tracer(False)

for times in range(19):
     spike(100)

     jump(0,0)

     bob.right(19)

     spike(10)

for times in range(3):
     for times in range(30):
             spike(30-times*12)
fadingshape()
for times in range(20):
     spike3(100)
     
     bob.width(2)

     jump(times*2,times*2)

     ye()

     bob.right(190)

     bob.width(69)
 
     spike3(10)




turtle.tracer(True)
