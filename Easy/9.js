// Palindrome number

// 242 is palindrome number

const isPalindrome = (num) => {
  let newNum = "";
  let x = num.toString();

  for (let i = 0; i < x.length; i++) {
    newNum += x[x.length - i - 1];
  }

  if (x == newNum) {
    console.log(`${num} is a polindrome number\n`);
    return true;
  } else {
    console.log(`${num} is not a polindrome number\n`);
    return false;
  }
};

const nums = [123, 2, 14, 141, 929, 923, 1001];
nums.map(function (num, index) {
  console.log(index);
  isPalindrome(num);
});
