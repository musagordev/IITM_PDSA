#Function takes list of suffix. Returns list of lists which can be apply construct word seeking with function.

def constructWord(word, wordList):
    def helper(target, memo):
        if target in memo:
            return memo[target]
        
        if target == '':
            return[[]]
        
        result = []
        
        for w in wordList:
            if target.startswith(w):
                suffix = target[len(w):]
                suffixWays = helper(suffix, memo)
                
                for way in suffixWays:
                    result.append([w] + way)
        memo[target] = result
        return result
    return helper(word, {})
