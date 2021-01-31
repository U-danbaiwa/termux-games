import random
red='\033[031m'
green='\033[092m'
yellow='\033[093m'
white='\033[097m'
pink='\33[95m'
lightblue='\033[096m'
logo=("* ★★★★★★★★★★★★DOCTOR GAMES★★★★★★★★★★★★★★ *")
print(logo)
print(lightblue+"*\t\t*\t==>coded<==\t *\t           *\n*\t\t  *\t\t       *",yellow+"\t\t   *\n*\t\t    *\t <°°By°°>     *\t\t           *\n*\t\t   *\t\t       *\t\t   *\n*\t\t  *",pink+" |_=_=Danbaiwa_=_|",yellow,"*\t\t   *\n*\t\t",red+" *#####################*\t\t   *")
print("************************************************************")
print("")
per=[]
print(green+"1:-List Patients")
print(pink+"2:-Add Patients")
print(red+"3:-Remove Patiens")
print(yellow+"4:-Call Patiens From List")
print(lightblue+"5:-Quit")
print(green+"6:-List Command")

for i in range(9999):
	print("")
	name=input(lightblue+"Enter Command: ")
	print("")
	if name=="2":
		for i in range(3):
			a=input(green+"Enter Partien Name: ")
			per.append(a)
			print(per)
	elif name=='1':
		if len(per)==0:
			print(yellow+"[*] No Partiens Sir")
		else:
			print(pink+"Sir These Is The Partiens\n\n",per)
	elif name=="3":
		print(pink+"[*] Whom Do You Want Remove")
		if len(per)==0:
			print("")
			print("[*] No Partiens Sir")
		else:
			print(per)
			print("")
			re=input(yellow+"Enter partien Name To Remove: ")
			per.remove(re)
			print("")
			print("")
			print(red+"Remove",pink+re+red+" Succefull ")
			print("")
			print(per)
			if len(per)==0:
				print(yellow+"[*] No Patiens Sir")
	elif name=="4":
		if len(per)==0:
			print(yellow+"[*] No Patiens Sir Press Enter ")
			print("")
		elif len(per)==0:
			print(yellow+"No Patiens Sir")
		else:
			print(yellow+"These Is Our Patiens\n\n"+green,per)
			print("")
		call=input(green+"Enter Partiens Name To Call: ")
		if call in (per):
			print("")
			print(lightblue+"Hey",pink+call,lightblue+ "Doctor Call You!!!")
			print("")
			print("===================================")
			print("")
		else:
			print("")
			print(pink+"We Don't Have This Patien Sir")
		if len(per)==0:
			print("")
		else:
			a=[": Sir i have AHSHS!!! Stomachache ",": Sir i Have Pain ",": Sir i have Toothache ",": Sir WUHH!!! i Have Flus",": Sir i Have Diebetes",": Sir AHH!!! i Have Rabies",": Sir i Have Fever ",": Sir i Have Maleria",": Sir i Have Pneumonias",]
			print(yellow+call.upper(),random.choice(a))
			print("")
			print(red+"============================================================")
			print("")
			p=("ACT LIKE REAL DOCTOR")
			print(yellow+"  ".join(p))
			print(pink+"============================================================")
			print("")
		for i in range(100):
			doc=input(green+"Doctor: ")
			if doc=="when you get it":
				po=[": Three Day Ago",": Since Last Week Sir ASHH!!!",": Now Sir ",": Morning Sir ",": Evining Sir WAAA!!! ","Just i Feel it Now",": Yesterday Sir",": Sir Annual i Feel ",": 4 Days Ago","Since Two Week sir","I Didn't Know Sir"]
				print(call,random.choice(po))
			if doc=="when":
				o=[": Three Day Ago",": Since Last Week Sir ASHH!!!",": Now Sir ",": Morning Sir ",": Evining Sir WAAA!!! ","Just i Feel it Now",": Yesterday Sir",": Sir Annual i Feel ",": 4 Days Ago","Since Two Week sir","I Didn't Know Sir"]
				print(call,random.choice(o))
			

