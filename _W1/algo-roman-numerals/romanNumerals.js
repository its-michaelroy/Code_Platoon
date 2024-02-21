/**
1. Write a function `toRomanLazy` that takes in a single input, `num`(an arabic number). Note: this step has already been done for you.

2. Create a variable `output` and set it's initial value to the empty string (`""`)

3. Create a variable `romanNumeralToArabic` that holds an object mapping the key of a roman numeral (`V`) to it's arabic equivalent (`5`)

4. Create a variable `romanNumeralPriorityOrder` that holds an array with the roman numerals in descending order (`['M', 'D', 'C' ...]`)

5. Iterate through `romanNumeralPriorityOrder`

6. Use division and `Math.floor` to find out how many times a given `num` can be divided by the arabic equivalent of the current romanNumeral being iterated through. Append this many of the given romanNumeral to the `output`

7. Subtract `num` by that number so only the remaining portion that couldn't be divided is left.

8. Continue iterating until `num === 0`

9. return `output`

## Step 1: Lazy Roman Numerals

Given a number in today's numbers, (Arabic Numeral), return its equivalent in Roman Numerals in the lazy way. Lazy Roman Numerals is where Roman Numerals are added together (9 is `VIIII`, 4 is `IIII`). Here are Roman Numerals with their Arabic Numeral counterparts:
**/
let output = '';
let romanNumeralToArabic = {
  'M':1000,
  'D':500,
  'C':100,
  'L':50,
  'X':10,
  'V':5,
  'I':1
}
let romanNumeralPriorityOrder = ['M','D','C','L','X','V','I']

function toRomanLazy(num) {
  let iteration = 0;

  for (el of romanNumeralPriorityOrder) {
      let arabicNum = romanNumeralToArabic[el]
      //console.log(`arabicNum ${arabicNum}`)
      let count = Math.floor(num/arabicNum)
      //console.log(`can be divided ${count} times`)
      if(count > 0){
        let letter = romanNumeralPriorityOrder[iteration]
        //console.log(letter)
        output += letter.repeat(count)
        count = 0;
        num -= arabicNum;
        //console.log(`output is now ${output}`)
      }iteration ++
      //console.log(`at the end output is ${output}`)
//4 /value of obj
  }
  return output;//5 > V
}

function toRoman(num) {
  return "";
}

//module.exports = { toRoman, toRomanLazy };

//console.log(toRomanLazy(1667))
