/* Compute e ** x, using Taylor series.  */

#include <stdio.h>

int main(void)
{
    double x;
    int n;
    
    /* Read numbers from the standard input. Execute the loop if it is successful. */
    /* To exit, press Ctrl-D or Ctr-C */
    while (scanf("%lf%d", &x, &n) == 2)
    {
        // Use only first n terms
        double e, p, f;
        int i;

        i = 0;
        e = 0.0;

        p = 1;      // p = x ** i
        f = 1;      // f = i!
        while (i < n) {
            // add another term 
            e += p / f; 
            // increment i
            i ++;
            // prepare for the next iteration
            // compute x^i from x^{i-1}
            p *= x;
            // compute i! from (i-1)!
            f *= (double)i;
        }

        printf("exp(%.10f)=%.10f\n", x, e);
    }

    return 0;
}
