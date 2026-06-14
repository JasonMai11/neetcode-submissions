class Solution {
    public int maxProfit(int[] prices) {
        int lowStock = prices[0];
        int maxProf = 0;
        for (int i = 0; i < prices.length; i++) {
            if (lowStock > prices[i]){
                lowStock = prices[i];
            } else {
                maxProf = Math.max(maxProf, prices[i] - lowStock);
            }
        }
        return maxProf;
    }
}
