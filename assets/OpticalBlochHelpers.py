#!/usr/bin/env python
'''
    written by: Michael Gutierrez
    date: 2015-04-06
    
    description: Helper modules to create optical bloch equations for a multi-level atom. 
                in script values are meant to agree with case A of fig 7 in the Berkeland paper
                http://journals.aps.org/pra/pdf/10.1103/PhysRevA.65.033413
    Requirements: QUTIP + dependencies, Numpy. 


'''
from __future__ import division
import numpy as np
import qutip as qp
import math 
import scipy as sp

def murelj(Jg, Je):
    '''
        #Calculates the clebsch-gordon coefficients for sigma_-, pi, sigma_+ polarized light in a Jg->Je coupled system
    '''
    
    #Generate the full range of M states for each levels
    Mg = np.arange(-Jg,Jg+1)
    Me = np.arange(-Je,Je+1)
    
    #Generate arrays for storage
    Am = np.zeros(shape=(int(2*Jg+1),int(2*Je+1)))
    A0 = np.zeros(shape=(int(2*Jg+1),int(2*Je+1)))
    Ap = np.zeros(shape=(int(2*Jg+1),int(2*Je+1)))
    #cycle through Mg states and generate clebsch-gordon coefficients
    #Note format for clebsch: clebsch(J1, Delta L (1 for dipole), J2, current m, q=(polarization -1,0,1), m + q)
    for m in enumerate(Mg):

        if abs(m[1]-1) <= Je: Am[m[0],int(np.where(Me==m[1]-1)[0])] = qp.clebsch(Jg, 1, Je, m[1], -1, m[1]-1)
        if abs(m[1])   <= Je: A0[m[0],int(np.where(Me==m[1])[0])]   = qp.clebsch(Jg, 1, Je, m[1], 0, m[1])
        if abs(m[1]+1) <= Je: Ap[m[0],int(np.where(Me==m[1]+1)[0])] = qp.clebsch(Jg, 1, Je, m[1], 1, m[1]+1)
    # return coupling matrix for each polarization
    return [Am,A0,Ap]
    
    
def Landeg(gL,gS,L,J,S):
    return gL+(gS-gL)*(J*(J+1)+S*(S+1)-L*(L+1))/(2*J*(J+1))

def Hzeeman(Bfield,jvalues,lvalues):
    '''
        Generates the zeeman hamiltonian H \propto J \cdot B
        Hat
        
        input:  Bfield:ARRAY:[Bx,By,Bz]
                Subspaces:ARRAY:[J1,J2,J3....]
    '''
    #calculate total levels
    Ntot=np.sum(2*np.array(jvalues)+1)
    muB = 2*np.pi*1.4 #Bohr magneton hbar*MHz/Gauss
    
    #Generate storage matrices
    Jz={}
    Jx={}
    Jy={}
    H = 0
    for i in enumerate(jvalues):
        Jz[i[0]]=np.zeros(shape=(Ntot,Ntot),dtype=complex)
        Jx[i[0]]=np.zeros(shape=(Ntot,Ntot),dtype=complex)
        Jy[i[0]]=np.zeros(shape=(Ntot,Ntot),dtype=complex)
        start= int(0 + np.sum(2*np.array(jvalues[0:i[0]])+1))
        end  = int(2*i[1]+1+np.sum(2*np.array(jvalues[0:i[0]])+1))
        
        Jz[i[0]][start:end,start:end] = qp.jmat(i[1],'z').full()
        Jx[i[0]][start:end,start:end] = qp.jmat(i[1],'x').full()
        Jy[i[0]][start:end,start:end] = qp.jmat(i[1],'y').full()
        
        H += muB*Landeg(1,2,lvalues[i[0]],i[1],0.5)*(Bfield[0]*Jx[i[0]] + Bfield[1]*Jy[i[0]]+Bfield[2]*Jz[i[0]])
        
    return qp.Qobj(H)
    
def CollapseOperators(jvalues,lvalues,clevels):
    '''
    
    '''
    #calculate state space size
    Ntot = int(np.sum(2*np.array(jvalues)+1))
    #Generate storage matrices
    Am={}
    A0={}
    Ap={}
    rv=[]
    for i in enumerate(clevels):
        [ Am[i[0]] , A0[i[0]], Ap[i[0]] ] = [ np.zeros(shape=(Ntot,Ntot),
                                                dtype=complex),np.zeros(shape=(Ntot,Ntot),
                                                dtype=complex),np.zeros(shape=(Ntot,Ntot),dtype=complex)
                                          ]
        start1= int(0 + np.sum(2*np.array(jvalues[0:int(i[1][0])])+1))
        end1  = int(2*jvalues[int(i[1][0])]+1+np.sum(2*np.array(jvalues[0:int(i[1][0])])+1))
        start2= int(0 + np.sum(2*np.array(jvalues[0:int(i[1][1])])+1))
        end2  = int(2*jvalues[int(i[1][1])]+1+np.sum(2*np.array(jvalues[0:int(i[1][1])])+1))

        [ Am[i[0]][start1:end1,start2:end2], A0[i[0]][start1:end1,start2:end2], Ap[i[0]][start1:end1,start2:end2] ] = murelj(jvalues[i[1][0]],jvalues[i[1][1]])
        rv.append([qp.Qobj(Am[i[0]]),qp.Qobj(A0[i[0]]),qp.Qobj(Ap[i[0]])])
        
    return rv



def Hdipole(Omega,Collapse):
    '''
    '''
    Hdipole=0
    for Omg in enumerate(Omega):
        Hdipole+=(Omg[1][0]/2.0)*Collapse[Omg[0]][0]+(Omg[1][1]/2.0)*Collapse[Omg[0]][1]+(Omg[1][2]/2.0)*Collapse[Omg[0]][2]
    return Hdipole+Hdipole.dag()


def Hatomic(proj,detunings):
    
    #set total state space size
    Hatomic = 0
    
    for i in enumerate(detunings):
        Hatomic+= detunings[i[0]]*proj[i[0]]
    
    return Hatomic
    
    
    
def LambDicke_LK(l,k,eta):
    return np.exp(-eta**2/2)*eta**(k-l)*np.sqrt(math.factorial(l)/math.factorial(k) )*sp.special.lpmv(l,k-l,eta**2)





print LambDicke_LK(0,0,0.1)
