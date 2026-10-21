#noinspection CucumberUndefinedStep
Feature: Mina böcker
  # US5:
  # Som läsare
  # vill jag se en lista med de böcker jag har hjärtmarkerat
  # så att jag vet vad jag vill läsa.

  Background:
    Given att jag är på Läslistans startsida

  Scenario: Meddelande visas när inga favoriter är valda
    When jag går till vyn "Mina böcker"
    Then ska meddelandet om att inga favoriter finns visas
    And ska listan med favoriter innehålla 0 böcker

  Scenario: En hjärtmarkerad bok visas i Mina böcker
    Given jag klickar på hjärtat för "Agile Is a Feeling"
    When jag går till vyn "Mina böcker"
    Then ska "Agile Is a Feeling" finnas bland mina böcker
    And ska listan med favoriter innehålla 1 böcker
    And ska meddelandet om att inga favoriter finns inte visas

  Scenario Outline: Antalet favoriter stämmer med antalet hjärtmarkerade böcker
    Given jag hjärtmarkerar de <antal> första böckerna
    When jag går till vyn "Mina böcker"
    Then ska listan med favoriter innehålla <antal> böcker

    Examples:
      | antal |
      | 1     |
      | 3     |
      | 13    |

  Scenario: En bok som inte längre är markerad försvinner från Mina böcker
    Given jag klickar på hjärtat för "Agile Is a Feeling"
    And jag klickar på hjärtat för "The Bugs are Coming"
    And jag klickar på hjärtat för "Agile Is a Feeling"
    When jag går till vyn "Mina böcker"
    Then ska "Agile Is a Feeling" inte finnas bland mina böcker
    And ska "The Bugs are Coming" finnas bland mina böcker
    And ska listan med favoriter innehålla 1 böcker

  Scenario: Meddelandet kommer tillbaka när alla favoriter tagits bort
    Given jag klickar på hjärtat för "Agile Is a Feeling"
    And jag går till vyn "Mina böcker"
    And jag går till vyn "Katalog"
    When jag klickar på hjärtat för "Agile Is a Feeling"
    And jag går till vyn "Mina böcker"
    Then ska meddelandet om att inga favoriter finns visas
    And ska listan med favoriter innehålla 0 böcker

  Scenario: En bok som markeras flera gånger visas bara en gång
    Given jag klickar på hjärtat för "Agile Is a Feeling" 3 gånger
    When jag går till vyn "Mina böcker"
    Then ska listan med favoriter innehålla 1 böcker
