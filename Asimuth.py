import math
xc = int(input('What is the X of the second point of line?'))
xb = int(input('What is the X of the first point of line?'))
delta_x = xc - xb #counting delta x 
yc = int(input('What is the Y of the second point of line?'))
yb = int(input('What is the Y of the first point of line?'))
delta_y = yc - yb #counting delta y
if delta_x > 0 and delta_y > 0:
    fi = math.atan(delta_y/delta_x) #counting value of the angle which will be used soon
    asimuth = ((fi*400)/(2*math.pi)) #changing from radians to grads as a geodesy unit
    print('The Asimuth is: ' + str(asimuth) + ' grads')
elif delta_x > 0 and delta_y < 0:
    fi = math.atan(delta_y/delta_x)
    asimuth = 200 + ((fi*400)/(2*math.pi)) #adding 200 grads what come from a position in given quarter
    print('The Asimuth is: ' + str(asimuth) + ' grads')
elif delta_x < 0 and delta_y < 0:
    fi = math.atan(delta_y/delta_x)
    asimuth = 200 + ((fi*400)/(2*math.pi))
    print('The Asimuth is: ' + str(asimuth) + ' grads')
else:
    fi = math.atan(delta_y/delta_x)
    asimuth = 400 + ((fi*400)/(2*math.pi))
    print('The Asimuth is: ' + str(asimuth) + ' grads')
    
