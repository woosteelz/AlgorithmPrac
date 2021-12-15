function solution(s) {
    var answer = [];
    let temp = [];
    let a = "";

    for (let i = 0; i < s.length; i++) {
        if (s[i] === "{" || s[i] === "}") {
            continue;
        } else if (s[i] === ",") {
            temp.push(parseInt(a))
            a = "";
        } else a = a + s[i];
    }
    if (a.length > 0) temp.push(parseInt(a))

    console.log(temp)

}