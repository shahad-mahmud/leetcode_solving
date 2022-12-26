class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # make the graph        
        wordList.append(beginWord)
        graph = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                graph[pattern].append(word)
        
        # do the bfs
        q = deque([beginWord])
        visited = {beginWord}
        res = 1
        
        while q:            
            for j in range(len(q)):
                head = q.popleft()
                if head == endWord:
                    return res
                
                for i in range(len(head)):
                    pattern = head[:i]+'*'+head[i+1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        return 0
        