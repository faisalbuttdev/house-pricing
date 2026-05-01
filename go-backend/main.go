package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	fmt.Println("Server running on :8090")
	http.HandleFunc("/hello", hellohandlefunc)
	http.HandleFunc("/fastapi", model)
	http.ListenAndServe(":8090", nil)
}
func hellohandlefunc(w http.ResponseWriter, r *http.Request) {

	fmt.Fprint(w, "This is pure net/http\n")
	fmt.Fprint(w, "r.URL.Path: ", r.URL.Path)
}

func model(w http.ResponseWriter, r *http.Request) {
	resp, err := http.Get("http://127.0.0.1:8000/predict")
	if err != nil {
		fmt.Fprint(w, "Error: ", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Fprint(w, string(body))

}
