'''
@author : Jayad Pathan
@goal : 
    a) accept mass of two objects in Kgs, distance
    between them in meters
    b) do a validation check 
    c) compute gravitational force of attraction 
    d) print the result
'''

import sys

def main() -> None:
    '''
    @input: None
    @output: None
    @goal: a driver function of application
    '''
    m1 = float(input("Enter mass of ojbect 1 in kgs:"))
    m2 = float(input("Enter mass of object 2 in kgs:"))
    r = float(input("Enter the distance between in the objects in meters:"))
    try:
        F = computeGravitationalForce(m1, m2, r)
    except:
        exc_name, exc_data, exc_tb = sys.exc_info()
        print(exc_name.__name__, exc_data, sep=":")
        sys.exit(-1)
    print(f"Force of attraction if:{F} Newton")
    sys.exit(-1)

main()