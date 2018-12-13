def pow(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*pow(base,exp-1))
base=int(input(" "))
exp=int(input(" "))
print(pow(base,exp))
