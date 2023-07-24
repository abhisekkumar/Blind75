# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        count_list = list(count.items())
        count_list.sort(key=lambda x: x[1], reverse=True)
        return (x[0] for x in count_list[:k])



"""
Here is how the count dictionary would be updated during the iteration:
On the first iteration, num is 1, so count[1] = count.get(1, 0) + 1 is executed. Since 1 is not yet in the count dictionary, count.get(1, 0) returns 0, so count[1] is set to 1.
On the second iteration, num is 1 again, so count[1] = count.get(1, 0) + 1 is executed. This time, 1 is already in the count dictionary, so count.get(1, 0) returns 1, so count[1] is incremented to 2.
On the third iteration, num is 2, so count[2] = count.get(2, 0) + 1 is executed. Since 2 is not yet in the count dictionary, count.get(2, 0) returns 0, so count[2] is set to 1.
On the fourth iteration, num is 3, so count[3] = count.get(3, 0) + 1 is executed. Since 3 is not yet in the count dictionary, count.get(3, 0) returns 0, so count[3] is set to 1.
On the fifth iteration, num is 3 again, so count[3] = count.get(3, 0) + 1 is executed. This time, 3 is already in the count dictionary, so count.get(3, 0) returns 1, so count[3] is incremented to 2.
On the sixth iteration, num is 3 again, so count[3] = count.get(3, 0) + 1 is executed. This time, 3 is already in the count dictionary, so count.get(3, 0) returns 2, so count[3] is incremented to 3.
On the seventh iteration, num is 4, so count[4] = count.get(4, 0) + 1 is executed. Since 4 is not yet in the count dictionary, count.get(4, 0) returns 0, so count[4] is set to 1.
On the eighth iteration, num is 4 again, so count[4] = count.get(4, 0) + 1 is executed. This time, 4 is already in the count dictionary, so count.get(4, 0) returns 1, so count[4] is incremented to 2.
On the ninth iteration, num is 4 again, so count[4] = count.get(4, 0) + 1 is executed. This time, 4 is already in the count dictionary, so count.get(4, 0) returns 2, so count[4] is incremented to 3.
On the tenth iteration, num is 4 again, so count[4] = count.get(4, 0) + 1 is executed. This time, 4 is already in the count dictionary, so count.get(4, 0) returns 3, so count[4] is incremented to 4.
So after the iteration, the count dictionary would look like this: {1: 2, 2: 1, 3: 3, 4: 4}. This means that element 1 occurred twice, element 2 occurred once, element 3 occurred thrice and element 4 occurred four times in the input array.
With this count dictionary, we can easily find the k most frequent elements by sorting the dictionary by the occurrences and returning the first k elements.
"""