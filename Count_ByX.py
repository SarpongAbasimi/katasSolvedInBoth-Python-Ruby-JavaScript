#Ruby Solution for Kata
def count_by(x, n)
  array=[]
  1.upto(x * n) do |num|
    num % x == 0 ? array << num : ''
  end
  array
end

puts count_by(4,5)


#Javascript solution for Kata
function countBy(x, n) {
  const myArray=[];
  const mul =x*n;

  for(let i = 1; i < mul+1 ; i++){
    if (i % x == 0) myArray.push(i)
  }
  return myArray
}
console.log(countBy(2,5));



#Python Solution For Kata
import unittest

def count_by(x, n):
    mylist=[]
    for i in range(1,(x*n)+1):
        if(i % x==0):
            mylist.append(i)
    return mylist

class unittesing(unittest.TestCase):

    def test_is_count(self):
        self.assertEqual(count_by(1,5),[1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()
