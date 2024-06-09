const fs = require('fs')

const table = ' .#@'.split('')
const len = 64
const dig = 2

let data = ''
let raw = fs.readFileSync('./map.input', 'utf-8').split('\n')
let width = 0, height = raw.length
for (let i = 0; i < height; i ++) {
    let v = raw[i]
    if (i == 0) {
        width = v.length
    }
    else if (v.length > width) {
        throw new Error('Map over size.')
    }
    else {
        while (v.length < width) {
            v += ' '
        }
    }
    data += `-${v}-\n`
}

fs.writeFileSync('./map.0', data)

let res = Buffer.alloc(Math.ceil(data.length * dig / (len / dig)), 0)
let p = 0
let buf = []
for (let i = 0; i < data.length; i ++) {
    let v = data[i]
    buf.push(table.indexOf(v))
    if (buf.length >= len) {
        let n = 0, a, j = 0
        while (a = buf.pop()) {
            n |= a << j * dig
            i ++
        }
        res[p ++] = n
    }
}

fs.writeFileSync('./map.dat', res)
