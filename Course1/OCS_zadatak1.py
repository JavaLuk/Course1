lista = []
sana = input("sana: ")

def for_loop():
	for x in lista:
		if x==sana:
			return 1
	lista.append(sana)
	return 0 

while True:
	if for_loop()==1:
		break
	else:
		sana = input("sana: ")

print("len:: ", len(lista))
print(lista)