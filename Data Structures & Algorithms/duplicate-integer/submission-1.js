class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let number = new Set();
        for (const num of nums){
            if (number.has(num)) return true;

            number.add(num);
        }
        return false;
    }
}
