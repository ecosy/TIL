# https://leetcode.com/problems/longest-univalue-path/
# leetcode #687
# 가장 긴 동일 값의 경로

#%%
class Solution: 
    result: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            # left, right 각각에서 제일 깊은 동일 경로 개수 리턴
            left_count = dfs(node.left)
            right_count = dfs(node.right)

            # left child 와 value가 같다면 개수 + 1
            if node.left and node.val == node.left.val:
                left_count += 1
            else:
                left_count = 0
            
            # right child 와 value가 같다면 개수 + 1
            if node.right and node.val == node.right.val:
                right_count += 1
            else:
                right_count = 0
            
            # 결과 값을 최대 동일 경로로 갱신
            self.result = max(self.result, left_count + right_count)

            # left, right 중 더 긴 동일 경로 리턴
            return max(left_count, right_count)
            
        dfs(root)
        return self.result

#%%
# 책 풀이 분석 1
class Solution:    
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: Treenode):
            if node is None:
                return 0
        
            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)

            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)
    
    dfs(root)
    return self.result