cred={'OE':3,'Chem':4,'CSEN':3,'English':2,'Discrete Math':2,'Graph Theory':2,'EVPR':2,'VDC':1}
lookup={'O':10,'A*':9,'A':8,'B*':7,'B':6}
TGP=0
T_cred=19
for i in cred:
  grad_in=input(f"Enter your Grade for {i} : ")
  GP=lookup[grad_in]*cred[i]
  TGP+=GP
print("=-=-=-=-=-=-=-=-=-=-=-=")
print(f"GPA={TGP/19}")