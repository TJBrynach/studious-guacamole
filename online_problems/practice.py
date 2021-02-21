# Two Sum LC
# BruteForce
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and i!=j:
                    return [i,j]

def twoSum_2(self, nums: List[int], target: int) -> List[int]:
    hash = {} #init dictionary 
    for i in range(len(nums)): # looping through the list of numbers
        complement = target - nums[i]       # finding the comp number to the target
        if complement in hash:  # if the comp is in the dictionary
            return [hash[complement],i] # return the hash with the position
        else:
            if nums[i] in hash: # if the number is in hash
                continue
            hash[nums[i]] = i

def isPalindrome(self, x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False

# Count of matches in tournament

def numberOfMatches(self, n: int) -> int:
    count = 0
    while n >= 2:
        if n % 2 == 0:
            count += n/2
            n = n/2
        elif n % 2 == 1:
            count += (n - 1)/2
            n = (n-1)/2 + 1
    return int(count)

def singleNumber(nums):
    dict1 = {}
    for i in nums:
        dict1.get(i,None)
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    for key, values in dict1.items():
        if values == 1:
            return key
            
#####################
from collections import defaultdict
def singleNumber(self, nums: List[int]) -> int:
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
    
    for i in hash_table:
        if hash_table[i] == 1:
            return i

####################
#1221. Split a String in Balanced Strings
# First attempt 32ms, 14.4mb


def balancedStringSplit(self, s: str) -> int:
    # balanced strings are those who have equal quantity of L and R characters.
    # Given a balanced string s, split it in the max amount of balanced strings. return max amount of b strings
    # "-RL-RRLL-RL-RL-" returns 4 
    
    count = num = 0
    for char in s:
        if char == "R":
            num += 1
            if num == 0:
                count += 1
        elif char == "L":
            num -= 1
            if num == 0:
                count += 1
    return count

                
#################
#1185. Day of the Week


def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    day_of_week = { 0: "Sunday",
                    1: "Monday",
                    2: "Tuesday",
                    3: "Wednesday",
                    4: "Thursday",
                    5: "Friday",
                    6: "Saturday"   }
    month_of_year = {   1:  0,
                2:  3,
                3:  3,
                4:  6,
                5:  1,
                6:  4,
                7:  6,
                8:  2,
                9:  5,
                10: 0,
                11: 3,
                12: 5   }
    
    century = { 17: 4,
                18: 2,
                19: 0,
                20: 6,
                21: 4,
                22: 2,
                23: 0    }
    yy, cc = int(str(year)[-2:]), int(str(year)[:2])
    year_code = yy + (yy /4) % 7
    month_code = month_of_year.get(month)
    century_code = century.get(cc)
    leap_year_code = 0
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        if month <= 2:
            leap_year_code = 1
            
    x = (year_code + month_code + century_code + day - leap_year_code) % 7 

    return day_of_week.get(int(x))

########
# 326. Power of Three

def isPowerOfThree(self, n: int) -> bool:
    if n == 1 or n==3:
        return True
    else:
        while n >= 3:
            n /= 3
            if n == 3:
                return True
        return False

#########
# 83. Remove Duplicates from Sorted List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode):
    currentNode = head
    while currentNode != None and currentNode.next != None:
        if currentNode.val == currentNode.next.val:
            currentNode.next = currentNode.next.next  #Skipping the replicate node
        else:
            currentNode = currentNode.next #moving to the next node 
    return head


# 387. First Unique Character in a String
# first attempt

def firstUniqChar(self, s: str) -> int:
        hash = {}
        for char in s:
            hash.get(char,None)
            if char not in hash:
                hash[char] = 1
            else:
                hash[char] += 1
        letter = ''
        for key, values in hash.items():
            if values == 1:
                letter = key
                break
        
        for char in range(len(s)):
            if s[char] == letter:
                return char

# given solution on leetcode

def firstUniqChar(self, s: str) -> int:
    count = collections.Counter(s) # the counter function within the collecitons modeule keeps track of how many times  equiv values are added.

    for index, char in enumerate(s):
        if count[char] == 1:
            return index
    return -1


# 217 Duplicates 

def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

#   OR the dictionary method

def containsDuplicate(self, nums: List[int]) -> bool:
    hash = {}
    for i in nums:
        hash.get(i,None)
        if i not in hash:
            hash[i] = 1
        else:
            return True
    return False

# 218 Majority Element

def majorityElement(self, nums: List[int]) -> int:
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)



# 1748. Sum of Unique Elements

def sumOfUnique(self, nums: List[int]) -> int:
    hash = {}
    sum = 0
    
    for i in nums:
        hash.get(i, None)
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    
    for value, key in hash.items():
        if key == 1:
            sum += value
    return sum

# The entire first for loop to generate your python dictionary can be replaced with collection function
# Counter <-------

def sumOfUnique(self, nums: List[int]) -> int:
    sum = 0
    x = Counter(nums)
    
    for value, key in x.items():
        if key == 1:
            sum += value
    return sum