class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #define hashtable
        wordsFrequencies = {}
        
        #count the words frequencies
        for i in  words:
            if i in wordsFrequencies:
                wordsFrequencies[i] += 1
            else:
                wordsFrequencies[i] = 1

        #create a max heap
        max_heap = [(-wordsFrequencies[word],word) for word in wordsFrequencies]
        heapq.heapify(max_heap)

        #pop the first k elements from the heap (max frequency) and add them to the results arrey
        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
        
        #return the results array which contains the Top K Frequent Words
        return result
