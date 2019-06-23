//Square Every Digit
//Welcome. In this kata, you are asked to square every digit of a number.
//For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
//Note: The function accepts an integer and returns an integer

function squareDigits(num){
  return parseInt(num.toString().split('').map((eachNum)=>Math.pow(eachNum,2)).join(''));
}

console.log(squareDigits(9119));


//Square Every Digit python Version
import math

def square_digits(num):
     newArray=[]
     split=list(str(num))
     for i in split:
         newArray.append(str(int(math.pow(int(i),2))))
     return int("".join(newArray))
print square_digits(9119)


//Ruby Square Every Digit
def square_digits(num)
  splitted=num.to_s.split('')
  mathPow= Proc.new{ |x| x.to_i**2 }
 (splitted.collect(&mathPow).join('')).to_i
end

print(square_digits(3212))
