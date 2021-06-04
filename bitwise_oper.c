/**
 * For a given int n and threshold k, for each number from 1 through n, 
 * find the maximum value of the logical, or, and , xor when
 * compared against threshold
 */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int i, j;
  int a, b, c;
  a = b = c = 0;
  for (i = 1; i <= n; i++)
  {
        for (j = 1 + i; j <= n; j++)
        {
            a = ((i & j) < k && (i & j) > a )? i & j: a;
            b = ((i | j) < k && (i | j) > b )? i | j: b;
            c = ((i ^ j) < k && (i ^ j) > c )? i ^ j: c;
        }
  }
  printf("%d\n%d\n%d\n",a, b, c);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
