#search element in an array
#include <stdio.h>

int main(void) {
	int t,n,key,count,i,j,k; 
	printf("Enter the test cases:");
	scanf("%d",&t); 
	for(i=0;i<t;i++)
	{
	    count=0;
	    printf("Enter the size of array:\n");
	    scanf("%d",&n);
	    int arr[n];
	    printf("Enter array elements:\n");
	    for(j=0;j<n;j++){
	        scanf("%d",&arr[j]);
	        
	    }  
	    printf("Enter the search key:\n");
	    scanf("%d",&key);
	    for(k=0;k<n;k++){
	        if(arr[k]==key){
	           count++;
	        } 
	    }
	    if(count>0){
	        printf("YES\n");
	    }
	    else{
	        printf("NO\n");
	    }
	}
	
	return 0;
}
