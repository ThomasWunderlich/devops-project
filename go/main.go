package main

import (
	"io"
	"net/http"
	"strconv"
	"strings"
)

// Fibonacci returns the first `n` Fibonacci numbers
func Fibonacci(n int) []int {
	// TODO: Fill this function out
	return nil
}

// getFibs is the response handler for the web server
func getFibs(w http.ResponseWriter, r *http.Request) {
	param, ok := r.URL.Query()["n"]
	if !ok || len(param[0]) < 1 {
		w.WriteHeader(http.StatusUnprocessableEntity)
		return
	}

	n, err := strconv.Atoi(param[0])
	if err != nil {
		w.WriteHeader(http.StatusUnprocessableEntity)
		return
	}

	nums := Fibonacci(n)
	strNums := make([]string, len(nums))

	// convert nums from int to string array
	for i, num := range nums {
		strNums[i] = strconv.Itoa(num)
	}

	finalNums := strings.Join(strNums, ", ")
	io.WriteString(w, finalNums)
	return
}

func main() {
	http.HandleFunc("/", getFibs)
	http.ListenAndServe(":8000", nil)
}
