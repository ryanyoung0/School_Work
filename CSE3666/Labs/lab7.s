################################ data segment
	.data
name:	.asciiz "CSE3666: Lab 7: Ryan Young (rsy16102)\n\n"
nl:	.asciiz "\n"

	.align 2
fconst: .float	0.0, 1.0, 2.0, -1.0
arr:    .float	0.1, 0.2, 0.3, 0.4, 0.5, 0.7853981, 1.570796, 3.1415927, 0.0

################################ code segment
	.text
	.globl	main		# declare main to be global
	

main: 
	la	$a0, name	# load the address of "name" into $a0
	li	$v0, 4		# system call, type 4, print an string
	syscall			# system call

	la	$s0, arr	
	li	$s1, 9		# the number of elements in the array
	sll	$s1, $s1, 2	# make it 36
	add	$s1, $s1, $s0   # make $s1 have the base address of $s0 + 36
	

main_loop:
	# TODO
	lwc1 $f12, 0($s0) # load the element from the array to $f12 thi is X in the C code 
	jal sin# for valid index i = 0, 1, ..., 
	# will print the value in $f12
	mov.s $f12, $f0
	li $v0, 2 # print sin(arr[i]), and new line
	syscall # print $f12
	# print new line 
	li $a0, 10 
	li $v0, 11
	syscall
	
	
main_continue:
	addi	$s0, $s0, 4
	bne	$s0, $s1, main_loop
	
Exit:	li	$v0, 10		# System call, type 10, standard exit
	syscall			# ...and call the OS

# TODO
# your implementation of sin
sin: 
        # loading the intial float value
        # $f12 is the input float
	# $f0 is the output
	li $s2, 0 # this is the I var
	li $s3, 20 # this is 20
	
	
        la $t0, fconst # load the address of sign
        lwc1 $f9, 4($t0) # this is 1.0
        lwc1 $f10, 8($t0) # this is 2.0
        lwc1 $f11, 12($t0) # this is -1.0
        lwc1 $f1, 4($t0) # sign var
        lwc1 $f2, 4($t0) # n var
        lwc1 $f3, 4($t0) # fact var
        lwc1 $f4, 0($t0)# load 0.0 into $f4
        add.s $f4, $f4, $f12 # 0.0 + $f12 THIS GIVES the power var
        lwc1 $f5, 0($t0) # load 0 into $f5
        add.s $f5, $f5, $f12 # 0.0 + $f12 THIS GIVES the v var

sin_loop:
	addi $s2, $s2, 1 # increment i
	
	mul.s $f4, $f4, $f12 # this is power * x
	mul.s $f4, $f4, $f12 # this is power * x
	
	add.s $f7, $f2, $f9 # n + 1.0
	add.s $f8, $f2, $f10 # n + 2.0
	mul.s $f7, $f7, $f8 # (n + 1.0) * (n + 2.0)
	mul.s $f3, $f3, $f7 #fact *= (n + 1.0) * (n + 2.0)
	
	add.s $f2, $f2, $f10 # n += 2.0
	mul.s $f1, $f1, $f11 # sign = - sign // multiplied by -1.0
	
	# v += power / fact * sign
	
	mul.s $f14, $f3, $f1 # = fact * sign
	
	div.s $f15, $f4, $f14 # = power / (fact * sign)
	
	add.s $f5, $f5, $f15 # v += (power / (fact * sign) )
	# set the output should be in $f12
	mov.s $f0, $f5
	blt $s2, $s3 sin_loop # go back to the top of the loop
	jr 	$ra                 # return
