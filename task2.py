import numpy as np
import scipy.integrate as spInt
import matplotlib.pyplot as pPlt

if __name__ == "__main__":
    #Create the system of ODE with the differential equation
    def System_ODE(y,t,a,b):
        #y0 is the prey, y1 is the predator
        #Set y0 and y1 equal to y
        y0, y1 = y
        #The differential equation is written as diff
        diff = [a*(y0 - y0*y1),b*(-y1 + y0*y1)]
        return diff
    
    #Function for graph plotting of ODE system solutions
    def odeintplotting(n):
        #Set the parameters as set in question
        a = 1.0
        b = 0.2
        y0 = [n,1.0]
        t = np.linspace(0, 5, 10)
        
        #The system of ODEs is solved using the scipy.integrate.odeint
        ans = spInt.odeint(System_ODE,y0,t,args=(a,b))
        
        #Graph plotting for y0 and y1 against t
        pPlt.plot(t, ans[:, 0], 'r', label='y0(t)')
        pPlt.plot(t, ans[:, 1], 'b', label='y1(t)')
        pPlt.legend(loc='best')
        pPlt.ylabel('y(t)')
        pPlt.xlabel('t')
        pPlt.grid()
        pPlt.show()
        
        #Graph plotting for y1 against y0
        pPlt.plot(ans[:, 1],ans[:,0], 'g', label='y1 against y0')
        pPlt.legend(loc='best')
        pPlt.ylabel('y1')
        pPlt.xlabel('y0')
        pPlt.grid()
        pPlt.show()
        return ans

#The solution with y0(0) equal to 0.1
odeintplotting(0.1)

#The solution with y1(0) equal to 0.11
odeintplotting(0.11)
