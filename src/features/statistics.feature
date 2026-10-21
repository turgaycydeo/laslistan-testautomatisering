#noinspection CucumberUndefinedStep
Feature: Statistik
  # US6:
  # Som besökare
  # vill jag se hur många böcker listan har och hur många som är hjärtmarkerade
  # så att jag får en överblick över läslistan.

  Background:
    Given att jag är på Läslistans startsida

  Scenario: Statistiken från början
    When jag går till vyn "Statistik"
    Then ska statistiken visa att listan har 13 böcker
    And ska statistiken visa att 0 böcker är hjärtmarkerade

  Scenario Outline: Antalet hjärtmarkerade böcker räknas
    Given jag hjärtmarkerar de <antal> första böckerna
    When jag går till vyn "Statistik"
    Then ska statistiken visa att <antal> böcker är hjärtmarkerade
    And ska statistiken visa att listan har 13 böcker

    Examples:
      | antal |
      | 1     |
      | 5     |
      | 13    |

  Scenario: Antalet hjärtmarkerade minskar när en markering tas bort
    Given jag klickar på hjärtat för "Agile Is a Feeling"
    And jag klickar på hjärtat för "The Bugs are Coming"
    And jag klickar på hjärtat för "Agile Is a Feeling"
    When jag går till vyn "Statistik"
    Then ska statistiken visa att 1 böcker är hjärtmarkerade

  Scenario Outline: Antalet böcker ökar när böcker läggs till
    Given jag går till vyn "Lägg till bok"
    And jag lägger till <antal> nya böcker
    When jag går till vyn "Statistik"
    Then ska statistiken visa att listan har <totalt> böcker

    Examples:
      | antal | totalt |
      | 1     | 14     |
      | 3     | 16     |
