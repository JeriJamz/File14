let i;// let is one way to decalre a varible
i = 0;
console.log(i)
i = i + 1;
console.log(i);

const e = 3;//this is how u make a var an immuatable data type
console.log(e)

const arr = ['Hello','World'];//i think this is a list
for (const elem of arr){
    console.log(elem);
}

const f = () => g();
const g = () => 123;
 
console.log(f);
console.log(g);