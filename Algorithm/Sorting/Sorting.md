# Sorting
> 목록의 요소를 특정 순서대로 넣는 알고리즘이다. 숫자식 Numerical Order, 사전식 Lexicographical Order 로 정렬한다.

## 1. 버블 정렬 (Bubble Sort)
> 인접한 두 수를 비교하여, 만약 앞의 수가 뒤보다 더 크면 서로의 순서를 바꾼다.
* 안정 정렬 (Stable Sort)
* 시간복잡도 : O(n<sup>2</sup>)

```python
def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A)-1):
            if A[j] > A[j + 1]:
                A[j], A[j+1] = A[j + 1], A[j]
```

## 2. 병합 정렬 (Merge Sort)
> 숫자 리스트를 쪼갤 수 없을 때까지 계속 분할한 후, 정렬하면서 정복해 나간다.

* 존 폰 노이만이 고안했으며, 분할 정복 (Divide and Conquer) 알고리즘
* 최선과 최악의 경우 O(nlogn)
* 안정 정렬 (Stable Sort)

## 3. 퀵 정렬 (Quick Sort)
> 피벗을 기준으로 작으면 왼쪽, 크면 오른쪽으로 파티셔닝 하면서 쪼갠다.
* 매우 빠르고 효율적이지만, 최악의 경우 O(n<sup>2</sup>)

```python
def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)
```
---
## Reference
1. 파이썬 알고리즘 인터뷰 (저자 : 박상길) Sorting 편
2. https://www.fun-coding.org/Chapter15-mergesort.html