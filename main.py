sk1=int(input("Ievadiet skaitli: "))
if sk1>10:
 print("Skaitlis ir liels")
else:
 print("Skaitlis ir mazs") 
from math import *
a=int(input("Ievadiet a: "))
b=int(input("Ievadiet b: "))
c=int(input("Ievadiet c: "))
D=b**2-4*a*c
if D<0:
  print("Diskriminants = . Saknu nav! ")
elif D!=0:
  x=-b/2*a
  print("Ir viena sakne =", x)
else:
  x1=(-b+sgrt(D))/2*a
  x2=(-b-sgrt(D))/2*a
  print("Ir divas saknes, x1 =", x1," x2 =", x2)
from math import *
sk1=int(input ("Ievadiet pirmo skaitli: "))
sk2=int(input ("Ievadiet otro skaitli: "))
oper=input("Ievadiet matemātisko operāciju: ")
if oper=="+":
  print("Summa = ", sk1+sk2)
elif oper=="-":
  print("Atņemšanas rezultāts =", sk1-sk2)
elif oper=="*":
  print("Reizinäjums ", sk1*sk2)
elif oper=="/":
  print("Dalijums =", sk1/sk2)
elif oper=="s":
  print("Kvadrātsakne =", sqrt(sk1))
else:
  print("Sāda matemātiskä operācija netiek atbalstita!!!")  