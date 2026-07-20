class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        List <List <Integer>> result = new ArrayList<>();


        return subset(nums,0,new ArrayList<Integer>(), result);
    }

    public List<List<Integer>> subset (int nums[], int i, List <Integer> sub, List<List<Integer>> result)
    {
        ArrayList<Integer> newSub = new ArrayList<>(sub);
        newSub.add(nums[i]);
        if(i==nums.length - 1)
        {
            result.add(sub);
            result.add(newSub);
            return result;
        }
        i++;
        subset(nums, i, sub, result);
        subset(nums, i, newSub, result);

        return result;
    }
}
