
# Consider the cube C with vertices (\pm 1, \pm 1, \pm 1) and
# consider the unit ball B centered at the origin. 
# 
# We have area(B)/area(C) = pi/6.
# In this code, we will approximate pi using a Monte Carlo algorithm:
# first, approximate area(B)/area(C) by counting the number of random points
# that land inside the unit ball over the total number of test points.
# We then multiply this number by 6 to approximate pi. 


from decimal import * 
from random import random
points = 100000
in_unit_ball = 0

for i in range(points):
    x = 2 * (random() - 0.5)
    y = 2 * (random() - 0.5)
    z = 2 * (random() - 0.5)
    d = x**2 + y**2 + z**2
    if d <= 1: 
        in_unit_ball = in_unit_ball + 1

Pi = Decimal(6 * in_unit_ball / points)
 
print("An approximation to Pi after %d points is: %s." % (points, Pi))




