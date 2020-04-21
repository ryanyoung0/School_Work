#include <stdio.h>

/* Search for `count' distinct odd numbers that
 * are smaller than `bound' and add up to `sum'.
 *
 * Return value:
 *  1: A solution is found and printed.
 *  0: No solution was found.
 */
int odd_sum(int count, int bound, int sum)
{
    if (count <= 0 || bound <= 1 || sum <= 0)
       return 0;

    /********* base cases *****/
    if (count == 1) {
        // if only one odd number is allowed,
        // it must be sum itself.
        // The sum has to be odd and less than bound
        // sum & 1 extracts the least significant bit of sum
        if (sum < bound && (sum & 1) == 1) {
            printf("%d ",sum);
            return 1;
        }
        else
            return 0;
    }

    /********* prepare for recursion *****/
    // Note that count is at least 2 if the code reaches here
    //
    // starting from the largest odd number below min(bound, sum)
    // because we have bound to leverage, and we need to print numbers
    // in increasing order.
    int  upper;

    // this is a good place to use ?:
    if (bound > sum)
        upper = sum;
    else
        upper = bound;

    // again, could use ?:
    // the largest odd number below odd is either odd - 1 or odd - 2
    if (upper & 1)
        upper -= 2;   // if upper is odd
    else
        upper -= 1;

    /********* try to reduce search space before recursion *****/

    // The parity has to match.
    // count and sum must be odd or even at the same time.
    if ((count ^ sum) & 1)
        return 0;

    // the sum of the smallest count odd integers must <= sum
    // the sum of first n odd integers is n*n.
    if (count * count > sum)
        return 0;

    int n_odd = (upper + 1) / 2; // number of odd numbers <= upper
    if (n_odd < count)  // not enough odd numbers
        return 0;

    // the max sum of count odd integers <= upper must be >= sum
    if ((n_odd * n_odd) - (n_odd - count) * (n_odd - count) < sum)
        return 0;

    /*********  recursion *************/
    // try to find (count - 1) odd numbers that are less than upper and add up to sum - upper
    if (odd_sum(count - 1, upper, sum - upper)) {
        printf("%d ", upper);
        return 1;
    }

    // then the solution must not include upper
    return odd_sum(count, upper, sum);
}

/* Do not change the main() function */
int main(void)
{
    int value;
    int c, b, s;

    printf("Please enter 3 positive integers: count, bound, and sum:\n");
    if (scanf("%d%d%d", &c, &b, &s) != 3) {
        printf("Please enter 3 integers.\n");
        return 1;
    }

    if (c <= 0 || b <= 0 || s <= 0) {
        printf("Integers must be positive.\n");
        return 1;
    }

    value = odd_sum(c, b, s);
    if (value)
        printf("\n");
    else
        printf("There are no solutions.\n");
    return 0;
}
