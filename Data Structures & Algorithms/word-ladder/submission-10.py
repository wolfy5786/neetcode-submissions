class Node:
    def __init__(self, word, edges):
        self.word = word
        self.edges = edges
        self.parent = None

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        wordList = list(set(wordList))
        i = 0
        nodes = {}
        if endWord not in wordList:
            return 0

        for word in wordList:
            nodes[word] = Node(word, [])


        while i < len(wordList):
            j = i + 1
            while j < len(wordList):
                if self.isNeighbour(wordList[i], wordList[j]):
                    nodes[wordList[i]].edges.append(wordList[j])
                    nodes[wordList[j]].edges.append(wordList[i])

                j = j + 1
            i = i + 1 

        for k,n in nodes.items():
            print(k,n.edges)
        return self.bfs(nodes, beginWord, endWord)

    
    def bfs(self, nodes,start, end):
        length = 0
        if start == end:
            return length

        visited = {}
        visited[start] = True
        next = []
        next.append(start)

        for n in next:
            if n == end:
                break
            visited[n] = True
            for e in nodes[n].edges:
                if e not in visited:
                    next.append(e)
                    nodes[e].parent = n
                    visited[e] = True


        while end != start:
            if end is None:
                return 0
            print(end)
            end = nodes[end].parent
            length = length + 1

        return length + 1



    def isNeighbour(self, word_1, word_2):
        result = False
        i = 0
        allow = 1 
        while i < len(word_1):
            if word_1[i] != word_2[i]:
                allow = allow - 1
        
            i = i + 1

        if allow==0:
            result = True
        return result
    
