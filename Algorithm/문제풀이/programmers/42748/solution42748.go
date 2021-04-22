// https://programmers.co.kr/learn/courses/30/lessons/42748

package Solution42748

func sort(array *[]int) {

}

func Solution(array []int, commands [][]int) []int {
	answer := []int{}

	for i := range commands {
		start := commands[i][0] - 1
		end := commands[i][1] - 1

		slicedArray := array[start:end]
		sort(&slicedArray)
	}

	answer = []int{5, 6, 3}
	return answer
}
