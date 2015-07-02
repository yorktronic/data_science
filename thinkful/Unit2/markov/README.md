# Markov Models #

Markov processes are processes in which the present state is influenced only by the immediately preceding state. Here's a good visual example of a Markov model: 

<img src="https://tf-curricula-prod.s3.amazonaws.com/curricula/b04b6f653b9d364d5612ac767527458a/DATA-001/v2/assets2/2.8.1_Overview_Markov_Models/MC2.png">

* Think of a Markov process as a square matrix - for every node in the process there is a transitional probability to each of the other nodes in the process, and all of those and the sum of those probabilities is equal to 1
* In order to calculate the probaibility that you will end up at some M state after N number of state changes, you simply raise the matrix to the nth power and then find the corresponding transitional probability in the matrix
* If you iterate enough times (i.e. n becomes a really big number), you enter a potential steady state where all the probabilities become stable regardless of your starting point
* _Recurrent states_ will have a chance of coming back to the original state
* _Transient states_ have transitions that will eliminate the possibility that the state will return to the original state
* _Recurrent class_ is a set of recurrent states that communicate only with each other

Subway, bus, and air travel is a good example of where Markov models would apply. They however cannot (or should not?) be used to model anything with a time component, or where data prior to the immediate previous state is applicable in determining the current and future state, or any of a vast variety of common sense cases that I'm not going to write about here :)
