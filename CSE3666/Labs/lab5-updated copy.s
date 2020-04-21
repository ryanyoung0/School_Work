#	Lab 5
# Josh Redmond, Ryan Young, Yeshi Soleti
#	Merge Sort

	.data			#data segment
	.align 2
buffer:	.space 4096		#allocate space for 1K words

	.align 2
array1: .space 4096  
	#.align 2

name:	.asciiz "CSE3666: Lab 5: Yashaswini Soleti, yas16107\n; Josh Redmond; Ryan Young"

	.text			# Code segment
	.globl	main		# declare main to be global
main: 
        # specify the size of the array, must be less than 1024
	la	$s0, buffer	# address of the buffer in $s0
	li	$s1, 4	# number of elements in $s1

	la	$a0, name	# load the address of "name" into $a0
	li	$v0, 4		# system call, type 4, print an string
	syscall			# system call

	# call init_array() to initialize the array with random values
	move	$a0, $s0	# a0 is the array (?)
	move	$a1, $s1        # a1 is the number of elements
	jal	init_array	

	# check array
	move	$a0, $s0
	move	$a1, $s1
	jal	check_array

	# call merge_sort function with proper arguments
	move	$a0, $s0 #a0 is array 
	move	$a1, $s1 #a1 is number of elements
	jal	merge_sort 	# call merge_sort

	# check array
	move	$a0, $s0
	move	$a1, $s1 #a1 has the value of n, or the number of elements
	jal	check_array

Exit:	li	$v0, 10		# System call, type 10, standard exit
	syscall			# ...and call the OS


##################################TODO#########################################
####START_OF_MERGE_SORT
###############################################################################
#######################void merge_sort(int p[], int n)
# TODO
merge_sort:
	
	slti $t0, $a1, 2 #loop condition, checking if n<2
	bne $t0, $0, End_2 #if it is true, then exit
	
	# Start pushing registers into stack
	addi $sp, $sp, -32 #allocate space on stack for 7 items
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	sw $s2, 12($sp) #p1
	sw $s3, 16($sp) #p2
	sw $s4, 20($sp) #p3
	sw $s5, 24($sp) #s5 is the stack pointer
	sw $s6, 28($sp) #storing p 
	
	move $s6, $a0 #address of p
	
	#allocating array
	add $s5, $sp, $0 #adding the stack pointer into $s5
	sll $t0, $a1, 2 #multiplying n by 4 in $t0
	sub $sp, $sp, $t0 #modifying stack pointer - using up that space
	
	
	
	move $s4, $sp #putting in the address for p3
	
	

	srl $s0, $a1, 1 #save n1 in $t0 with a shift right (div by 2), $s0 has n1
	sub $s1, $a1, $s0  #$s1 has n2
	move $s2, $a0 #loading p into $s2 which is p1
	sll $t0, $s0, 2 #multiplying n1 by 4 
	add $s3, $t0, $a0 #p2 = p + n1
	
	move $a0, $s2
	move $a1, $s0
	
	jal merge_sort 
	
	move $a0, $s3
	move $a1, $s1
	
	jal merge_sort
	
	#initializing i1, i2, i3
	add $t0, $0, $0 # $t0 = i1
	add $t1, $0, $0 #$t1 = i2
	add $t2, $0, $0 #t2 = i3
	
While_1:
	slt $t3, $t0, $s0 #if i1<n1
	slt $t4, $t2, $s1 #if i2<n2
	and $t3, $t3, $t4 #checking if both cases are true
	beq $t3, $0, While_2
	
	#figuring out what we are comparing
	sll $t3, $t0, 2 #multiplying i1 by 4, storing in $t3
	sll $t4, $t1, 2 #multiplying i2 by 4, storing in $t4
	sll $t5, $t2, 2 #multiplying i3 by 4, storing in $t5
	
	#get base address
	add $t3, $s2, $t3 #p1[i1]
	add $t4, $s3, $t4 #p2[i2]
	add $t5, $s4, $t5 #p3[i3]
	
	lw $t3, 0($t3) #t3 has value p1[i1]
	lw $t4, 0($t4) #t4 has value of p2[i2]
	
	slt $t6, $t3, $t4
	beq $t6, $0, Else #if not true, jump to Else condition
	sw $t3, 0($t5)
	addi $t0, $t0, 1 #incrementing
	addi $t2, $t2, 1 #incrementing
	
	j While_1

Else:
	sw $t4, 0($t5)
	addi $t1, $t1, 1 #incrementing
	addi $t2, $t2, 1 #incrementing
	
	
	j While_1
While_2:
	slt $t6, $t0, $s0 #conditional
	beq $t6, $0, While_3 #if false go to next while
	
	sll $t4, $t0, 2 #multiplying i1 by 4, storing in $t3
	sll $t5, $t2, 2 #multiplying i3 by 4, storing in $t5
	
	#get base address
	add $t4, $s2, $t4 #p1[i1]
	add $t5, $s4, $t5 #p3[i3]
	
	lw $t4, 0($t4)
	sw $t4, 0($t5)
	addi $t0, $t0, 1 #incrementing index i1
	addi $t2, $t2, 1 #incrementing index i3 
	
	j While_2
	
