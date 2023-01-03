def wordPattern(pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        hashtable = {} 
        for i in range(0, len(s)):
            if pattern[i] not in hashtable:
                hashtable[pattern[i]] = s[i]
            else:
                if hashtable[pattern[i]] != s[i]:
                        print(hashtable)
                        return False

        print(hashtable)
        return True



testcaseOne = ['abba', 'dog cat cat fish']
testcaseTwo = ['abba', 'dog cat cat dog']
testcaseThree = ['aaaa', 'dog cat cat dog']
testcaseFour = ['ab', 'dog cat cat dog']


if wordPattern(testcaseOne[0], testcaseOne[1]) == False:
        print('Test Case One - Passed')
else:
        print('Test Case One - Failed')

if wordPattern(testcaseTwo[0], testcaseTwo[1]) == True:
        print('Test Case Two - Passed')
else:
        print('Test Case Two - Failed')

if wordPattern(testcaseThree[0], testcaseThree[1]) == False:
        print('Test Case Three - Passed')
else:
        print('Test Case Three - Failed')

if wordPattern(testcaseFour[0], testcaseFour[1]) == False:
        print('Test Case Four - Passed')
else:
        print('Test Case Four - Failed')


hasmap = {'p' : 'q'}

hasmap[testcaseFour[0]] = testcaseFour[1]

print(hasmap[testcaseFour[0]])
