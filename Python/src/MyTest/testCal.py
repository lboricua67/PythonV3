#!/usr/bin/env python3

def Calcpay(e):
    l= e["lname"]
    f= e["fname"]
    a= e["age"]
    h= e["hours"]
    p= e["rate"]

    print("\n==============================\n")
    print("Your last name         ==> ", l)
    print("Your first name        ==> ", f)
    print("Employee age           ==> ", a)
    print("Enter the hours worked ==> ", h)
    print("Enter the pay rate     ==> ", p)

    if h <= 40:
       payment=(h*p)
    else:
       payment=((p*40)+((h-40)*(p*1.5)))
    payment="${:,.2f}".format(payment)
    name=f + " " + l
    print("Weekly Pay for: ", name, " is: ", payment)

def main():
    print("==============================")
    print("Payroll App")
    print("==============================\n")

    employee={}
    l=str(input("Employee Last Name......: "))
    f=str(input("Employee First Name.....: "))
    a=int(input("Employee Age............: "))
    h=int(input("Employee Hours worked...: "))
    p=float(input("Employee Hourly rate....: "))

    employee["lname"]=l
    employee["fname"]=f
    employee["age"]=a
    employee["hours"]=h
    employee["rate"]=p

    Calcpay(employee)


if __name__ == '__main__': main()
