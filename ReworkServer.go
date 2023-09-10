//A little book work bc I dont wanna touch python today
package main
import("fmt"
       "os"
       "net/http"
	   "sync")



const mu sync.Mutex
const count int

func operator(){

	http.HandleFunc("/", handler)
	http.HandleFunc("/count", counter)
	log.Fatal(http.ListenAndServe("localHost:8000",nil))

}

func handler(w http.ResponseWriter, r *http.Request){

	mu.Lock()
	count++
	mu.Unlock
	fmt.Printf(w, "URL.Path = %q\n", r.URL.Path)

}

func counter(w http.ResponseWriter, r *http.Request){

	mu.Lock()
	fmt.Fprintf(w, "Count %d\n", count)
	mu.Unlock()

}



