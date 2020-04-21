alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
codestring="JMBCYEKLFDGUVWHINXRTOSPZQA"
plaintext="Ab3c, De1::6"
## encode and decode functions using string operations
def encode_string(codestring, plaintext):
	ciphertext= ""
	for char in plaintext:
		char = char.upper()
		if char in codestring:
			ciphertext = ciphertext + codestring[alphabet.index(char)]
		elif char == " ":
		 	ciphertext = ciphertext + "-"
		else:
			ciphertext= ciphertext + char
	return ciphertext

def decode_string(codestring, ciphertext):
	plaintext = ""
	for	char in	ciphertext:
		char=char.upper()
		if char in codestring:
			plaintext = plaintext + alphabet[codestring.index(char)]
		elif char == "-":
			plaintext = plaintext + " "
		else:
			plaintext = plaintext + char
	return plaintext
def create_elist(codestring):
	e_list=[]
	for char in codestring:
		e_list.append(char)
	return e_list
def create_dlist(codestring):
	d_list=[alphabet[codestring.index(char)] for char in alphabet if char in codestring]
	return d_list

def encode_list(e_list, plaintext):
	ciphertext = []
	for char in plaintext:
		char=char.upper()
		if char in e_list:
			ciphertext.append(e_list[alphabet.index(char)])
		elif char == " ":
			ciphertext.append("-")
		else:
			ciphertext.append(char)
	cipherstring= "".join(ciphertext)
	return cipherstring
def decode_list(d_list, ciphertext):
	plaintext = []
	for	char in	ciphertext:
		char=char.upper()
		if char in alphabet:
			plaintext.append(d_list[alphabet.index(char)])
		elif char == "-":
			plaintext.append(" ")
		else:
			plaintext.append(char)
	plainstring = "".join(plaintext)
	return plainstring
def create_edict(codestring):
	e_dict={}
	for char in codestring:
		e_dict[alphabet[codestring.index(char)]] = char
	return(e_dict)
def create_ddict(codestring):
	d_dict = {}
	for char in codestring:
		d_dict[char] = alphabet[codestring.index(char)]
	return(d_dict)
def encode_dictionary(e_dict, plaintext):
	ciphertext = ""
	plaintext = plaintext.upper()
	for char in plaintext:
		if char is " ":
			ciphertext = ciphertext + "-"
		elif char in e_dict:
			ciphertext = ciphertext + e_dict[char]
		else:
			ciphertext = ciphertext + char
	return(ciphertext)
def decode_dictionary(d_dict, ciphertext):
	plaintext = ""
	ciphertext = ciphertext.upper()
	for char in ciphertext:
		if char in d_dict:
			plaintext = plaintext + d_dict[char]
		elif char is "-":
			plaintext = plaintext + " "
		else:
			plaintext = plaintext + char
	return(plaintext)
