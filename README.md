# SuDoKu

`SuDoKu` jest to prosta gra logiczna, wzorowana na popularnej grze Sudoku.

Repozytorium `sudoku` zawiera następujące pliki oraz foldery:

* `Sudoku.py`: główna aplikacja, od której zaczynamy zabawę

* `sudoku/`

    * `SudokuMainWindow.py`: moduł do tworzenia okna gry, zawiera również klasy do implementacji gry;
  
    * `CreateSudoku.py`: moduł do tworzenia planszy sudoku, wykorzystywanej w `SuDoKu`;
  
    * `AboutGame.py`: klasa do wyświetlania okna z informacjami o grze, zawiera następujące zakładki:
  informacja oo grze, reguły gry oraz skróty klawiszowe;
  
    * w folderze `sudoku` zostały umieszczone obrazki użyte przy tworzeniu gry.
  
### Uruchomienie gry

Uruchomienie gry przy użyciu:

```
./Sudoku.py
```

### Reguły gry

`SuDoKu `to łamigłówka, której celem jest wypełnienie diagramu 9 × 9 w taki sposób, aby w każdym wierszu, w każdej kolumnie i w każdym z dziewięciu bloków 3 × 3 znalazła się dokładnie jedna cyfra od 1 do 9.

### Jak grać?

Gra `SuDoKu` została przygotowana w taki sposób, że użytkownik może wykorzystywać zarówno myszkę, jak i klawiaturę. 

Przed pojawieniem się planszy, użytkownik musi wybrać poziom trudności.

W puste pola należy wstawić jedną z cyfr, w sposób podany w **Reguły gry**. 

W każdej chwili gracz może sprawdzić czy wprowadzone cyfry są prawidłowe, klikając w przycisk `Check` (lub wykorzystując skrót `Ctrl+C`), po naciśnięciu otrzyma stosowny komunikat o prawidłości swojego rozwiązania (lub jego części). 
W przypadku błędów w rozwiązaniu, pola z niepoprawną cyfrą zostaną pokolorowane na czerwono (lub inny kolor jaki zostanie wybrany przez użytkownika w `Options`). 

Gracz może skasować niepoprawne rozwiązanie, poprzez naciśnięcie przycisku `Backspace` lub `Delete`. Może również wykorzystać przycisk `Solve Cell` (lub skrót `Ctrl+M`), wówczas w wybranym polu pojawi się poprawna odpowiedź, a pole zmieni kolor na zielony (lub inny kolor jaki zostanie wybrany przez użytkownika w `Options`).

Po wypełnieniu wszystkich pól warto sprawdzić swoje rozwiązanie za pomocą przycisku `Check`.

Ponadto istnieje opcja zresetowania gry i zaczęcia wszystkiego od nowa (przycisk `Reset` lub skrót `Ctrl+R`) lub odłonięcia całego rozwiązania (przycisk `Solve` lub `Ctrl+S`).

**Uwaga**: Istnieje opcja zmiany kolorów pól, które zostały sprawdzone i są źle wypełnione oraz tych, które zostały rozwiązane poprzez naciśnięcie przycisku `Solve Cell`, po zmianie opcji `SuDoKu` zostanie zresetowane.

