//decimal to binary

include <stdio.h>

void toBinary(int N)
{
    int binarr[32];
    int i=0,j;
    while(N>0)
    {
        binarr[i]=N%2;
        N=N/2;
        i++;
    }
    for(j=i-1;j>=0;j--)
    {
        printf("%d",binarr[j]);
    }
}

//{ Driver Code Starts.

int main() {
	//code
	
	int t;
	scanf("%d", &t);
	
	
	while(t--)
	{
	    int n;
	    scanf("%d", &n);
	    
	    toBinary(n);
	    printf("\n");
	}
	return 0;
}
// } Driver Code Ends