txt = input("Enter a word or phrase: ")
initial_txt = txt
txt_valid = False
isPal = True
characters = [',', "'", '"', '.','?',';',':','!','-']

while not txt_valid:
    txt = txt.strip()
    txt = txt.replace(' ', '')
    txt = txt.lower()

    for ch in txt:
        if ch in characters:
            txt = txt.replace(ch, '')

    if txt.isalpha():
        txt_valid = True
    else:
        txt = input("Only enter letters: ")
        initial_txt = txt

for char in range(len(txt)):
    if txt[char] == txt[-(char + 1)]:
        continue
    else:
        isPal = False
        break

if isPal:
    if len(initial_txt.split()) <= 1:
        print(f"{txt.upper()} is a palindrome!")
    else:
        print(f"{initial_txt} is a palindrome!")
else:
    print(f"{txt.capitalize()} is not a palindrome.")