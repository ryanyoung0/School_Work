#include <stdio.h>
#include <ctype.h>

#define     NEW_LINE    '\n'
#define     CHAR_SLASH  '/'

#define     MIN_YEAR    1600
#define     MAX_YEAR    2399
#define     YEAR_OFFSET 2000

#define     RV_NODATE   0
#define     RV_VALIDDATE 1
#define     RV_INVALIDDATE 2

/***** date checking *****/

_Bool isLeapYear(int const year);
int daysInMonth(unsigned const month, int const year);

_Bool isLeapYear(int const year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int daysInMonth(unsigned const month, int const year) {
    // You could use a switch statement.
    // swith (month)

    // out-of-bound entries, including {0} + [13, inf)
    if ((month - 1) >= 12) return 0;

    // Feb
    if (month == 2) return 28 + isLeapYear(year);

    // 31 if X is odd, where X is m+1 if m > 7 and m otherwise
    // or you can just list the months that have 31 days
    // For example, if (month == 1 || month == 3 ...)
    if (1 == (month + (month > 7)) % 2) return 31;

    // otherwise 30
    return 30;
}

/***** DFA *****/

/* You could use macro to define state values */
typedef enum States_T {
    STATE_S = 0, // starting point

    STATE_M1 = 1, STATE_M2, // month
    D0, D1, D2, // day
    STATE_Y0, STATE_Y1, STATE_Y2, STATE_Y3, STATE_Y4, // year

    STATE_OK = -1, STATE_ERR = -2, // ending points
} States;

/* The function checks if a date is present at the beginning of a line,
 * and if the date is valid.
 *
 * Return values:
 *
 * 0:  Not date was found.
 * 1:  Date is valid.
 * 2:  Date was found, but not valid.
 */
int get_date()
{
    // starting state
    // if you use macros, simply do
    // int state = STATE_S;
    States state = STATE_S;
    int     c;

    int day = 0, month = 0, year = 0;

    while ((c = getchar()) != NEW_LINE && c != EOF) {
        switch (state) {
            case STATE_S:
                if (isblank(c)) {
                    // Stay in current state if blank
                }
                // if it is a digit, it is the first digit in month
                else if (isdigit(c)) {
                    month = c - '0';
                    state = STATE_M1;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_M1:
                // Only digit or slash is valid
                // if another numeric, postpend month and -> STATE_M2
                if (isdigit(c)) {
                    month = (month * 10) + c - '0';
                    state = STATE_M2;
                }
                // if slash, stop reading month and -> D0
                else if (c == CHAR_SLASH) {
                    state = D0;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_M2:
                // Already had two digits. Only accepts slash, -> D0
                if (c == CHAR_SLASH) {
                    state = D0;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case D0:
                // only accepts a digit for day -> D1
                if (isdigit(c)) {
                    day = c - '0';
                    state = D1;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case D1:
                // valid digit, update day, -> D2
                if (isdigit(c)) {
                    day = (day * 10) + c - '0';
                    state = D2;
                }
                // if slash, stop day and start year, -> STATE_Y0
                else if (c == CHAR_SLASH) {
                    state = STATE_Y0;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case D2:
                // only slash allowed, -> STATE_Y0
                if (c == CHAR_SLASH) {
                    state = STATE_Y0;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_Y0:
                // only accepts a digit for year -> STATE_Y1
                if (isdigit(c)) {
                    year = c - '0';
                    state = STATE_Y1;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_Y1:
                // only accepts a valid digit, update year -> STATE_Y2
                if (isdigit(c)) {
                    year = (year * 10) + c - '0';
                    state = STATE_Y2;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_Y2:
                // if valid digit, update year, -> STATE_Y3
                if (isdigit(c)) {
                    year = (year * 10) + c - '0';
                    state = STATE_Y3;
                }
                // if only 2 digits in the date -> STATE_OK
                else if (isblank(c)) {
                    year += YEAR_OFFSET;
                    state = STATE_OK;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_Y3:
                // only accepts a valid digit, update year
                // if valid digit, update year, -> STATE_Y4
                if (isdigit(c)) {
                    year = (year * 10) + c - '0';
                    state = STATE_Y4;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_Y4:
                // only blank or new line is expected  -> STATE_OK
                if (isblank(c)) {
                    state = STATE_OK;
                }
                // otherwise error
                else
                    state = STATE_ERR;
                break;

            case STATE_OK:
            case STATE_ERR:
                // do not change state once in STATE_OK or STATE_ERR
                break;

            default:
                // otherwise something is wrong
                state = STATE_ERR;
        }
    }

    // accepting state: STATE_Y4 and STATE_OK
    if (state != STATE_Y2 && state != STATE_Y4 && state != STATE_OK)
        return RV_NODATE;

    if (state == STATE_Y2)
        year += YEAR_OFFSET;

    // Validate date
    // error if year is not in range
    if (! (year >= MIN_YEAR && year <= MAX_YEAR))
        return RV_INVALIDDATE;

    // error if month out of range
    if (month < 1 || month > 12)
        return RV_INVALIDDATE;

    // error if day out of range
    if (day < 1 || day > daysInMonth(month, year))
        return RV_INVALIDDATE;

    return RV_VALIDDATE;
}

/***** main *****/
/* Do not change the main function. */
int main(void)
{
    // run the loop until hit end of file
    do  {
        int rv = get_date();

        if (!feof(stdin)) {
            switch (rv) {
                case RV_NODATE:
                    printf("No date found.\n");
                    break;
                case RV_VALIDDATE:
                    printf("Valid date.\n");
                    break;
                case RV_INVALIDDATE:
                    printf("Invalid date.\n");
                    break;
                default:
                    printf("Unknown return value %d.\n", rv);
                    break;
            }
        }
    } while (! feof(stdin));

    return 0;
}
