# CFG to C

* Open the website with the control flow graphs and the C code
* The control graph with no arrows and the call to idiv is the modulo function
* The control graph with arrows that only go down is the control function
* The control graph that has an arrow going back up and the `cmp $0,8(%ebp)` instruction is the loop function
* The control graph that has an arrow going back up and the `cmp 12(%ebp),%eax` instruction is the for_loop function
