class Solution {
    HashMap<Integer, Integer> results = new HashMap<>();
    public int climbStairs(int n) {
        
        if (n==0)
        {
            results.putIfAbsent(n,1);
            return 1;
        }else if(n<0)
        {
            results.putIfAbsent(n,0);
            return 0;
        }
        int a = results.getOrDefault(n-1,climbStairs(n-1));
        int b = results.getOrDefault(n-2,climbStairs(n-2));
        results.putIfAbsent(n,a+b);
        return a + b;
    }
}
