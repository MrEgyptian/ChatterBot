text='HI BSDKLFSDLKFSL'
z=text.split('\x20')
res=''
for (let i of z){
 res+=i[0].toUpperCase()
 res+=i.slice(1).toLowerCase()
 res+=' '
}
console.log(res)
