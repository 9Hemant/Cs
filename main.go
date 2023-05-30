package main
import(
    "fmt"
    "net/http"
)
func main(){
    http.HandleFunc("/test-server", func(rw http.ResponseWriter, r *http.Request){
        fmt.Fprint(rw, "\nThis is a test Server\n")
    })
    http.ListenAndServe(":80",nil)
}