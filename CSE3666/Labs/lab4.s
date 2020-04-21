################################ data segment
	.data
name:	.asciiz "CSE3666: Lab 4: Ryan Young (rsy16102)\n\n"
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
	la	$a0, str # each time through the loop takes a char c from the string input
	li	$a1, 128 # now holds 128 bytes for our string
	li	$v0, 8
	syscall

	# TODO
	# call strtoupper and make sure that it isnt an end line character and make sure its not the end if it is exit
	jal strtoupper # for each char we call strtoupper
	beq $t0, 10, Exit1 #output of strtoupper , 10 then exit1 because this means its "\n"
	beq $t0, $0, Exit1 # prcents the loop from running twice if i take this out the capitalized string is printed twice
	
	
	# print the returned char if its not the end of line or 0
	la $a0, str
	li $v0, 4 # loading in 1 to $v0 so sys call will print a string
	syscall
	
Exit1:	
	# printing the char
	la $a0, str # need to print the char when we exit
	li $v0, 4 # command to print a string
	syscall # need the sys call
	
	# now exit out for good
	li $v0, 10 # System call, type 10, standard exit
	syscall # ...and call the OS

# TODO
# your implementation of strtoupper
strtoupper:
	# loading onto stack and creating stack space
	# create space on the stack for 8 bytes or two ints so we are saving the address where we came from and the char each time
	addi $sp, $sp, -8
	# push $ra onto the stack at the first spot needs fro spots because its an int address
	sw $ra, ($sp) # wont work if there is a 0 here do you know why?
	# push str onto the stack this will need 4 spots because ASCII is an int
	sw $a0, 4($sp)
	
	
	#taking off stack
	# load $a0 off the stack and into a temp variable
	lb $t0, ($a0) # CHECK IF CAN USE LW and might need to change from stack to $a0
	# output of strtouper, $0 then exit because this means its the end of the string 0 is the last thing in an arary of chars or a string 
	beq $t0, $0, Exit2 
	# set if char is greater than 122 need to keep $t0 as the char though 
	
	# check if char is less than a
	slti $t1, $t0, 97
	# if less than then we skip that char
	beq $t1, 1, skip
	# reset $t2 to 0
	add $t1, $0, $0
	

	sgt $t2, $t0, 122
	# check if $t1 is out of range and if it is then pass over it and look or enxt valid char
	beq $t2, 1, skip
	# reset $t1 to 0
	add $t2, $0, $0
	# now that it has passed all the test we need to capitalized it
	# can do this by using ASCII and subtracting 32
	#hence why need to keep $t0 the lowercase char and use $t1 and $t2 as the checks to make sure char was in range
	addi $t0, $t0, -32
	# put the new captial char back into the stack
	sb $t0, ($a0) # needs to be sb so it will continue to loop and not just sw because that will only return the first char
	# dont need this
        #jr 	$ra                 # return to calling routine
        
        
skip:
	# increment $a0 by 1 
	addi $a0, $a0 1
	# go back now that we incremented need to use link so we can go back and not just jr
	jal strtoupper
	
	
Exit2:
	# now that we are done we have to fix all the stuff we did to the stack
	# reset stack to the original state
	addi $sp, $sp, 8 
	# need to get the register address back so we can get out of here
	lw $ra, ($sp) # CHECK IF NEED TO TAKE THE ZERO OUT OF HERE
	# get our char back from the stack
	lw $a0, 4($sp)
	# peace out back to the main loop
	jr $ra
