class Solution {
    public int climbStairs(int n) {
        if (n==0)
        {
            return 1;
        }else if(n<0)
        {
            return 0;
        }
        int a = climbStairs(n-1);
        int b = climbStairs(n-2);
        return a + b;
    }
}
