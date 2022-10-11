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