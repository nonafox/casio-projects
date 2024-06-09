const fs = require('fs')

const alp = 'abcdefghijklmnopqrstuvwxyz'.split('')
function numeric(str) {
    let res = ''
    for (let v of str) {
        let i = alp.indexOf(v.toLowerCase()) + 1
        i = i < 10 ? '3' + i : '' + i
        res += i
    }
    return res
}
function charcodes(str = '') {
    let res = []
    for (let v of str) {
        res.push(v.toLowerCase().charCodeAt(0))
    }
    return res.sort().toString()
}

let lines = fs.readFileSync('./ori.csv', 'utf8').split('\n')
let res = ''
let i = 1
let table = {}
for (let k in lines) {
    let v = lines[k].replace(/^\s/g, '').replace(/\s$/g, '')
    let w = v.split(',')
    if (w[0].match(/^[a-zA-Z]+$/) && w[0].length == 6) {
        res += w[0] + '\n'
        let cc = charcodes(w[0])
        if (cc in table) {
            table[cc].push(w[0])
        }
        else {
            table[cc] = [w[0]]
        }
        i ++
    }
}
let table_ = {}
for (let i in table) {
    let v = table[i]
    if (v.length < 2) {
        continue
    }
    for (let k2 in v) {
        let v2 = v[k2]
        let tmp = Object.assign([], v)
        tmp.splice(k2, 1)
        table_[v2] = tmp
    }
}
res = res.replace(/\s$/, '')
fs.writeFileSync('./words.txt', res)
fs.writeFileSync('./isomers.json', JSON.stringify(table_))
