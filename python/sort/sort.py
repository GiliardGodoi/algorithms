
class Sort():
    def sort(self, seq =[]):
        raise NotImplementedError()

class InsertionSort(Sort):
    def sort(self, seq =[]):
        for i in range(len(seq)):
            j = i
            while j > 0 and seq[j-1] > seq[j]:
                seq[j-1], seq[j] = seq[j], seq[j-1]
                j -= 1
        return seq

class SelectionSort(Sort):
    def sort(self, seq = []):
        for i in range(len(seq)-1, 0, -1):
            max_j = i
            for j in range(max_j):
                if seq[j] > seq[max_j]:
                    max_j = j
                seq[i],seq[max_j] = seq[max_j], seq[i]
        return seq

class QuickSort(Sort):
    def sort(self, seq = []):
        if len(seq) <= 1:
            return seq
        pivot = seq[len(seq) // 2]
        left = [x for x in seq if x < pivot]
        middle = [x for x in seq if x == pivot]
        right = [x for x in seq if x > pivot]
        return self.sort(left) + middle + self.sort(right)

if __name__ == "__main__":
    s = Quicksort()
    print(s.sort([3,6,8,10,1,2,1]))