class Solution {

    public double helper(double x, long n){
        if (n < 0){
            return 1/helper(x, -n);
        }

        if (x == 0){
            return 0;
        }
        if (n == 0){
            return 1;
        }
        if(n==1){
            return x;
        }
        if (n % 2 != 0){
            return x * helper(x*x, (n-1)/2);
            // return out*x;
        }
        
        return helper(x*x, n/2);
    }

    public double myPow(double x, int n) {
        
        return helper(x, (long) n);
    }
}