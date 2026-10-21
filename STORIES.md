# User stories – Läslistan

Funktionella krav för webbsidan https://tap-vt26-testautomatisering.github.io/exam/, formulerade som user stories med acceptanskriterier (AK). Varje story har en feature-fil i `src/features/`.

## US1 – Navigering
Som besökare
vill jag kunna växla mellan vyerna Katalog, Lägg till bok, Mina böcker och Statistik
så att jag hittar det jag vill göra.

- AK1. När sidan öppnas visas rubriken "Läslistan" och vyn Katalog.
- AK2. När jag klickar på en knapp i navigeringen visas motsvarande vy.
- AK3. Knappen för vyn jag står i är inaktiv, de andra går att klicka på.
- AK4. Innehållet från den förra vyn visas inte längre.

Feature: `navigation.feature`

## US2 – Se katalogen
Som läsare
vill jag se alla böcker i katalogen med titel och författare
så att jag kan hitta något att läsa.

- AK1. Katalogen visar 13 böcker från början.
- AK2. Varje bok visas som "Titel", Författare.
- AK3. Från början är inga böcker hjärtmarkerade.

Feature: `catalog.feature`

## US3 – Hjärtmarkera favoriter
Som läsare
vill jag kunna hjärtmarkera böcker i katalogen, och ta bort markeringen igen,
så att jag kan välja ut mina favoriter.

- AK1. När jag klickar på hjärtat för en bok blir den markerad.
- AK2. När jag klickar igen tas markeringen bort.
- AK3. Varje klick växlar markeringen (udda antal klick = markerad).
- AK4. Att markera en bok påverkar inte andra böcker.
- AK5. Markeringen finns kvar när jag byter vy och kommer tillbaka.

Feature: `catalog.feature`

## US4 – Lägga till en bok
Som läsare
vill jag kunna lägga till en bok med titel och författare
så att katalogen innehåller böcker som jag tycker saknas.

- AK1. Knappen "Lägg till ny bok" är inaktiv tills både titel och författare är ifyllda.
- AK2. Om ett fält töms blir knappen inaktiv igen.
- AK3. När boken läggs till töms formuläret.
- AK4. Den nya boken visas i katalogen och antalet böcker ökar.
- AK5. En tillagd bok kan hjärtmarkeras som alla andra böcker.

Feature: `add_book.feature`

## US5 – Mina böcker
Som läsare
vill jag se en lista med de böcker jag har hjärtmarkerat
så att jag vet vad jag vill läsa.

- AK1. Om inga böcker är markerade visas ett meddelande om att favoriterna kommer att visas här.
- AK2. Hjärtmarkerade böcker visas i en numrerad lista.
- AK3. Antalet böcker i listan är lika med antalet hjärtmarkerade böcker.
- AK4. En bok som inte längre är markerad försvinner från listan.
- AK5. En bok visas bara en gång i listan.

Feature: `favorites.feature`

## US6 – Statistik
Som besökare
vill jag se hur många böcker listan har och hur många som är hjärtmarkerade
så att jag får en överblick över läslistan.

- AK1. Statistiken visar antalet böcker i listan (13 från början).
- AK2. Statistiken visar antalet hjärtmarkerade böcker (0 från början).
- AK3. Antalet hjärtmarkerade ökar och minskar när markeringar läggs till och tas bort.
- AK4. Antalet böcker ökar när böcker läggs till.

Feature: `statistics.feature`
