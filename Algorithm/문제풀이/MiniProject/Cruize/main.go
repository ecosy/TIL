package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"test/Cruize/Cruize"
)

func Drive() {
	log.Println("Drive Func start...")
	defer func() {
		log.Println("Drive Func end...")
		return
	}()

	// ioReader := bufio.NewReader(os.Stdin)
	consoleReader := bufio.NewReaderSize(os.Stdin, 1)
	for {
		fmt.Print("> ")
		// command, _ := ioReader.ReadString('\n')
		command, _ := consoleReader.ReadByte()
		log.Printf("io input : %v\n", command)
	}
}

func main() {
	log.Println("i am main")

	Drive()

	Cruize.CalculateCruiseControlSpeed(Cruize.UPH, 1)

	return
}

// "crz start" 라는 입력이 들어오면, 크루즈 모드 시작
// "crz off" 입력 들어오면, 크루즈 모드 종료
