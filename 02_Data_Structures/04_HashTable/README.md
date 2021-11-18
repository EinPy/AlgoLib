# HASH TABLE #
This is truly a great data structure.
Hsing a value is the same as storing it a unique place in memory with a
key that points directly to that value. The trick here is that one needs a hashing
function that gives unique places in memory for unique keys. I will not go further
into detail here and instead suggest the use of a Pyton dictionary that fills the
function of a Hash Map. 

A great example of the use of a Hash table is for this problem. 
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

with the solution: 
´´´Python3
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) -1
        while p1<p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1+1,p2+1]
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                p1 += 1
´´´
