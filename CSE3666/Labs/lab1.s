#	MIPS Example
#	Comments.  Anything after # is comments.

	# .text starts code segments
	.text
	.globl	main	# declare main to be global. Note it is ".globl"

	# define a label
main:	
	# performing  100 + 300 - 450
	
	addi	$s1, $0, 100
	addi	$s2, $0, 300
	add	$s1, $s1, $s2
	addi	$s1, $s1, -450

	# TODO
	# Add you code here
	# read an integer x. 
	li $v0, 5 # loading 5 into V0 so we can read an integer
	#add $a0, $t0, $zero
	syscall
	sub $a0, $zero, $v0
	# two instructions
	li $v0, 1
	syscall
	
	# change its sign. Note that -x = 0 - x
	# one instruction

	# print the result (-x)
	# two or three instructions

	# System call
	# The simulator supports many system calls. 
	# Regiter $v0 is used to specify which system calls to make.
	# Some system calls require additional info in reigseters like $a0 and $a1.
	# And some system calls also return values. Read the manuals.  
	# System call number 10 is for exiting from the program, and
	# it does not need additional info.
	# Therefore, set the value of $v0 to 10 and do 'syscall'
	
exit:	addi	$v0, $0, 10	
	syscall				# ...and call the OS
