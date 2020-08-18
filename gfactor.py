v=float(input("Enter your relative velocity in m/s :"))
c=3*(10**8)
csqr=c*c
vsqr=v*v
gfactor=1/((1-(vsqr/csqr))**.5)
print("Gamma Factor = ", gfactor)
