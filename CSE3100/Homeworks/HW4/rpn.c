#include    <stdio.h>
#include    <stdlib.h>
#include    <string.h>
#include    <ctype.h>
#include    <assert.h>

#define     ARGV_STEP      16
#define     LINESIZE_STEP  32
#define     NEW_LINE       '\n'

#define     MIN_STACKSIZE     10

int     is_number(char *s);

enum ErrorNumber {ERR_OK, ERR_EMPTY, ERR_NOOPERANDS, ERR_NOMEM, ERR_END};

// print an error message by an error number, and return
// the function does not exit from the program
// the function does not return a value
void    error_message(enum ErrorNumber errno)
{
    char    *messages[] = {"OK",
        "Stack is empty.",
        "Not enough operands.",
        "Memory allocaton failed.",
        "Invalid error number."};

    if (errno < 0 || errno >= ERR_END)
        errno = ERR_END;
    printf("rpn: %s\n", messages[errno]);
}

// struct for holding tokens from a line
typedef     struct {
    int     num_entries;
    int     argc;
    char ** argv;
} tokens_t;

void    init_tokens(tokens_t *t)
{
    // One way to initialize all members of a structure to 0
    tokens_t t0 = {0};

    // struct assignments
    *t = t0;
}

// get tokens from a line from stdin
// Return values:
// -1:  EOF or error
// 0:   argc, and argv in line is set.
int     get_tokens(tokens_t *t)
{
    char    * line;
    size_t  line_size, line_len;
    int     ch;

    init_tokens(t);

    // initialize variables
    line = NULL;
    line_size = line_len = 0;

    // This is also an example showing how to realloc a block
    // if more space is needed.
    do {
        ch = getchar();

        if (ch == EOF) {
            if (line)
                free(line);
            return -1;
        }

        // append ch to line
        // if not enough space, realloc
        if (line_len + 2 > line_size) {
            line_size += LINESIZE_STEP;
            line = realloc(line, line_size * sizeof(char));
            if (line == NULL) {
                error_message(ERR_NOMEM);
                exit(1);
            }
            // you can check how line_size grows
            // printf("line_size=%lu,ch=%c\n", line_size, ch);
        }

        // there should be at least 2 bytes available
        // one for ch and one for NUL
        line[line_len ++] = ch;
    } while (ch != NEW_LINE);

    // line should not be NULL. It has NEW_LINE at least.
    line[line_len] = '\0';  // put NUL at the end

    int argc = 0;

    char * pch;
    pch = strtok (line," \t\n");
    while (pch != NULL) {
        if (argc == t->num_entries) {
            t->argv = realloc(t->argv, (t->num_entries + ARGV_STEP)*sizeof(char *));
            if (t->argv == NULL) {
                // free(line);  going to exit anyway
                error_message(ERR_NOMEM);
                exit(1);
            }
            t->num_entries += ARGV_STEP;
        }
        // malloc() is done in strdup()
        t->argv[argc++] = strdup(pch);
        // printf ("%s\n",pch);
        pch = strtok (NULL, " \t\n");
    }
    t->argc = argc;
    free(line);
    return argc;
}

// free space in token
// Do not free(t) in this program
void    free_tokens(tokens_t *t)
{
    // TODO BEGIN
    if (t == NULL || t->argv == NULL)
        return;
    for(int i = 0; i < t->argc; i++){
        free(t->argv[i]);
    }
    free(t->argv);
    t->argv = NULL;
    // if *t is on heap (in some programs), free(t)
    // TODO END
}

/*  stack_t  */
typedef struct {
    int     num_entries;
    int     sp;     // index of the number at the top. -1 for empty stack
    int     *stack;
} stack_t;

void    init_stack(stack_t * stack)
{
    stack->num_entries = 0;
    //when stack is empty, stack->sp should be -1.
    stack->sp = -1;
    stack->stack = NULL;
}

// return the numer of elements on the stack (not the number of entries)
int     stack_size(stack_t * stack)
{
    return stack->sp + 1;
}

//  Stack pop.
//  Parameters:
//  stack:  the stack
//  pn:     the location to store the value at the top of stack
//  Return values:
//  0:      the value is in *pn
//  -1:     stack is empty
int     stack_pop(stack_t *stack, int *pn)
{
    // TODO BEGIN
    if (stack && stack->stack && stack->sp >= 0 && stack->num_entries > 0) {
        *pn = stack->stack[stack->sp];
        stack->sp--;
        // check if we need to shrink the stack
        // printf("%d out of %d\n", stack->sp, stack->num_entries);
        if ((stack->sp)*3 < stack->num_entries) {
            //shrink
            int new_entries = 2*(stack->sp);
            if (new_entries < MIN_STACKSIZE)
                new_entries = MIN_STACKSIZE;
            if (new_entries < stack->num_entries) {
                size_t new_size = new_entries*sizeof(int);
                int* new_memory = realloc(stack->stack, new_size);
                if (new_memory == NULL) {
                    error_message(ERR_NOMEM);
                    exit(1);
                }
                stack->stack = new_memory;
                stack->num_entries = new_entries;
            }
        }
        return 0;
    }
    // else
    // TODO END
    return -1;
}

