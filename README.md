    Principiile S.O.L.I.D.

În general este foarte ușor să scriem cod fără a ne gândi la modul în care îl vom întreţine. Scopul meu însă a fost din start să încep o aplicaţie pe care să o rafinez pe parcurs. Modul în care intenţionez să dezvolt această aplicație este aderând la principiile care organizat dau acronimul S.O.L.I.D. Le voi prezenta nu în ordinea din acronim, ci în stilul pe care l-am descoperit cel mai ușor de asimilat. Aceste principii sunt acceptate ca și standarde în comunitate software actuală, problema rămâne totuși cum le aplicăm și cum le interpretăm.

    Single Responsability Principle - principiul responsabilităţii unice

Acest principiu afirmă că o clasă trebuie să aibe un singur motiv pentru a fi modificată.
Este relativ greu de întreţinut arhitectura unei aplicaţii. Cu cât aduci mai mulţi oameni pe proiect și cu cât investești mai mult în anumite facilităţi, degradarea sistemului în general se face simţită. Acest principiu propune o strategie care forţează scrierea de obiecte simple, care au o responsabilitate exactă, ușor de urmărit și modificat. Fiind vorba de o singură responsabilitate, probabilitatea ca schimbarea să afecteze alt cod este destul de restrânsă. Comportamentul se va schimba evident, dar codul nu. Și în cazul unei erori, responsabilul e relativ ușor de identificat.

    Dependency Injection 

Acest principiu afirmă că "Modulele de nivel înalt nu ar trebui să depindă de modulele din nivelele inferioare, ambele ar trebui să depinde de abstracţii" și "Abstracţiile nu ar trebui să depindă de detalii, detaliile ar trebui să depindă de abstracţii". Sună bizar de primele 12 ori când îl citești, dar parcă ceva sună bine, indicația ar fi să nu se folosească nicăieri în cod referinţe la clase concrete ci doar la interfeţe și/sau clase abstracte, concretizările acestor vor fi injectate fie de către un alt obiect/altă clasă.
Există 3 forme de injectare:

Injectare prin constructor: dependințele sunt declarate în constructor, satisfacerea acestor dependințe fiind lăsată pe seama celui care crează instanța

Injectare prin elemente setter10: dependințele sunt injectate prin intermediul unei funcții care respectă convenția de nume setXXX, unde XXX este numele proprietății.

Injectare prin interfață: se declară interfețe care vor avea funcții injectXXX pentru fiecare dependință pe care vrem să o injectăm.

    Open Closed Principle

"Clasele ar trebui să fie deschise extensiei și închise modificărilor". Semnificaţia este următoare, dacă e nevoie să se modifice ceva din comportamentul extern al clasei sau dependinţele acesteia, acea modificare trebuie să fie posibilă fără a schimba codul clasei. Cheia pentru a obține acest comportament este utilizarea abstractizării. Din moment ce clasa încapsulează logica utilizând abstracții, înseamnă că putem schimba implementările acelor abstracții și se va modifica și comportamentul, dar nu codul.

   Liskov Substitution Principle

"Funcţiile care utilizează pointeri sau referinţe la clasele de bază trebuie să poată folosi obiecte sau clase derivate fără să știe acest lucru". În principiu înseamnă că o dată comportamentul clasei stabilit modifcările pe care le fac asupra claselor din afara domeniul desemnat de obiect nu ar trebui să ma forţeze să modific comportamentul intern al clasei mele.'

   Interface Segregation Principle

"Clienţii nu ar trebui să fie forţaţi să depindă de interfeţe pe care nu le folosesc". Semnificaţia este că dacă un client depinde de anumite utilizări, a nu se confunda cu diferite responsabilităţi, atunci ar trebui să fie o interfaţă specifică pentru fiecare dintre utilizări.