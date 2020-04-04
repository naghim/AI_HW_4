# AI_HW_4
_Genetic Algorithm for the Travelling Salesman problem using DEAP framework._

# Feladat
Utazóügynök feladat megoldása evolúciós módszerrel. Bármilyen külső evolúciós framework használható.

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






