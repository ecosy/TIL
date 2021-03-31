package Cruize

import "log"

func CalculateCruiseControlSpeed(button ButtonType, currentSpeed int) {
	log.Println("Cruize control start....")
	log.Printf("button : %v, current speed : %v\n", button, currentSpeed)

	defer func() {
		log.Println("Cruize control end....")
		return
	}()
}
