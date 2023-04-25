Modelele de design creational sunt un subset de modele de design care se concentrează pe modul în care obiectele sunt create, instantate și manipulate într-un sistem software. Acestea sunt folosite pentru a îmbunătăți modul de creare a obiectelor într-un sistem și pentru a face această operațiune mai flexibilă și mai ușor de gestionat.

Cele mai cunoscute modele de design creational sunt:

Singleton - asigură că o clasă are o singură instanță și oferă un punct centralizat de acces la această instanță.

Factory Method - oferă o interfață pentru crearea de obiecte într-o clasă de bază, dar permite subclaselor să schimbe tipul obiectelor create.

Abstract Factory - furnizează o interfață pentru crearea de familii de obiecte asociate sau dependente, fără a specifica clasele concrete.

Builder - separă procesul de construire a unui obiect de reprezentarea sa și permite crearea de obiecte complexe pas cu pas.

Prototype - permite crearea de noi obiecte prin clonarea altor obiecte existente.

Aceste modele de design sunt folosite frecvent în dezvoltarea software-ului pentru a crea obiecte și structuri de obiecte mai flexibile și mai ușor de gestionat.




În proiectul actual, am selectat următoarele modele de design creațional: 

Singleton

Acest design pattern permite crearea unei singure instanțe a unei clase și asigură că această instanță este accesibilă global. În codul dat, clasa ExchangeRateAPI este implementată folosind Singleton. Astfel, obiectele acestei clase pot fi create folosind metoda statică "get_instance". Datorită acestui design pattern, se poate asigura faptul că întotdeauna se va lucra cu aceeași instanță a acestei clase.

Factory

Acest design pattern permite crearea unor obiecte fără a fi nevoie să se specifice clasa exactă a obiectului. În codul dat, clasa CurrencyConverterFactory este implementată folosind Factory. Aceasta permite crearea unui obiect CurrencyConverter în funcție de obiectul ExchangeRateAPI primit ca parametru. Acest design pattern permite crearea unor obiecte flexibile și ușor de întreținut, care pot fi extinse cu ușurință.

Builder

Acest design pattern permite crearea obiectelor pas cu pas și oferă o abstracție pentru crearea unor obiecte complexe. În codul dat, clasa CurrencyConverterBuilder este implementată folosind Builder. Aceasta permite construirea unui obiect CurrencyConverter prin adăugarea unui obiect ExchangeRateAPI folosind metoda "add_api" și apoi crearea obiectului final folosind metoda "build". Acest design pattern oferă o metodă clară de creare a obiectelor complexe și permite separarea construcției obiectelor de reprezentarea lor.

