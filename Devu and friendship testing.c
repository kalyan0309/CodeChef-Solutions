#include <stdio.h>
int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int n,i,j,c=0;
	    scanf("%d",&n);
	    int a[n];
	    for(i=0;i<n;i++){
	        scanf("%d",&a[i]);
	    }
	    for(i=0;i<n;i++){
	        for(j=0;j<n;j++){
	            if(a[i]==a[j] && i!=j){
	               a[i]=0;
	            }
	        }
	    }
	    for(i=0;i<n;i++){
	        if(a[i]!=0){
	            c+=1;
	        }
	    }
	    printf("%d\n",c);
	}
	return 0;
}
