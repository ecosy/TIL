package preprocess

import (
	"fmt"
	"io"
	"log"
	"strconv"
	"sync"
)

type transmCh struct {
	mpgCH  chan float64
	milgCh chan int
}

type sumVal struct {
	milgSUM int64
	mpgSUM  int64
}

var transmissionSUM map[string]sumVal

func newTransmCh() *transmCh {
	ch := transmCh{}
	ch.milgCh = make(chan int, 10000)
	ch.mpgCH = make(chan float64, 10000)
	return &ch
}

func closeTransmCh(ch *transmCh) {
	close(ch.milgCh)
	close(ch.mpgCH)
}

func inputChannel(wg *sync.WaitGroup, manualCh, autoCh, semiAutoCH *transmCh) {
	log.Println("inputchannel start....")
	fileName := "audi"
	r := readFromCSV(fileName)

	count := 0
	for {
		record, err := r.Read()
		if count == 0 {
			count++
			continue
		}
		count++

		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalf("error in r.Read(), err : %v\n", err)
		}

		mileage, err := strconv.Atoi(record[MILEAGE])
		if err != nil {
			log.Fatalf("error strconv.Atoi record[MILEAGE], err : %v\n", err)
		}
		mpg, err := strconv.ParseFloat(record[MPG], 64)
		if err != nil {
			log.Fatalf("error strconv.Atoi record[MPG], err : %v\n", err)
		}
		// log.Printf("mile : %v, mpg : %v\n", mileage, mpg)

		switch record[TRANSMISSION] {
		case "Manual":
			manualCh.milgCh <- mileage
			manualCh.mpgCH <- mpg
		case "Automatic":
			autoCh.milgCh <- mileage
			autoCh.mpgCH <- mpg
		case "Semi-Auto":
			semiAutoCH.milgCh <- mileage
			semiAutoCH.mpgCH <- mpg
		default:
			log.Printf("record[TRANSMISSION] is not among [manual, auto, semi-auto]\n")
		}
	}
	closeTransmCh(manualCh)
	closeTransmCh(autoCh)
	closeTransmCh(semiAutoCH)
	log.Println("input channel end")
	wg.Done()
}

func printCh(wg *sync.WaitGroup, ch *transmCh) {
	for v := range ch.mpgCH {
		fmt.Printf("%v ", v)
	}
	fmt.Println()
	for v := range ch.milgCh {
		fmt.Printf("%v ", v)
	}
	wg.Done()
}

func calculateSum(wg *sync.WaitGroup, ch *transmCh, transmissionType string) {
	var transType string = fmt.Sprintf("%sSUM", transmissionType)

	for v := range ch.milgCh {
		transmissionSUM[transType].milgSUM += int64(v)
	}
	fmt.Println()
	for v := range ch.milgCh {
		fmt.Printf("%v ", v)
	}
}

func Solution2Origin() {
	log.Println("main start....")

	manualCh := newTransmCh()
	autoCh := newTransmCh()
	semiAutoCH := newTransmCh()

	transmissionSUM = map[string]sumVal{
		"manualSUM":   sumVal{},
		"autoSUM":     sumVal{},
		"semiAutoSUM": sumVal{},
	}

	// fileName := "audi"
	var wg sync.WaitGroup
	wg.Add(1)
	go inputChannel(&wg, manualCh, autoCh, semiAutoCH)
	wg.Wait()

	wg.Add(3)
	go printCh(&wg, manualCh)
	log.Println("print manualCh end")

	go printCh(&wg, autoCh)
	log.Println("print autoCh end")

	go printCh(&wg, semiAutoCH)
	log.Println("print semiAutoCH end")

	wg.Wait()
	log.Println("wait end")

	log.Println("main end....")
	return
}

func Solution2GoRoutine() {}

func solution2(fileName string) {
	// r := readFromCSV(fileName)
}

// [transmission]
// manual
// automatic
// semi auto

// 각 브랜드별로 병렬처리
// 한번만 csv 파일을 읽으면서, 각 type에 맞게, go channel에 값 넣기
//
