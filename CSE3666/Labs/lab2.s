#	CSE3666 Lab 2

	.data		#data segment

        # The next variable (symbol) should starts at an address that is a multiple of 4.
        # define a single word and an array of words.
	.align 2
w:	.word 0x41424344
warray:	.word 0x5678ABCD, -112, 0xC5E03666, 4, 5, 6, 7, 8

        # Just reserve 128 bytes space for a variable (array). Not initialized.
        # you can use it as an array of words, halwords, or bytes.
        # we will use it as a word array.
	.align 2
buf:	.space 128

        # Define two ASCIIZ strings. 
        # asciiz with z means 0 (not character '0') is placed after the last character. 

	.align 2
        # Just a new line character
newline: .asciiz "\n"	        

	.align 2
        # Course number, lab number, and your name
name:	.asciiz "CSE3666: Lab 1: Ryan Young \n\n"

	.text				# Code segment
	.globl	main			# declare main to be global

main:	
		
	# load an address, which is a 32-bit value. 
	# la is a pseudo instruction. It is converted into two instructions.
	# See the real instructions in the text segment window after the code is assembled

	# load the address of string name in $a0, and use syscall 4 to print a null-terminated string
	# li is a pseudoinstruction that load an immediate in a register
	la	$a0, name
	li	$v0, 4
	syscall

	# copy two words in warray to buf
	# buf[0] = warray[0]
	# buf[1] = warray[1]
	la $s0, warray # loading the address of warray into $s0
	la $s1, buf    # loading the address of buf into $s1
	lw $t0, 0($s0) # loading first word into $t0 from warray
	sw $t0, 0($s1) # saving first word into buf
	lw $t0, 4($s0) # loading second word into $t0 from warray
	sw $t0, 4($s1) # saving second word into buff
	# Print warray[2] as an signed integer and an unsigned integer
	
	lw $a0, 8($s0) # loading third word into $a0 so we can print
	li $v0, 1 # loading function to be performed by syscall
	syscall # now that we have $a0 and $v0 we know we can perform whats in $v0 and on whats in $a0 
	
	la $a0, newline # laod newline into $a0
	li $v0, 4 # set $v0 to print the new line
	syscall
	
	lw $a0, 8($s0) #loading number
	li $v0, 36 #printing unsigned command
	syscall # printing unsigned

	la $a0, newline # laod newline into $a0
	li $v0, 4 # set $v0 to print the new line
	syscall
 	
	# Print the word located at name in hexadecimal
	lw $a0, name #load name in
	li $v0, 34 # allow hexadecimal to be printed
	syscall
	
	la $a0, newline # laod newline into $a0
	li $v0, 4 # set $v0 to print the new line
	syscall
	
	#print buffer address
	#la $s0, buf #load addres of buffer into $a0 
	#li $v0, 34 # allow hexadecimal to be printed
	#syscall
	
	#la $s6, 8($s0) Loading address of third word into $s6
	#i $v0, 34 Needed to print Hexadecimal
	#syscall Syscall to print
	# System call, type 10, standard exit
Exit:	addi	$v0, $0, 10	
	syscall
	
# Answer the following questions. Remember to make your 
#
# Example: What is the address of w in hexadecimal and decimal?
# Answer: 0x10010000 268500992
#
# Q1: What is the address of buf in hexadecimal and decimal?
# A1: 0x10010024 268501028
#
# Q2: What is the value of warray[0] in decimal?
# A2: 1450748877
#
# Q3: What is the value of warray[1] in hexadecimal?
# A3: 0xffffff90
#
# Q4: What is the address of warray[2] in hexadecimal and decimal?
# A4: 0x100100a4 268501156
#
# Q5: What is the address of name in hexadecimal and decimal?
# A5: 0x100100a8   268501160
#
# Q6: Find the string name in data segment window. Toggle the checkbox for ASCII option. 
#     Observe how bytes are displayed as words in the data segment window.
#     Does the simulator work in big endian mode or littel endian mode?
# A6: The Mars Simulator operates in Little Endian.
