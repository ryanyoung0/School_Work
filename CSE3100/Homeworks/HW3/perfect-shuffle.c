#include    <stdio.h>
#include    <stdlib.h>

// Print first n elements in array arr
// This function does not return a value.
void print_array(int *arr, int n)
{
    for (int i = 0; i < n; i ++)
        printf("%d ", i); 
    printf("\n");
}

// initialize an array of n int's to be 0, 1, 2, ..., n-1
// This function does not return a value.
void init_array(int *arr, int n)
{
    for (int i = 0; i < n; i ++)
        arr[i] = i;
}

// check if an array of n int's is in the intial order 
// Return value:
//      0: Not in the initial order
//      1: Yes 
int is_initial (int *arr, int n)
{
    for (int i = 0; i < n; i ++)
        if (arr[i] != i)
            return 0;
    return 1;
}

// do a perfect shuffle on an array of n elements.
// n must be at least 1.
// src is the source array, dest is the destination array.
// if n is less than 1, dest is not changed.
// the function does not return a value.
void perfect_shuffle(int *dest, int *src, int n)
{
    // i: index to left, j: index to right
    // k: index to dest
    int     i, j, k; 
    int     half;

    if (n < 1)
        return;

    half = (n + 1) / 2; 
    i = k = 0; j = half; 

    // place two cards each time
    for (k = 0; k + 1 < n; i ++, j ++, k += 2) {
        dest[k] = src[i];
        dest[k + 1] = src[j];
    }

    // handling odd case
    if (k < n) 
        dest[k] = src[i];
}

// return the number of perfect shuffles that place a deck of n cards back to original order
// n must be positive
int find_cycle(int n)
{
    int     count = 0;
    int     arr1[n];
    int     arr2[n];
    int     *current, *shuffled;

    init_array(arr1, n);

    current = arr1;
    shuffled = arr2;
    do {
        perfect_shuffle(shuffled, current, n);
        count ++;

        // switch shuffled and switch  
        int * tmp;
        tmp = current;
        current = shuffled;
        shuffled = tmp;
    } while (! is_initial(current, n));
    return count;
} 

int main(int argc, char **argv)
{
    int     n;

    /* the upper bound of n is not checked. Try what happens if you enter a large number */
    if (argc == 1) {
        int     rv;
        while ((rv = scanf("%d", &n)) >= 0) {
            if (rv != 1 || n < 1) {
                printf("Number of cards must be a positive integer.\n");
                return 1;
            }
            printf("%d %d\n", n, find_cycle(n)); 
        }
    }
    else {
        for (int i = 1; i < argc; i ++) {
            n = atoi(argv[i]);
            if (n < 1) {
                printf("Number of cards must be a positive integer.\n");
                return 1;
            }
            printf("%d %d\n", n, find_cycle(n)); 
        }
    }
    return 0;
}
