
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

if __name__ == "__main__":
    s = Sort()