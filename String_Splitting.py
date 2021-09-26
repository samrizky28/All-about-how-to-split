#For example, a string consisting of first name, last name, and phone number 
input = "John,Martin,081122334455;Bobby,Williams,081212121212;John,Unknown,081122334455;Samuel,Thomas,081989898989"

a = input.split(";")

a2 = []
for i in a:
  a1=i.replace(","," ",1)
  a2.append(a1)

a4 = []
for j in a2:
  a3 = j.split(",")
  a4.append(a3)

a5=[]
a6=[]
print("Log:")
for k in range(len(a4)):
  y=a4[k][1]
  if y not in a5:
    a5.append(y)
    a6.append(a4[k])
    print(a4[k][0] + " - " + a4[k][1] + " : insert success")
  else:
    print(a4[k][0] + " - " + a4[k][1] + " : duplicate phone number")

print("\nPhone Book:")
a6.sort()
for l in range(len(a6)):
  print(a6[l][0] +" - "+ a6[l][1])
