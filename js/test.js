var longestPalindrome = function(s) {
    if (s.length == 1) return s;
    var copy = s;
    var reversed = copy.split('').reverse().join('');
    var i;
    var len = s.length;
    for (i=0; i<len; i++) {
        if (s.slice(0, len-i) == reversed.slice(i)) {
            if (i < len - 1) {
                return reversed.slice(i);
            } else {
                return longestPalindrome(s.slice(1));
            }
        }
    }
};
console.log(longestPalindrome('aaaabaaa'));