# fantapalla_mattacup

L'algoritmo selection_giornate.py estrae 9 giornate usando come input i fantapunti a fine stagione delle 8 squadre e la somma totale di fantapunti. La selezione è deterministica e sfrutta la funzione modulo per estrarre giornate contenute tra la 6 e la 34 (estremi compresi). Flow:
1. Si ordinano le squadre alfabeticamente, lasciando la somma dei fantapunti come ultimo elemento.
2. Tutte i punteggi vengono convertiti a intero usando la funzione floor.
3. Per ogni punteggio, si prende 6 + punteggio % 29 (questo garantisce che la giornata estratta sia sempre compresa tra 6 e 34)
4. Se il risultato non è già occorso, si aggiunge direttamente alla lista di giornate estratte.
5. In caso contrario, si procede aggiungendo 1 al risultato finché non si incontri una giornata non ancora in lista.
6. Se 5 fosse insufficiente (ovvero sommando fino al massimo valore consentito non si incontra nessun valore non ancora estratto), si procede sottraendo 1 al risultato finché non si incontri una giornata non ancora in lista.
7. Quando tutti i punteggi sono stati processati, si ritorna la lista di giornate nello stesso ordine di estrazione. NB: nella logica della Matta Cup è assolutamente consentito che le giornate non siano monotòne (ad esempio la seconda giornata sia minore della prima).

La natura della funzione modulo, unita all'ordine di grandezza tipico dei fantapunti tipicamente molto maggiore dei valori nell'intervallo [6, 34], fa sì che pur essendo deterministico, riproducibile e verificabile a posteriori da chiunque, l'algoritmo produca dei valori impossibili da prevedere a stagione in corso. 
