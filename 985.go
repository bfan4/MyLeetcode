package main

import (
	"fmt"
)

func main() {

	var A = []int{1, 2, 3, 4}
	fmt.Println(A)

	var queries = [4][2]int{{1, 0}, {-3, 1}, {-4, 0}, {2, 3}}

	fmt.Println(sumEvenAfterQueries(A, queries))

}

func sumEvenAfterQueries(A []int, queries [][]int) []int {

	var length int = len(A)

	var sum []int

	for i := 0; i < length; i++ {

		A[queries[i][1]] += queries[i][0]
		for j := 0; j < length; {
			if A[i]%2 == 0 {
				sum[i] += A[i]
				i++
			} else {
				i++
			}
		}
	}
	return sum

}
