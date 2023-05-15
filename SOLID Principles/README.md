Acest cod implementează un convertor de valută, care utilizează un API pentru a obține ratele de schimb curente. Principiile solide care sunt aplicate în acest cod sunt următoarele:

    1  Principiul responsabilității unice (SRP): Acest principiu spune că o clasă ar trebui să aibă o singură responsabilitate. În acest cod, fiecare clasă are o singură responsabilitate. De exemplu, clasa ExchangeRateAPI este responsabilă doar pentru apelarea API-ului și pentru obținerea datelor cu privire la ratele de schimb.
Clasa CurrencyConverter este responsabilă doar pentru conversia dintre monede. Clasa CurrencyConverterApp este responsabilă pentru afișarea meniului de conversie.

    2 Principiul deschis-închis (OCP): Acest principiu spune că o clasă ar trebui să fie deschisă pentru extensie, dar închisă pentru modificare. În acest cod, clasa CurrencyConverter poate fi extinsă pentru a adăuga noi funcționalități de conversie între monede, fără a modifica codul existent.

    3 Principiul substituției Liskov (LSP): Acest principiu spune că obiectele unei clase derivate ar trebui să poată fi utilizate în locul obiectelor clasei de bază, fără a afecta corectitudinea programului. În acest cod, nu sunt prezente clase derivate.

    4 Principiul segregării interfețelor (ISP): Acest principiu spune că o interfață ar trebui să fie specifică contextului de utilizare și nu ar trebui să fie prea generală. În acest cod, nu există interfețe.

    5 Principiul inversiunii dependențelor (DIP): Acest principiu spune că modulele de nivel inferior nu ar trebui să depindă direct de modulele de nivel superior, ci ar trebui să depindă de abstracțiuni. În acest cod, clasa CurrencyConverter depinde de o interfață ExchangeRateAPI, care este o abstracțiune a API-ului de conversie valutară. Această abstracțiune permite schimbarea implementării API-ului fără a afecta codul din clasa CurrencyConverter. Acest lucru poate fi util în cazul în care se dorește schimbarea API-ului de conversie valutară dintr-un motiv sau altul.
