################################ data segment
	.data
name:	.asciiz "CSE3666: Lab 6: Ryan Young (rsy16102)\n\n"
errmsg: .asciiz "The number is too large.\n"
nl:	.asciiz "\n"
str:    .space 128

################################ code segment
	.text
	.globl	main		# declare main to be global

main: 
	la	$a0, name	# load the address of "name" into $a0
	li	$v0, 4		# system call, type 4, print an string
	syscall			# system call

main_loop:
	# use a system call to read a string into str
	la	$a0, str
	li	$a1, 128
	li	$v0, 8
	syscall

	# TODO
	# if str[0] is '\n' or 0, exit from the loop.
	add $t1, $0, $0
	lb $t1, 0($a0) # load first byte from array 
	
	addi $t2, $0, 10 # put 10 into $t2

	beq $t1, $0, Exit # compare first word with zero
	beq $t1, $t2, Exit # compare first word with '\n'
	
	jal myatoi # call myatoi(str)
	# to get the $v0 move it to a saved register
	
	bne $v0, -1, no_error # we are good so we can print out in the three types 
	# else now we haev the error
	# b return_error:
	la $a0, errmsg # load the error in
	li $v0, 4 # print a string
	syscall # do it
	
	b main_continue # loop again
		
no_error:
	move $a0, $s3
	li $v0, 34 # print in hexadecimal
	syscall
	
	li $a0 32 # load blank spcae asciii into $a0
	li $v0, 11 # print ASCII
	syscall 
	
	move $a0, $s3
	li $v0, 36 # print unsigned
	syscall
	
	li $a0 32 # load blank spcae asciii into $a0
	li $v0, 11 # print ASCII
	syscall 
	
	move $a0, $s3
	li $v0, 1 # print signed int
	syscall
	
	# print return value in three different formats, separated by a space.
	# syscall 11 can be used to print a character (e.g., a space, a new line).
	
main_continue:
	b	main_loop
	
Exit:	li	$v0, 10		# System call, type 10, standard exit
	syscall			# ...and call the OS

# TODO
# your implementation of myatoi
myatoi: 
	addi $s3, $0, 0 # initalize V to 0
	#addi $t1, $0, 0 # intitalize I to 0 DONT NEED THIS
	#move $s1, $a0 # put the array into $s1
	
loop_myatoi:
	# put C or S[i] in $t2
	add $t2, $0, $0
	lb $t2, 0($a0) 	
	# check if c is less than 0 and if it its greater than 9
	
	blt $t2, 48, my_exit # banch to return sub function 
	bgt $t2, 57, my_exit # branch to return sub function
	# doing the actually calcs on v
	addi $t7, $0, 10
	subi $t5, $t2, 48 # C - '0'
	multu $s3 $t7 # multiply v by 10
	#Overflow
	
	mfhi $t6 # put the higher bits for comparation with 0 to check for overflow
	bne $t6, $0, Error # need to check for overflow
	
	# V Stuff
	mflo $s4 # put v*10 
	add $s3, $t5, $s4 # add c - '0' plus v * 10
	
	# incrementation

	addi $a0, $a0, 1 # add i to the base address
	
	j loop_myatoi # ASK DINA IF I NEED THE STACK BECUASE IM LOOPING jump back to the top of the function now that the base address is incremented again
	
Error:
	addi $v0, $0, -1 # retun unsigned int - 1
	jr $ra # return to address

my_exit:
        jr 	$ra                 # return to calling routine
   
