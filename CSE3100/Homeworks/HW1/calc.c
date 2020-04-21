#include <stdio.h>

/*
 * Print an integer (of int) in four formats:
 *
 * The output is:
 * name
 * binary
 * hexadecimal
 * decimal with bits interpreted as signed int
 * decimal with bits interpreted as unsigned int.
 *
 * The function does not return a value.
 */
void print_int(int n, char *name)
{
    // print name
    printf("%s\tbin:", name ? name : "");

    // a loop to print bits from most significant to least significant
    // also an example of using sizeof
    for (int i = sizeof(int) * 8 - 1; i >= 0; i --)
       printf("%d", (n >> i) & 1);

    // other formats
    printf(" hex:%08X signed:%10d unsigned:%10u\n", n, n, n);
}

int main(void)
{
    int a, b;
    char c;

    // Repeatedly read integers and operator from standard input
    // To exit, press Ctrl-D or Ctr-C

    while (scanf("%i %c%i", &a, &c, &b) == 3) {
        // Your code to be placed after TODO
        int r;

        // You can use switch
        if (c == '+') {
            r = a + b;
        } else if (c == '-') {
            r = a - b;
        } else if (c == '*') {
            r = a * b;
        } else if (c == '/') {
            r = a / b;
        } else if (c == '%') {
            r = a % b;
        } else if (c == '&') {
            r = a & b;
        } else if (c == '|') {
            r = a | b;
        } else if (c == '^') {
            r = a ^ b;
        } else if (c == 'l') {
            r = a << b;
        } else if (c == 'r') {
            r = a >> b;
        }
        else {
            printf("Operator %c is not supported.\n", c);
            c = 0;
        }

        // Since all test cases have valid operator,
        // this should not happen in submission testing. 
        if (!c)
            continue;
        
        // call print_int to print integers
        print_int(a, "a");
        printf("%c\n", c);
        print_int(b, "b");
        printf("=\n");
        print_int(r, "r");
    };

    return 0;
}
