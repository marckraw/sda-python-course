# Git - Szkolenie Video
- Repozytorium
- Konsola bashowa
- Commit - jest to migawka (snapshot) projektu, wraz z dodatkowymi informacjami, wraz z suma kontrolna ktora wskazuje JEDNOZNACZNIE commit na konkretne zmiany
- .gitignore - dodawanie plikow/folderow ktore chcemy ignorowac, git nie bedzie zarzadzal ich zmianami i nie zostana nigdy dodane do repo
- branch - gałąź

## Przydatne linki
- 

## Przydatne z z tego dnia
- Fast Forwarding - "przestawienie wskaznika mastera na commit na ktory wskazuje branch feature1", domyslna strategia mergowania, git proboje uzyc fast forward gdzie sie da (nie powstaje wtedy zaden merge commit)
- Rebase vs Merge - 


## Przydatne komendy z Shella
```shell
mkdir something - tworzenie folderu o nazwie somethin
touch plik.txt - tworzenie pliku 
ls - listowanie plikow i katalogow kolo siebie
ls -l - listowanie plikow i katalogow w liscie
ls -la - listowanie plikow i katalogow wraz z plikami niewidocznymi
cd .. - zmiena katalogu na podrzedny 
cd ./folder - zmiana katalogu na katalog folder, znajdujacy sie w aktualnym katalogu w ktorym jestesmy
cp - kopiowanie
cp -rf - kopiowanie wraz z wszystkim w glab katalogu
mv - przenoszenie 
mv -rf - przenoszeniw wraz z wszystkim w glab katalogu
pwd - sciezka katalogu w ktorym sie znajdujemy
rm - usuwanie
rm -rf - usuwanie wraz ze wszystkim w glab
```


## Przydatne komendy git
```shell
git init - inicjalizacja gita
git status - status plikow (czy sa zmienione, czy dodane do staging)
git add . - dodanie do staging area wszysktim plikow w aktualnym katalogu i wglab
git add plik.txt - dodanie do staring area pliku plik.txt
git commit -m "Commit message" - stworzenie commita z wiadomoscia Commit messages
git push origin HEAD - pushowanie brancha na ktorym jestesmy do zdalnego brancha o tej samej nazwie
git pull - sciaganie zmian z zdalnego repozytorium
git checkout -b my_branch - stworzenie brancha my_branch z brancha na ktorym aktualnie sie znajdujesz i przelaczenie sie na niego
git pull origin my_branch - sciagniecie zmian z branchea my_branch z zdalnego repozytorium do naszego lokalnego brancha my_branch
git checkout master - zmiana na branch master
git checkout my_branch - zmiana na branch my_branch
git branch nazwa_brancha - tworzy branch nazwa_brancha z aktualnego brancha na ktorym sie jest
git commit -m - otwiera domyslny edytor textowy w ktorym mozemy wpisac commit message
git log - loguje historie commitow
git log --oneline
git log --stat - more stats
git log --graph
git log -- plik.txt

git revert <commit> - pozwala na odwrocenie zmian wprowadzonych w konkretnym commmmicie. Polecenie tworzy nowy commit ktory swoimi zmianami odwraca inne zmiany. Czyli NIE MODYFIKUJE historii.
git branch -d nazwa_brancha - usuwa brancha nazwa_brancha
```

```shell
git stash
git stash list
git stash apply
git stash pop
```

Cofanie stanu pliku:
```shell
git reset plik.txt - uzyte na pliku, dziala odwrotnie do git add, cofa pliki z staging area do working directory
git checkout plik.txt - uzyte na pliku, przywraca stan pliku do postaci zapisanej przez git
git rm - usuwa podany plik/katalog z projektu
```


Scalanie zmian
```shell
git merge <nazwa_brancha> - do brancha, na ktorym obecnie sie znajdujemy, zostana dolaczone zmiany z wybranego brancha
git rebase <nazwa_brancha> - polecenie pozwalajace zamienic podstawe brancha, na ktorym jestesmy, na branch podany w poleceniu, przepisanie commitow z naszego brancha
git rebase -i <nazwa_brancha> - interaktywny rebase, mozna w nim dokonywac zmianw  commitach, zlaczac commity, zmieniac commit message, cuda wianki - bardzo niebezpieczna komenda, uzywac z rozwaga
```






## Przydatne komendy vim:
- vim plik.txt - w konsoli
- zeby zaczac pisac trzeba wcisnac "i" - uruchomi tryb edycji
- robimy zmiany
- pozniej klikamy "esc"
- wpisujemy ":w" a pozniej ":q" i to wychodzi z edytora