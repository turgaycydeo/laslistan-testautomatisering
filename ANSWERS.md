# Teorifrågor

## 1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

Ett enhetstest testar en liten del av koden för sig själv, oftast en metod eller en klass. Om klassen är beroende av något annat byter man ut det mot en mock eller fake så att det bara är just den delen som testas. I mitt projekt testar jag t.ex. BookStore med en mockad FavoriteBooks.

Ett integrationstest testar att flera delar fungerar ihop och skickar data mellan sig på rätt sätt. Där använder man de riktiga klasserna, som när jag testar att en bok hamnar i FavoriteBooks när man kör toggleFavorite i BookStore.

Ett regressionstest ska se till att saker som fungerade innan inte går sönder när man lägger till ny kod. Det är egentligen inte en egen sorts test, det handlar mer om varför testet finns. Alla tester man sparar och kör igen blir regressionstester efter ett tag, och ofta skriver man ett nytt test när man har hittat en bugg så att den inte kommer tillbaka.

Ett prestandatest mäter hur snabbt och stabilt systemet är, t.ex. körtid, svarstid och hur mycket resurser det tar, särskilt när datamängden eller belastningen ökar. I kursen använde vi pytest-benchmark för att jämföra olika versioner av en funktion.

## 2. Beskriv hur det går till när man arbetar med TDD.

Man skriver testet innan koden. Först skriver man ett test för något som inte finns än och kör det, då ska det bli rött. Sedan skriver man så lite kod som möjligt för att få testet grönt. När det är grönt kan man städa upp och förbättra koden (refactor) och köra testerna igen för att se att allt fortfarande fungerar. Sen tar man nästa lilla krav och gör samma sak igen. Red, green, refactor.

Fördelen är att man hela tiden vet att koden gör det den ska och att man tänker igenom kraven innan man börjar koda.

## 3. Beskriv hur BDD skiljer sig från TDD.

BDD bygger på TDD men fokuserar mer på hur systemet ska bete sig för användaren än på enskilda funktioner. Testerna skrivs på nästan vanligt språk med Gherkin (Given, When, Then) i feature-filer, så att även kunden och andra som inte programmerar kan läsa dem och vara med och skriva dem. Sen kopplas varje mening till kod i step-filer, i vårt fall med behave.

TDD är mer för utvecklaren och handlar om små kodenheter, medan BDD handlar om ett gemensamt språk för hela teamet och att lösa verkliga behov. Testerna skrivs fortfarande innan koden i båda.

## 4. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

För backend skulle jag använda enhetstester för alla klasser och metoder, eftersom de är snabba och visar exakt var felet är. Jag skulle också ha integrationstester för de delar som jobbar ihop, t.ex. katalogen och favoritlistan, och mot databasen om det fanns en.

För frontend skulle jag använda BDD med behave och Playwright. Då blir user stories direkt till tester och det går att visa feature-filerna för beställaren. E2E-testerna visar att hela flödet fungerar som en riktig användare skulle använda sidan. De är långsammare, så jag skulle inte ha med varenda detalj där utan fokusera på de viktigaste flödena.

Alla tester skulle köras i CI vid varje push så att man upptäcker regressioner direkt. Om sidan växer och får fler användare, som de planerar med quiz och diskussioner, skulle jag också lägga till prestandatester för att se att den klarar större listor och fler användare samtidigt.
