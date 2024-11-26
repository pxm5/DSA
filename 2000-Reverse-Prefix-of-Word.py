class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        c = 0
        
        while c < len(word):
            stack.append(word[c])
            if word[c] == ch:
                break
            c+=1
        if c == len(word):
            return word
        out = ''
        for i in range(len(stack)-1, -1, -1):
            out += stack[i]
        return out + word[c+1:]
