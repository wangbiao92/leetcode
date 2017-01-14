var reverseVowels = function (s) {
    vowels = {"a":true, "o":true, "e":true, "i":true, "u":true, "A":true, "O":true, "E":true, "I":true, "U":true};
    i = 0;
    j = s.length - 1;
    l = s.split();//字符串转成数组
    while (i < j) {
        if (l[i] in vowels && l[j] in vowels) {
            i++;
            j--;
        }
        if (!(l[i] in vowels)) {
            i++;
        }
        if (!(l[j] in vowels)) {
            j--;
        }
        t = l[i];
        l[i] = l [j];
        l[j] = t;
    }  
    return l.join("");//数组转成字符串
};