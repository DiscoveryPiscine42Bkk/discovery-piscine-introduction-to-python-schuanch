
for multipiler in range(11):
txt_input = input("Give me a word: ")


print(txt_input.upper())

	
	print(f"Table de {multipiler}:", end="")


	for number in range(11):
		print(f" {multipiler * number}", end="")

