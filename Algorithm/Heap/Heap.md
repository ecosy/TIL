# Heap
> 힙의 특성 (최소 힙 Min Heap에서는 부모가 항상 자식보다 작거나 같다)을 만족하는
거의 완전한 트리 Almost Complete Tree인 특수한 트리 기반의 자료구조다.

## 1. 힙
* 트리 기반의 자료구조

```python
class BinaryHeap(object):
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] =\
                    self.items[i], self.items[parent]
            i = parent
            parent = i // 2
    
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
    
    def _percolate_down(self, idx):
        left = idx * 2
        right  idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        
        if smallest != idx:
            self.items[idx], self.items[smallest] =\
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
    
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
```
(Reference 1)

---
## Reference
1. 파이썬 알고리즘 인터뷰 (저자 : 박상길) Heap 편
2. https://www.fun-coding.org/Chapter11-heap.html