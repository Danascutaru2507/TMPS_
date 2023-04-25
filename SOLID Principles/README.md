S - Single Responsibility Principle: fiecare clasă are o singură responsabilitate, clasa CurrencyConverter este responsabilă doar de convertirea valutelor.

O - Open-Closed Principle: codul este deschis pentru extensii prin adăugarea de noi clase care implementează interfața IExchangeRateProvider. Acest lucru permite utilizarea altor API-uri pentru a obține ratele de schimb valutar, fără a modifica clasa CurrencyConverter.

L - Liskov Substitution Principle: obiectele de tip IExchangeRateProvider pot fi utilizate în locul obiectului CurrencyConverter fără a afecta comportamentul programului.

I - Interface Segregation Principle: clasa CurrencyConverter depinde de interfața IExchangeRateProvider, care definește numai metodele necesare pentru a obține ratele de schimb valutar. Astfel, clasa CurrencyConverter nu este afectată de alte metode din clasa IExchangeRateProvider, pe care nu le folosește.

D - Dependency Inversion Principle: clasa CurrencyConverter depinde de o interfață (IExchangeRateProvider) și nu de o implementare concretă a acesteia. Acest lucru permite schimbarea implementării IExchangeRateProvider fără a modifica clasa CurrencyConverter.