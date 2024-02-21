function factorial(num) {
  if(num == 0){
    return 1
  }
  else{
    let answer = num*(num-1)*(num-2)
    return answer;
  }


}

module.exports = factorial;
