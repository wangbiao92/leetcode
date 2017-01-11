/**
 * @param {string} s
 * @return {string}
 */
/*
字符串的索引string.charAt()
 */
var reverseString = function(s) {
    var rstring = "";
    leng = s.length - 1;
    for (var i = leng; i >= 0; i--){
        rstring += s.charAt(i);//s.[i] IE8+版本可以使用
    }
    return rstring;
};