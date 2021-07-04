def logarithmic_product(n,pow):
    if pow==0:
        return 1
    halftot=logarithmic_product(n,int(pow/2))
    total=halftot*halftot
    if pow%2==1:
        total=total*n

    return total    # if we print directly fact here it is giving error but if we are returning fact it is working fine

pow=int(input("enter the power"))
print(logarithmic_product(10,pow))