#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main()
{
    int n;
    
    scanf("%d",&n);
    int a[n][n];
    int i = 0, j = 0;
    for(i = 0;i<n;i++)
    {
        for(j = 0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    int k = 0;
    for(k = 0;k<n;k++)
    {
        for(i = 0;i<n;i++)
        {
            for(j = 0;j<n;j++)
            {
                if(a[i][k]+a[k][j] < a[i][j])
                {
                    a[i][j] = a[i][k]+a[k][j];
                }
            }
        }
    }
    
    for(i = 0;i<n;i++)
    {
        for(j = 0;j<n;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
