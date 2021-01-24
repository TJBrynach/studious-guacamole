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


