#noinspection CucumberUndefinedStep
Feature: Navigering mellan vyerna
  # US1:
  # Som besökare
  # vill jag kunna växla mellan vyerna Katalog, Lägg till bok, Mina böcker och Statistik
  # så att jag hittar det jag vill göra.

  Background:
    Given att jag är på Läslistans startsida

  Scenario: Katalogen visas när sidan öppnas
    Then ska rubriken "Läslistan" visas
    And ska vyn "Katalog" vara vald
    And ska innehållet för "Katalog" visas

  Scenario Outline: Byta till en annan vy
    When jag går till vyn "<vy>"
    Then ska vyn "<vy>" vara vald
    And ska de andra navigeringsknapparna gå att klicka på
    And ska innehållet för "<vy>" visas

    Examples:
      | vy            |
      | Lägg till bok |
      | Mina böcker   |
      | Statistik     |

  Scenario Outline: Gå tillbaka till katalogen från en annan vy
    Given jag går till vyn "<vy>"
    When jag går till vyn "Katalog"
    Then ska vyn "Katalog" vara vald
    And ska innehållet för "Katalog" visas
    And ska innehållet för "<vy>" inte visas

    Examples:
      | vy            |
      | Lägg till bok |
      | Mina böcker   |
      | Statistik     |

  Scenario: Navigera genom alla vyer i följd
    When jag går till vyn "Lägg till bok"
    And jag går till vyn "Mina böcker"
    And jag går till vyn "Statistik"
    And jag går till vyn "Katalog"
    Then ska vyn "Katalog" vara vald
    And ska de andra navigeringsknapparna gå att klicka på
