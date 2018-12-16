#python
import unittest


def divisors(n):
    mylist=[]
    myFuntion=lambda (x) : n % x == 0
    for i in range(1,n+1):
        mylist.append(i)
    ans =filter(myFuntion,mylist)
    return len(ans)

#test for function
class TestDivisors(unittest.TestCase):

    def test_divisors(self):
        self.assertEquals(divisors(10),4)
        self.assertEquals(divisors(5),2)

if __name__ == '__main__':
    unittest.main()

#Ruby Solution
def divisors(n)
  #get all num upTo the number
  myArray = []
  myProc = Proc.new { |x| myArray << x if n % x == 0  }
  1.upto(n) do |num|
    localArray= Array.new << num
    localArray.each(&myProc)
  end
  return myArray.count
end
puts divisors(11)


#JavaScript solutuion
nction getDivisorsCnt(n){
  const myArray=[];
  let count = 1;
  while(count < (n+1)){
    myArray.push(count);
    count++;
  }
  return (myArray.filter((value)=>n % value == 0)).length
}

console.log(getDivisorsCnt(10))
