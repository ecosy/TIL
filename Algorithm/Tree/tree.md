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
### (1.4) 이진 트리
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

##  Reference
1. 파이썬 알고리즘 인터뷰 (저자 : 박상길) Shortest Path 편
2. https://www.fun-coding.org/Chapter20-shortest-live.html