package preprocess

import "testing"

func BenchmarkSolution1Origin(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Solution1Origin()
	}
}

func BenchmarkSolution1GoRoutine(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Solution1GoRoutine()
	}
}

func BenchmarkSolution2Origin(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Solution2Origin()
	}
}

func BenchmarkSolution2GoRoutine(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Solution2GoRoutine()
	}
}

func BenchmarkSolution3(b *testing.B) {
	for i := 0; i < b.N; i++ {
		solution3()
	}
}
