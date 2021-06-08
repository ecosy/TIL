package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// service id, car id 에 해당하는 VIN 리턴
func getVIN(w http.ResponseWriter, r *http.Request) {
}

func setVIN(w http.ResponseWriter, r *http.Request) {

}
func resetVIN(w http.ResponseWriter, r *http.Request) {

}
func deleteVIN(w http.ResponseWriter, r *http.Request) {

}

func main() {
	r := mux.NewRouter()
	r.Handle("/", http.FileServer(http.Dir("./static/")))

	r.HandleFunc("/api/v1/profile/car/{car_id}/vin", getVIN).Methods("GET")
	r.HandleFunc("/api/v1/profile/car/{car_id}/vin", setVIN).Methods("POST")
	r.HandleFunc("/api/v1/profile/car/{car_id}/vin", resetVIN).Methods("PUT")
	r.HandleFunc("/api/v1/profile/car/{car_id}/vin", deleteVIN).Methods("DELETE")

	log.Fatal(http.ListenAndServe(":8000", r))
}
