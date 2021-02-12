// https://programmers.co.kr/learn/courses/30/lessons/43162
// 프로그래머스 #43162
// 네트워크
// solution code

func contains(n int, slice []int) bool {
	if slice == nil {
		return false
	}
	for _, v := range slice {
		if v == n {
			return true
		}
	}
	return false
}

func dfs(index int, visited *[]int, computers *[][]int) {
	for i, connection := range (*computers)[index] {
		if !contains(i, *visited) && connection == 1 {
			*visited = append(*visited, i)
			dfs(i, visited, computers)
		}
	}
}

func solution(n int, computers [][]int) int {

	count := 0
	var visited []int

	for i := 0; i < len(computers); i++ {
		if visited == nil || !contains(i, visited) {
			visited = append(visited, i)
			dfs(i, &visited, &computers)
			count += 1
		}
	}
	return count
}
