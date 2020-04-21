################################ data segment
	.data
name:	.asciiz "CSE3666: Lab 3: Ryan Young (rsy16102)\n\n"
nl:	.asciiz "\n"

# set alignment for words. 
# Use 5 here so you can find the array in the data segment easily
	.align 5
buffer:	.space 4096		# allocate space for 1K words

################################ code segment
	.text
	.globl	main		# declare main to be global

main: 
        # specify the size of the array, must be less than 1024
	la	$s0, buffer	# address of the buffer in $s0
	li	$s1, 1024       # number of elements in $s1

	la	$a0, name	# load the address of "name" into $a0
	li	$v0, 4		# system call, type 4, print an string
	syscall			# system call

	# call init_array() to initialize the array with random values
	move	$a0, $s0	# use pseudoinstructions
	move	$a1, $s1
	jal	init_array	

	# TODO
	# call your find_max function with proper arguments
	move $a0, $s0		#use pseudoinstrucitons
	move $a1, $s1
	jal max_abs
	

	# print the returned value
	add $a0, $0, $v0
	li $v0, 1
	syscall
	# print the newline character
	la	$a0, nl		
	li	$v0, 4
	syscall

Exit:	li	$v0,10		# System call, type 10, standard exit
	syscall			# ...and call the OS

# TODO
# your implementation of max_abs
max_abs:
	addi $v1, $0, -1	#Initalizing maxa to be -1 in register $v1
	li $t3, 0		#Making register $t3 0 (i = 0 ) in the c code
	j checktheloop		#Making sure the loop isnt broken
	
loop:
	sll $t5, $t3, 2		#Multiplying $t3 by 4 and putting it in $t5
	add $t5, $t5, $a0	#Adding the address of $a0 to $t5
	lw $t1, ($t5)		#Loading $t5, p[i] in the c code, into $t1
	slti $at, $t1, 0	#Checking if $t1 is negative
	beq $at, $0, keepmoving	#If $t1 is positive we keep moving	
	sub $t1, $0, $t1	#subtract a from 0 to negate it if it's negative
	sw $t1, ($t5)		#storing the value of a into p[i] or $t1
	
keepmoving:
	slt $at, $v0, $t1	#Checking is the maxa needs to be updated
	beq $at, $0, iteratation#Increase $t3 by 1 or i in the c code to keep looping
	move $v1, $t1		#Updating new maxa
iteratation:
	addi $t3, $t3, 1	#Increasing $t3 by 1 or i in the c code
	
checktheloop:
	slt $at, $t3, $a1	#Checking if $t3 is less than $a1 or i is less than n in the c code
	bne $at, $0, loop	#Checkign if $at is not 0 and if not then it can be put in the loop
        jr $ra                  #Return back to the call routine
     
##### No need to change anything below
# void init_array(int *p, int n), or
# void init_array(int p[], int n) 
# use pseudorandom system calls in MARS
init_array:
	#save parameters
	addi	$t0, $a0, 0
	addi	$t1, $a1, 0

	# set the seed
	li	$a0, 0
	li	$a1, 3666
	li	$v0, 40
	syscall

	lui	$t2, 0x8000
	
	# A while loop to put random numbers in the array
	j	llinit_test

llinit_loop:
	li	$a0, 0			# syscall 41: rand()
	li	$v0, 41
	syscall
	
	# retry if the random number is 0x80000000
	beq	$a0, $t2, llinit_loop	

	sw	$a0, ($t0)		# save the random value
	addi	$t0, $t0, 4		# move to the next word
	addi	$t1, $t1, -1		# n --

llinit_test:
	slti	$at, $t1, 1		  # n < 1?
	beq	$at, $zero, llinit_loop   # if not, goto loop

	jr	$ra
