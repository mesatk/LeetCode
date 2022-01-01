// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

const func = (nums, target) => {
  let i = 0;
  let j = nums.length;

  while (true) {
    if (nums[i] + nums[j] == target) {
      return [i, j];
    }
    if (nums[i] + nums[j] < target) {
      i++;
      continue;
    } else {
      j--;
      continue;
    }
  }
};

const nums = [2, 7, 11, 15];
const target = 17;

console.log(func(nums, target));
