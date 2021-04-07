package preprocess

import (
	"fmt"
	"io"
	"log"
	"strconv"
	"sync"
)

type taxSum struct {
	count int
	sum   int64
}

var TransmFuel map[string]*taxSum

func newTaxSum() *taxSum {
	newStruct := taxSum{}
	return &newStruct
}

var transmSet map[string]int
var fuelSet map[string]int

func makeSet(wg *sync.WaitGroup, m *sync.Mutex, fileName string) {
	defer wg.Done()

	r := readFromCSV(fileName)
	// read one row of r
	count := 0
	for {
		record, err := r.Read()
		if count == 0 {
			count++
			continue
		}
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalf("error in r.Read(), err : %v\n", err)
		}
		key := fmt.Sprintf("%s_%s", record[TRANSMISSION], record[FUEL_TYPE])
		tax, err := strconv.Atoi(record[TAX])
		if err != nil {
			log.Fatalf("errror when strconv atoi tax\n")
		}

		m.Lock()
		if TransmFuel[key] == nil {
			TransmFuel[key] = newTaxSum()
		}
		TransmFuel[key].sum += int64(tax)
		TransmFuel[key].count++

		m.Unlock()
	}
}

func calculateTaxAVG() {
	for k, v := range TransmFuel {
		fmt.Printf("key : %v, tax AVG : %v\n", k, v.sum/int64(v.count))
	}
}

func Solution3() {
	TransmFuel = make(map[string]*taxSum)

	var wg sync.WaitGroup
	var m sync.Mutex
	wg.Add(len(Brands))
	for _, v := range Brands {
		go makeSet(&wg, &m, v)
	}
	wg.Wait()

	calculateTaxAVG()
}
