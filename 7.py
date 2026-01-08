alphabet = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

def caesar(start_text, shift_amount, direction):
    output_text = ""
    shift_amount %= len(alphabet)

    for letter in start_text:
        if letter not in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter)
            
            if direction == "encode":
                new_position = position + shift_amount
            else:  # decode
                new_position = position - shift_amount
            
            output_text += alphabet[new_position % len(alphabet)]

    print(f"Here is the {direction}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, direction=direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if choice == "no":
        should_continue = False
        print("Goodbye 👋")
'''
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\.git\7.py"
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello fasi 
Type the shift number:
3
Here is the encoded result: khoor idvl
Type 'yes' if you want to go again. Otherwise type 'no':
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor idvl
Type the shift number:
3
Here is the decoded result: hello fasi
Type 'yes' if you want to go again. Otherwise type 'no':
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
fasi@12 3
Type the shift number:
2
Here is the encoded result: hcuk@12 3
Type 'yes' if you want to go again. Otherwise type 'no':
yes 
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
hcuk@12 3
Type the shift number:
2
Here is the decoded result: fasi@12 3
Type 'yes' if you want to go again. Otherwise type 'no':
no
Goodbye 👋
'''