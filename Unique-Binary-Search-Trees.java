class Solution {


    public int numTrees(int n) {
        int ans = (int) Math.ceil((fact(2*n)/(fact(n+1) * fact(n))));
        return ans;
    }

    public double fact(int n){
        double prod = 1;
        for (int i = 2; i<=n; i++){
            prod*=i;
        }
        return prod;

    }
}