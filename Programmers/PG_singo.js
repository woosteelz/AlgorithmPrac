const solution = (id_list, report, k) => {
    let ans = [];

    let stop = [];
    let singo = {};
    let mail = {};

    report.map((temp) => {
        let { a, b } = temp.split();
        if (a in mail) {
            mail[a].add(b)
        } else {
            mail[a] = new Set();
            mail[a].add(b)
        }
        if (b in singo) {
            singo[b].add(a)
        } else {
            singo[b] = new Set();
            mail[b].add(a);
        }
    })

    for (let key in singo) {
        if (singo[key].length >= k) stop.push(key)
    }

    console.log(mail)

    // id_list.map((id) => {
    //     let cnt = 0;
    //     for (let item of mail[id]) {
    //         if (item in stop) cnt++;
    //     }
    //     ans.push(cnt);
    // })
    return ans
}