# javascript
function mergeArrays(arr1, arr2) {
let allArrayElement=[...arr1,...arr2];

const myNumbers= allArrayElement.reduce((acc,cur)=> {

if (acc.includes(cur)){

}else {
  acc.push(cur)
}
return acc
},[]);
return myNumbers.sort((a,b)=>a-b);
}

console.log(mergeArrays([1,1,2,3,4], [5,6,7,8]))

#ruby
def merge_arrays(arr1, arr2)
  concatArray = arr1.concat(arr2)
  return concatArray.uniq.sort {|x,y| x <=> y}
end

puts (merge_arrays([1,1,2,3,4], [5,6,7,8]))

#python
import unittest

def merge_arrays(arr1, arr2):
    return sorted((set(arr1 + arr2)))


print (merge_arrays([6, 2, 3, 4], [5,5,5, 6, 7, 8]))

#test for function
class testFucn(unittest.TestCase):

    def test_if_equal(self):
        self.assertEquals(merge_arrays([3,6,7,8],[3,4,5,7]),[3,4,5,6,7,8])
        self.assertEquals(merge_arrays([0,4,10,8],[7,4,30,7]),[0,4,7,8,10,30])



if __name__ == '__main__':
    unittest.main()
