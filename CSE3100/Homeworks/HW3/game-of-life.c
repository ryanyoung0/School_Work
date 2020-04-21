#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define M 40
#define N 80
#define N_INIT_CONFIG   8

void clearScreen(void);

// display the game borad 
void display(int m, int n, int A[][n])
{
    int i, j;

    for(i=0; i<m; i++)
    {
        for(j=0; j<n; j++)
        {
            if(A[i][j] == 1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}

// copy a small board into a bigger game board
void copy_block(int m, int n, int source[][n], int i_d, int j_d, int m1, int n1, int dest[][n1])
{
    int i, j;

    for(i=0; i<m; i++)
        for(j=0; j<n; j++)
        {
            if(i_d + i < m1 && j_d + j < n1)
                dest[i_d + i][j_d + j] = source[i][j];		
        }
}

/* This function determines the state of cell A[i][j] in the next generation. 
 * This is a quite long process. So we use a function.
 *
 * Return value is either 0 or 1, indicating A[i][j]'s value in the next generation.
 * */
int next_state(int m, int n, int A[][n], int i, int j)
{
    int sum = 0;

    // Add the values of cells in a 3x3 matrix  
    for(int ii = i - 1; ii <= i + 1; ii ++) {
        int ni = ii;
        // you can also use one statement like
        // ni = (ii + m) % m; 
        if (ni < 0)
            ni = m - 1; 
        else if (ni >= m)
            ni = 0;

        for(int jj = j - 1; jj <= j + 1; jj ++)
        {
            // here we use %
            int nj = (jj + n) % n;
            sum += A[ni][nj];
        }
    }
    // You could skip A[i][j] in the loop, but need many comparisons.
    sum -= A[i][j];

    // the number of comparisons can be reduced, but the logic would be less straightforward
    if(A[i][j] == 1 && (sum == 2 || sum == 3))
        return 1;
    if(A[i][j] == 0 && sum == 3)
        return 1;
    return 0;
}

void next_generation(int m, int n, int A[][n])
{
    int B[m][n];
    int i, j;

    for(i=0;i<M; i++)
        for(j=0; j<N; j++)
            B[i][j] = next_state(M, N, A, i, j);
    
    // if you do not want to write a loop, call copy_block()
    // you could also call memcpy(), but the code would be less readable. 
    for(i=0; i<M; i++)
        for(j=0; j<N; j++)
            A[i][j] = B[i][j];	
}

int main(int argc, char ** argv)
{
    // initialize all elements in A to 0
    int A[M][N] = {{0}};
    // hard coded configuration. 
    int a[10][10] = {
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
        {1,1,1,1,1,1,1,1,1,1},
    };
    int b[5][5] = {
        {0, 0, 0, 0, 0}, 
        {0, 0, 0, 0, 0}, 
        {0, 1, 1, 1, 0}, 
        {0, 0, 0, 0, 0}, 
        {0, 0, 0, 0, 0}
    };
    int c[2][2] = {{1, 1}, {1, 1}};
    int d[3][3] = {{0, 1, 1}, {1, 1, 0}, {0, 1, 0}};
    int e[3][8] = {{0, 0, 0, 0, 0, 0, 1, 0}, {1, 1, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 0, 1, 1, 1}};
    int f[3][7] = {{0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 1, 0, 0, 0}, {1, 1, 0, 0, 1, 1, 1}};
    int g[6][9] = {
        {0,0,0,0,0,0,0,1,0},
        {0,0,0,0,0,1,0,1,1},
        {0,0,0,0,0,1,0,1,0},
        {0,0,0,0,0,1,0,0,0},
        {0,0,0,1,0,0,0,0,0},
        {0,1,0,1,0,0,0,0,0}
    };
    int h[3][4] = {{0, 0, 1, 0}, {0, 0, 0, 1}, {0, 1, 1, 1}}; 

    if (argc == 1) {
        printf("Usage: %s init_conf [num_generations]\n", argv[0]);
        return 1;
    }

    // now, argc must be >= 2
    int init_conf = atoi(argv[1]);
    if (init_conf > N_INIT_CONFIG || init_conf < 1) {
        printf("init_conf must be an integer that is  >= 1 and <= 6.\n"); 
        return -1;
    }

    // set up the initial configuration
    switch(init_conf)
    {
        case 1:	
            copy_block(10, 10, a, M/2, N/2, M, N, A);
            break;
        case 2:
            copy_block(5, 5, b, M/2, N/2, M, N, A);
            break;
        case 3:
            copy_block(2, 2, c, M/2, N/2, M, N, A);
            break;
        case 4:
            copy_block(3, 3, d, M/2, N/2, M, N, A);
            break;
        case 5:
            copy_block(3, 8, e, M/2, N/2, M, N, A);
            break;
        case 6:
            copy_block(3, 7, f, M/2, N/2, M, N, A);
            break;
        case 7:
            copy_block(6, 9, g, M/2, N/2, M, N, A);
            break;
        case 8:
            copy_block(3, 4, h, M/2, N/2, M, N, A);
            break;
        default: 
            // should never get here 
            printf("Error: Invalid init_conf.\n");
            return -1;
    }

    int num_generations;

    if (argc >= 3) {
        num_generations = atoi(argv[2]); 
        if (num_generations <= 0) {
            printf("Error: Number of generations must be an integer > 0.\n");
            return 1;
        }
        for (int i=0; i < num_generations; i++) {
            next_generation(M, N, A);
        }
        display(M, N, A);
    }
    else {
        // interactive
        clearScreen();
        display(M, N, A);
        int rv = 1;

        while (rv == 1) {
            printf("Enter an integer (number of generations):");
            fflush(stdout); // flush stdout to display the prompt w/o new line 
            rv = scanf("%d", &num_generations);
            if (rv == 1 && num_generations > 0) {
                for (int i=0; i < num_generations; i++) {
                    clearScreen();
                    next_generation(M, N, A);
                    display(M, N, A);
                    usleep(50000);
                }
            }
            else if (rv == 0) {
                printf("Error: Number of generations must be an integer > 0.\n");
                return 1;
            }
        }
        if (rv < 0)
            printf("\n");
    }

    return 0;
}


// Use ANSI control sequence to clear screen
void clearScreen(void)
{
    char *CLEAR_SCREEN_ANSI = "\e[1;1H\e[2J";
    printf("%s", CLEAR_SCREEN_ANSI);
    fflush(stdout);
}