//  Stack push
//  Parameters:
//  stack:  the stack
//  n:      the value to be pushed onto the stack
//  This function does not return a value
void    stack_push(stack_t *stack, int n)
{
    // TODO BEGIN
    // if all entries are used, allocate more entries
    if (stack == NULL)
        return;
    if (stack->sp >= (stack->num_entries - 1)) {
        int num_entries = stack->num_entries * 2;

        if (num_entries < MIN_STACKSIZE) {
            num_entries = MIN_STACKSIZE;
        }

        size_t new_size =  num_entries*sizeof(int);
        int* new_memory = realloc(stack->stack, new_size);
        if (new_memory == NULL) {
            error_message(ERR_NOMEM);
            exit(1);
        }
        stack->stack = new_memory;
        stack->num_entries = num_entries;
    }

    // when there is space, simply push the number onto the stack
    // this is a good place to use (++ stack->sp)
    stack->sp++;
    stack->stack[stack->sp] = n;
    // printf("push %d\n", n);
    // TODO END
}

void    free_stack(stack_t * stack)
{
    if (stack->stack) {
        free(stack->stack);
        stack->stack = NULL;
    }
}

// print information about the stack
void    print_stack_info(stack_t * stack)
{
    printf("num_entries=%d\n", stack->num_entries);

    int sp = stack->sp;
    printf("sp=%d\n", sp);

    // print up to 5 numbers on the stack
    for (int i = 0; i < 5 && sp >= 0; i ++, sp --) {
        printf("stack[%d]=%d\n", sp, stack->stack[sp]);
    }
}

void    print_stack_top(stack_t * stack)
{
    // could have implemented a peek function
    if (stack_size(stack) < 1)
        error_message(ERR_EMPTY);
    else
        printf("%d\n", stack->stack[stack->sp]);
}

// perform different tasks by the token
// Return value:
// 0: continue
// 1: exit
int     process_tokens(stack_t * stack, tokens_t *t)
{
    for (int i=0; i < t->argc; i ++) {
        char *cur = t->argv[i];
        if (! strcmp(cur, "exit")) {
            return 1;
        }
        else if (! strcmp(cur, "info") || ! strcmp(cur, "i")) {
            print_stack_info(stack);
        }
        else if (! strcmp(cur, "p")) {
            print_stack_top(stack);
        }
        // deal with more commands or operators
        /*  You could handle each operator separatly. */
        else if (! strcmp(cur, "+") || ! strcmp(cur, "-") || ! strcmp(cur, "*")) {
            // process +, -, and *
            //     pop the correct number of operands off the stack
            //     perform the operation
            //     push the result onto the stack
            // All these operators require two operands
            // if there are not enough operands on the stack,
            //     report error by calling error_message(ERR_NOOPERANDS);
            //     and continue to process the next token.
            //     the stack should not be changed.
            // TODO BEGIN
            if (stack_size(stack) < 2) {
                error_message(ERR_NOOPERANDS);
                continue;
            }

            int num_one, num_two;
            if(stack_pop(stack, &num_one) == 0 && stack_pop(stack, &num_two) == 0){
                int     r = 0;
                switch (cur[0]) {
                    case '+':
                        r = num_one + num_two;
                        break;
                    case '-':
                        r = num_one - num_two;
                        break;
                    case '*':
                        r = num_one * num_two;
                        break;
                }
                stack_push(stack, r);
            }else{
                // should not happen
                print_stack_info(stack);
                exit(1);
            }
            /*
            else if(! strcmp(cur, "-")) {
            // similar operation
            int num_one, num_two;
            if(stack_pop(stack, &num_one) == 0 && stack_pop(stack, &num_two) == 0){
            stack_push(stack, num_two - num_one);
            }else{
            print_stack_info(stack);
            exit(1);
            }
            }
            */
            // TODO END
        }
        // better to use strtol(). Example is in "man strtol"
        // you do not need to change it
        else if (is_number(cur)) {
            // do not deal with overflow.
            int v = atoi(cur);
            stack_push(stack, v);
        }
        else {
            printf("rpn: unknown token: %s\n", cur);
        }
    }
    return 0;
}

/* main */
int main(void)
{
    tokens_t t;
    stack_t stack;
    int     flag = 0;    // exit if flag != 0

    init_stack(&stack);

    while (flag == 0 && get_tokens(&t) >= 0) {
        flag = process_tokens(&stack, &t);
        free_tokens(&t);
    }

    free_stack(&stack);
    return 0;
}

// check if a string is a decimal number
// could have a DFA, and recognize hex nubmers too
int     is_number(char *s)
{
    // skip '+' or '-'
    if (*s == '+' || *s == '-')
        s ++;

    // the rest must be digits

    // if empty, not a number
    if (! *s)
        return 0;

    while (isdigit(*s)) {
        s ++;
    }

    // could do return (! *s);
    if (*s)
        return 0;

    return 1;
}
