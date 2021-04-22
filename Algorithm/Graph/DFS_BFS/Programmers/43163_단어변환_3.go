// https://programmers.co.kr/learn/courses/30/lessons/43163
// 프로그래머스
// 단어변환
// 3번째 풀이 in GoLang

package main

import "fmt"

func contains(word string, words []string) bool {
	for _, v := range words {
		if word == v {
			return true
		}
	}
	return false
}

func solution(begin string, target string, words []string) int {
	var minCount int = -1
	var dfs func(word string, visited *[]string)

	// nested function
	dfs = func(word string, visited *[]string) {
		// termination condition
		if word == target {
			// update minCount
			if len(*visited) < minCount || minCount < 0 {
				minCount = len(*visited)
			}
			return
		}

		// 1글자 차이 단어 찾기
		for _, w := range words {
			if w == word {
				continue
			}

			diffCount := 0
			for i := 0; i < len(word); i++ {
				if word[i] != w[i] {
					diffCount++
				}
			}
			// word 1 글자만 다른 경우 dfs 실행
			if diffCount == 1 && !contains(w, *visited) {
				*visited = append(*visited, w)
				dfs(w, visited)
				*visited = (*visited)[:len(*visited)-1]
			}
		}
	}

	// target이 존재하지 않는 경우
	if !contains(target, words) {
		return 0
	}

	dfs(begin, &[]string{})

	// target에 도달할 수 없는 경우
	if minCount < 0 {
		return 0
	}
	return minCount
}

func main() {
	begin := "hit"
	target := "cog"
	words := []string{"hot", "dot", "dog", "lot", "log", "cog"}

	answer := solution(begin, target, words)
	fmt.Println("answer : ", answer)
}
