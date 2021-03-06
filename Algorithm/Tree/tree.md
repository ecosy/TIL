# Tree
> 계층형 트리 구조를 시뮬레이션 하는 추상 자료형(ADT)으로, 루트 값과 부모-자식 관계의 서브트리로 구성되며, 서로 연결된 노드의 집합이다.


## 1. 트리
### (1.1) 개요
* 재귀로 정의된(Recursively Defined) 자기 참조 (Self-Referential) 자료구조
  * 자식도 트리고 또 그 자식도 트리임 (Subtrees)
---
### (1.2) 트리의 각 명칭
1. Node : 트리에서 데이터를 저장하는 기본 요소
2. Root Node : 트리 맨 위에 있는 노드, 
3. Level : 최상위 노드를 Level 0으로 하며, 하위로 내려갈수록 커짐
4. Parent Node : 어떤 노드의 상위 레벨에 연결된 노드
5. Child Node : 어떤 노드의 하위 레벨에 연결된 노드
6. Leaf Node : Child Node가 하나도 없는 노드
7. Sibling : 동일한 Parent Node를 가진 노드
8. Depth : 루트에서부터 현재 노드까지의 거리
9. Height : 현재 위치에서부터 Leaf까지의 거리
10. Degree 차수 : 자식 노드의 개수
11. Size 크기 : 자신을 포함한 모든 자식 노드의 개수
---
### (1.3) 그래프 vs 트리
Graph | Tree
--- | ---
순환 구조, 비순환 구조 모두 허용 | 순환 구조를 갖지 않는 그래프
단방향, 양방향 가리킬 수 있음 | 단방향만 가능함
---
## 2. 이진 트리
* 각 노드가 m개 이하의 자식을 갖고 있으면, m-ary 트리 (다항트리, 다진트리) 라고 함
* 이때 m=2인 경우, 모든 노드의 차수가 2 이하일 때 이진 트리 Binary Tree 라고 함  

* Full Binary Tree 정 이진 트리
  * 모든 노드가 0개 또는 2개의 자식 노드를 가짐
* Complete Bianry Tree 완전 이진 트리
  * 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있음
  * 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있음
* Perfect Binary Tree 포화 이진 트리
  * 모든 노드가 2개의 자식 노드를 가짐
  * 모든 리프 노드가 동일한 깊이, 레벨을 가짐
---
### (2.1) 이진 탐색 트리 (Binary Search Tree)
* 이진 탐색 트리는 정렬된 트리임
  * 노드의 왼쪽 서브트리는 그 노드의 값보다 작은 값들을 지닌 노드로 이루어짐
  * 노드의 오른쪽 서브트리는 그 노드의 값과 같거나 큰 값들을 지닌 노드로 이루어짐
* 탐색 시 시간복잡도 : O(log _n_)
  * 트리의 균형이 깨질 경우 O(_n_)에 근접한 시간이 소요됨
  * 따라서 균형을 맞추기 위해서 _자가 균형 이진 탐색 트리_ 가 고안됨

#### 자가 균형 이진탐색 트리 (Self-Balancing Search Tree)
> 자가 균형 (높이 균형) 이진 탐색 토리는 삽입, 삭제 시 자동으로 높이를 작게 유지하는 노드 기반의 이진 탐색 트리다.
* (e.g.) AVL 트리, 레드-블랙 트리
  * 레드-블랙트리는 높은 효율성 때문에 실무에서도 빈번하게 사용됨

---
## 3. 트리 순회 (Tree Traversals)
> 그래프 순회의 한 형태로 트리 자료구조에서 각 노드를 정확히 한 번 방문하는 과정
* DFS, BFS로 탐색하며, 이진트리에서 DFS로 노드를 방문하는 순서에 따라 3가지 방식 존재함
  * 전위 순회 (Pre-Order), (NLR)
  * 중위 순회 (In-Order), (LNR)
  * 후위 순회 (Post-Order), (LRN)

<p align="center">
<img src = "../../images/tree_traversal_00.png" alt='Graph' width="40%" height='40%' class='center'>  
</p>

```python
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

root = Node('F',
            left = Node('B',
                        left = Node('A'),
                        right = Node('D',
                                    left = Node('C'),
                                    right = Node('E'))
                        ),
            right = Node('G',
                        left = None,
                        right = Node('I',
                                    left = Node('H'))
                        )
        )

```

### (3.1) 전위 순회
```python
def preorder(node):
  if node is None:
    return
  print(node.val)
  preorder(node.left)
  preorder(node.right)
# result : F - B - A - D - C - E - G - I - H
```

### (3.2) 중위 순회
```python
def inorder(node):
  if node is None:
    return
  inorder(node.left)
  print(node.val)
  inorder(node.right)
# result : A - B - C - D - E - F - G - H - I
```

### (3.3) 후위 순회
```python
def postorder(node):
  if node is None:
    return
  postorder(node.left)
  postorder(node.right)
  print(node.val)
# result : A - C - E - D - B - H - I - G - F
```

---
##  Reference
1. 파이썬 알고리즘 인터뷰 (저자 : 박상길) Shortest Path 편
2. https://www.fun-coding.org/Chapter20-shortest-live.html