//*  Set is like an array, but it has no particular order and, cant have duplicate items

//Set constructor function
let abc = new Set(['a','random','set','with',6,'elements','set','random','khala'])

// checking duplicate items
console.log(abc.size) //this only counts the unique values of the set

for (items of abc) {
    console.log(items); //this iteration returns unique values of set
}