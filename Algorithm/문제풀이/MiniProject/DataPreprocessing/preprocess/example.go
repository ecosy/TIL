package preprocess

import (
	"fmt"
	"log"
	"sync"
)

type extransmCh struct {
	mpgCH  chan float64
	milgCh chan int
}

func exnewTransmCh() *extransmCh {
	ch := extransmCh{}
	ch.milgCh = make(chan int)
	ch.mpgCH = make(chan float64)
	return &ch
}

func inputCh(ch *extransmCh, wg *sync.WaitGroup) {
	for i := 0; i < 10; i++ {
		ch.milgCh <- i
	}
	close(ch.milgCh)
	wg.Done()
}

func Example() {
	log.Println("example start...")

	var wg sync.WaitGroup
	ch := exnewTransmCh()

	wg.Add(1)
	go inputCh(ch, &wg)

	go func() {
		for v := range ch.milgCh {
			fmt.Printf("%v ", v)
		}
		fmt.Println()
	}()

	// for v := range ch.milgCh {
	// 	fmt.Printf("%v ", v)
	// }
	// fmt.Println()
	wg.Wait()

	log.Println("example end...")
}
