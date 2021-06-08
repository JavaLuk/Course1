loz = input("Unesi pravu lozinku: ")
rec = input("Unesi lozinku(proba): ")

while True:
	if rec.upper()==loz.upper():
		break
	else:
		rec = input("Unesi lozinku(proba): ")
print("Nice!")