// This is a file to learn data structure and algorithms using JS

//! stack
// keywords; PUSH, POP, length, shift

//* push = pushes something to the array
//* pop = drops the last item of the array, so it works as a selector of the last item
//* shift = selects the first item and drops it.
//? peek was previously used as shift but its depricated.

// palindrome checker
let word = "lieutenant"
let word_arr = []
let r_word = []

// pushing the letters of the stack in original order
for (let i = 0; i < word.length; i++) {
    word_arr.push(word[i])
}
console.log(word_arr)

for (let i = 0; i < word.length; i++) {
    r_word += word_arr.pop()
}

console.log("Given word: " + word)
if (r_word == word) {
    console.log(word +" is Palindrome");
}
else{
    console.log(word + " is not palindrom")
}


