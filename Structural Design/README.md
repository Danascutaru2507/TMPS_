Adapter: Adapterul este utilizat în proiectul tău pentru a conecta două interfețe incompatibile. Mai precis, clasa CurrencyConverter a fost scrisă pentru a utiliza datele furnizate de clasa ExchangeRateAPI. În schimb, clasa CurrencyConverterApp a fost scrisă pentru a permite interacțiunea cu utilizatorul prin intermediul unei interfețe de linie de comandă. Folosind un adapter, clasa CurrencyConverter poate fi utilizată în mod corespunzător în cadrul clasei CurrencyConverterApp.


Decorator: Decoratorul este utilizat în proiectul tău pentru a extinde funcționalitatea clasei CurrencyConverter. Mai exact, clasa CurrencyConverter calculează conversia dintre două valute pe baza unui factor de conversie. Cu toate acestea, dacă utilizatorul ar dori să adauge o taxă suplimentară la conversie, acest lucru ar fi dificil de realizat în cadrul clasei CurrencyConverter. Prin implementarea unui decorator, utilizatorul poate extinde clasa CurrencyConverter și poate adăuga o taxă suplimentară la conversie.


Façade este un model de design care ascunde complexitatea sistemului și oferă o interfață simplificată pentru a accesa și utiliza funcționalitățile sistemului. În acest proiect, clasa CurrencyConverterApp poate fi văzută ca o interfață simplificată pentru a accesa și utiliza funcționalitățile din spatele ei, cum ar fi clasa CurrencyConverter și ExchangeRateAPI. Prin intermediul clasei CurrencyConverterApp, utilizatorii pot introduce datele de intrare, apoi se apelează metodele din clasele CurrencyConverter și ExchangeRateAPI pentru a converti moneda.



Funcția design pattern-urilor structurale în acest proiect este aceea de a organiza obiectele și clasele într-o structură coerentă și flexibilă, pentru a putea schimba comportamentul acestora fără a modifica structura de bază a programului. Aceste design pattern-uri ajută la crearea unui sistem modular, ușor de întreținut și extensibil, prin separarea responsabilităților între clase și interfețe, reducerea duplicării codului și permiterea flexibilității în modificarea comportamentului. În cazul acestui proiect, cele trei design pattern-uri structurale implementate (Adapter, Decorator și Facade) au fost utilizate pentru a permite programului să fie mai ușor de extins, de modificat și de menținut, reducând complexitatea și sporind eficiența.