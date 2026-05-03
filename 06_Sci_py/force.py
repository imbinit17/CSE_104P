from scipy.constants import G , epsilon_0 , pi

def gravitational_force(m1:float,m2:float,r:float)->float:
    if r<=0 or m1<=0 or m2<=0:
        print('Distance and masses should be positive')
        return 0
    return G * m1 * m2 / r**2

def electrostatic_force(q1:float,q2:float,r:float)->float:
    if r<=0:
        print('Distance should be greater than zero')
        return 0
    return 1/(4*pi*epsilon_0) * q1 * q2 / r**2
