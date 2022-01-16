class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        chars = dict()
        ss_dict = dict()
        for c in word:
            ss_dict[c] = ss_dict.get(c, 0) + 1
        for col in range(0, len(board)):
            for row in range(0, len(board[0])):
                char = board[col][row]
                chars[char] = chars.get(char, 0) + 1
        # DFS
        for col in range(0, len(board)):
            for row in range(0, len(board[0])):
                if (self.existSubstring(col, row, board, word, [(col, row)], ss_dict, chars)):
                    return True
        return False
    
    def enoughChars(self, ss_dict, chars):
        for key in ss_dict:
            if (chars.get(key, 0) < ss_dict[key]):
                return False
        return True
    
    def existSubstring(self, col, row, board, ss, stack, ss_dict, chars):
        if (len(ss) == 0 or len(ss) == 1 and board[col][row] == ss):
            return True
        elif (ss[0] != board[col][row]):
            return False
        elif (not self.enoughChars(ss_dict, chars)):
            return False
        else:
            for (n_col, n_row) in self.getNeighborIndices(col, row, board, stack):
                stack.append((n_col, n_row))
                chars[board[col][row]] -= 1
                ss_dict[ss[0]] -= 1
                if (self.existSubstring(n_col, n_row, board, ss[1:], stack, ss_dict, chars)):
                    return True
                stack.pop()            
                chars[board[col][row]] += 1
                ss_dict[ss[0]] += 1
            return False
    
    def getNeighborIndices(self, col, row, board, stack):
        result = []
        if (col + 1 < len(board)):
            result.append((col + 1, row))          
        if (col - 1 >= 0):
            result.append((col - 1, row)) 
        if (row + 1 < len(board[0])):
            result.append((col, row + 1)) 
        if (row - 1 >= 0):
            result.append((col, row - 1)) 
        return list(filter(lambda idx: not idx in stack, result))
