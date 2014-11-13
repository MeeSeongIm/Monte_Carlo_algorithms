

# Consider the square S with vertices (\pm 1, \pm 1) and
# consider the disk D of radius 1 centered at the origin. 
# 
# We have area(D)/area(S) = pi/4.
# In this code, we will approximate pi using a Monte Carlo algorithm:
# first, approximate area(D)/area(S) by counting the number of random points
# that land inside the unit disk over the total number of test points.
# We then multiply this number by 4 to approximate pi. 


from decimal import * 
from random import random
points = 100000
in_unit_disk = 0

for i in range(points):
    x = 2 * (random() - 0.5)
    y = 2 * (random() - 0.5)
    d = x**2 + y**2
    if d <= 1: 
        in_unit_disk = in_unit_disk + 1

Pi = Decimal(4 * in_unit_disk / points)
 
print("An approximation to Pi after %d points is: %s." % (points, Pi))






