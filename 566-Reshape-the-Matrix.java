class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if  (r * c != mat.length * mat[0].length){
            return mat;
        }

        int[][] reshaped = new int[r][c];
        int[] arr = new int[r*c];
        int x = 0;
        for (int i = 0; i<mat.length; i++){
            for (int j = 0; j< mat[0].length; j++){
                arr[x] = mat[i][j];
                x++;
            }
        }
        x = 0;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                reshaped[i][j] = arr[x];
                x++;
            }
        }


        return reshaped;
    }
}