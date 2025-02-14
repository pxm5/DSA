class ProductOfNumbers {
    ArrayList<Integer> stream;
    public ProductOfNumbers() {
        stream = new ArrayList<>();
    }
    
    public void add(int num) {
        stream.add(num);
    }
    
    public int getProduct(int k) {
        int prod = 1;
        for (int i = stream.size() - k; i<stream.size(); i++){
            prod *= stream.get(i);
        }
        return prod;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */