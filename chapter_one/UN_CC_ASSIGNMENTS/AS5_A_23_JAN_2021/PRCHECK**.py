jane=int(input())

if jane==1 :
	print("0")

elif jane==2 or jane==3:
	print("1")

elif jane%2==0 or jane%3==0:
	print(0)

else:
	clara=5
	t=1
	while clara*clara<jane:
		if jane%clara==0 or jane%(clara+2)==0:
			print(0)
			quit()
		clara+=6
	print(1)