While_3:
	slt $t6, $t1, $s1
	beq $t6, $0, Copy #if false jump to copy
	
	sll $t4, $t1, 2 #multiplying i2 by 4, storing in $t4
	sll $t5, $t2, 2 #multiplying i3 by 4, storing in $t5
	
	#get base address
	add $t4, $s3, $t4 #p2[i2]
	add $t5, $s4, $t5 #p3[i3]
	
	lw $t4, 0($t4)
	sw $t4, 0($t5)
	addi $t1, $t1, 1 #incrementing index i2
	addi $t2, $t2, 1 #incrementing index i3
	
	j While_3

Copy:

	add $t0, $0, $0 #x is $t0 and is a counter

	#getting length of p3
	
	add $t1, $s0, $s1 #length of p3

Loop:

	slt $t2, $t0, $t1 #if x < len
	beq $t2, $0, End #if not true jump to end
	sll $t3, $t0, 2 #multiply x by 4
	add $t4, $t3, $s6 #p offset, base address of p
	add $t3, $t3, $s4 #base address of p3[x]
	lw $t3, 0($t3) #value at index in p3
	sw $t3, 0($t4) #copying the word
	addi $t0, $t0, 1 #incrementing $t0 by 1

	j Loop

End: #restoring all variables in the stack
	move $sp, $s5 #resetting the stack pointer
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $s2, 12($sp) #p1
	lw $s3, 16($sp) #p2
	lw $s4, 20($sp) #p3
	lw $s5, 24($sp) #s5 is the stack pointer
	lw $s6, 28($sp) #storing p 
	addi $sp, $sp, 32
	
	End_2:

        jr	$ra
           
####END_OF_MERGE_SORT

# void copy_array(int dst[], int src[], int n)
# This funciton is a leaf function
copy_array:
	b	ll_copy_array_test
	
ll_copy_array_loop:
	lw	$t0, ($a1)
	sw	$t0, ($a0)
	addi	$a2, $a2, -1
	addi	$a1, $a1, 4
	addi	$a0, $a0, 4

ll_copy_array_test:
	bne 	$a2, $0, ll_copy_array_loop
	move 	$a0, $s6 #restore arguments to original state
	move 	$a1, $s7 
	jr	$ra

####END_OF_copy_array
###############################################################################

################################################################################
##### No need to change anything below
################################################################################
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
	
        .data   #data segment
        .align	2
ais_sum:.word   0
msg0:	.asciiz "Sorted\n"
msg1:	.asciiz "Not sorted\n"
msg2:	.asciiz "Error: data were corrupted.\n"
msg3:	.asciiz "Error: array length is less than 1.\n"

        .text

# void check_array(int p[], int n)
# return 0 if the array elements are in ascending order
# return a non-zero value if not sorted or other errors
# p is in $a0, n is in $a1
check_array:

	# if (n < 1) return 0
	slti	$at, $a1, 1
	bne	$at, $0, ll_ais_exit3

	# save sum in $t2	
	li	$t2, 0
	li	$v0, 0

	# load 	first word in $t0
	lw	$t0, ($a0)
	b	ll_ais_test

ll_ais_loop:
	lw	$t1, ($a0)
	
	slt 	$at, $t1, $t0	# if $t1 < $t0
	beq	$at, $0, ll_ais_skip

	li	$v0, 1		# not sorted

ll_ais_skip:
	move	$t0, $t1

ll_ais_test:
	xor	$t2, $t2, $t0
	addi	$a0, $a0, 4
	addi	$a1, $a1, -1
	bne	$a1, $0, ll_ais_loop   # if there are elements goto loop

	la	$t4, ais_sum
	lw	$t0, ($t4)
        sw      $t2, ($t4)
        
        beq	$t0, $0, ll_ais_sum_ok
        bne	$t0, $t2, ll_ais_exit2
        
ll_ais_sum_ok:
	beq	$v0, $0, ll_ais_exit0

ll_ais_exit1:	# return 1
	la	$a0, msg1
	li	$v0, 4
	syscall
	li	$v0, 1
	b	ll_ais_exit
	
ll_ais_exit2:	# return 2
	la	$a0, msg2
	li	$v0, 4
	syscall
	li	$v0, 2
	b	ll_ais_exit

ll_ais_exit3:	# return 3
	la	$a0, msg3
	li	$v0, 4
	syscall
	li	$v0, 3
	b	ll_ais_exit

ll_ais_exit0:	# return 0
	la	$a0, msg0
	li	$v0, 4
	syscall
	li	$v0, 0

ll_ais_exit:
	jr	$ra
#######################################################################
