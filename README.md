# AI_HW_4
_Genetic Algorithm for the Travelling Salesman problem using DEAP framework._

The __readme__ is also available in English [here](#task).

# Feladat
Utazó ügynök feladat megoldása evolúciós módszerrel. Tehát adott egy lista a városokkal, keressük meg azt a legrövidebb utat, amely során a kiinduló városból ugyanoda érkezve minden többi várost egyszer érintünk. Használjunk hozzá evolúciós framework-öt.


## Megoldás

Az általam választott framework a DEAP framework. Mivel a mintakódok között fellelhető a TSP megoldása a framework segítségével, így egy másik, általam kitalált megoldással oldottam meg s nem a mintakód által javasolt struktúrával. 

A problémát mint irányítatlan súlyozott, teljes gráfként kezeltem, szimmetrikus TSP-t megoldva (vagyis minden út oda és vissza létezik és ugyanannyi a költsége). 

A Wikipedián fellelhető egyszerű gráfra lett megolva a probléma:

![Graph](https://github.com/naghim/AI_HW_4/blob/master/graph.jpg?raw=true)

További kikötés, hogy az `A` városból kell indulni.
Látható, hogy az `A` városból a legrövidebb út a következő szekvencia lesz: `A B C D A`, ennek össze pedig 97. A megoldási genom a következőként kódolja a megoldást, az index mutatja mely városból indulunk s az érték mutatja mely városba érkezünk. Tehát az optimális megoldás esetében a megoldási szekvencia a következő: `[1, 2, 3, 0]` --> 0->1->2->3->0, ahol a `0` `A` várost jelöli, `1` a `B` várost és így továb...

A kód Python-ban lett megírva, 3.7-es verzióban, illetve DEAP frameworkkel és párhuzamosítva van.

___
___

# Task
Solve the travelling salesman problem using an evolutionary method. So given a list of cities, let’s find the shortest way to reach all the other cities and arrive at the strating city. Use an evolutionary framework.

## Solution
The framework I chose is the DEAP framework. Since the solution of TSP can be found among the sample codes of the framework, I solved it with another solution and not with the structure suggested by the sample code.

I treated the problem as an undirected weighted, complete graph, solving a symmetric TSP (i.e., the distance between two cities is the same in each opposite direction).

The problem solves this the simple graph from Wikipedia:

[Graph] (https://github.com/naghim/AI_HW_4/blob/master/graph.jpg?raw=true)

Another constraint is that you must start from city `A`.
The shortest path from the city `A` will be the following sequence:` A B C D A` and its total cost is 97. The solution genome encodes the solution as follows, the index shows which city we are starting from and the value shows which city we are going to. So for the optimal solution, the solution sequence is: `[1, 2, 3, 0]` -> 0-> 1-> 2-> 3-> 0, where `0` denotes city `A`, `1` denotes city ` B` and so on...

The code was written in Python, version 3.7, and with DEAP framework and is parallelized.
