#noinspection CucumberUndefinedStep
Feature: Katalog och favoritmarkering
  # US2:
  # Som läsare
  # vill jag se alla böcker i katalogen med titel och författare
  # så att jag kan hitta något att läsa.
  #
  # US3:
  # Som läsare
  # vill jag kunna hjärtmarkera böcker i katalogen, och ta bort markeringen igen,
  # så att jag kan välja ut mina favoriter.

  Background:
    Given att jag är på Läslistans startsida

  Scenario: Katalogen visar alla böcker från början
    Then ska katalogen visa 13 böcker
    And ska inga böcker vara hjärtmarkerade

  Scenario Outline: Böckerna visas med titel och författare
    Then ska boken "<titel>" av "<författare>" finnas i katalogen

    Examples:
      | titel                                    | författare              |
      | Ormar på ett plan: En Python-berättelse  | Guido van Rossum        |
      | Playwright: Click It Till You Make It    | Microslop Browserdóttir |
      | My First Regex (And Last)                | Larry Wallström         |
      | The Bugs are Coming                      | George R.R. Martin      |

  Scenario: Hjärtmarkera en bok
    When jag klickar på hjärtat för "Agile Is a Feeling"
    Then ska hjärtat för "Agile Is a Feeling" vara markerat

  Scenario: Ta bort en hjärtmarkering
    Given jag klickar på hjärtat för "Agile Is a Feeling"
    When jag klickar på hjärtat för "Agile Is a Feeling"
    Then ska hjärtat för "Agile Is a Feeling" vara omarkerat

  Scenario Outline: Klicka på samma hjärta flera gånger
    When jag klickar på hjärtat för "Learn Python in 21 Years" <antal> gånger
    Then ska hjärtat för "Learn Python in 21 Years" vara <status>

    Examples:
      | antal | status    |
      | 1     | markerat  |
      | 2     | omarkerat |
      | 3     | markerat  |
      | 4     | omarkerat |
      | 5     | markerat  |

  Scenario: Hjärtmarkera flera böcker påverkar bara de valda böckerna
    When jag klickar på hjärtat för "The Pragmatic Procrastinator"
    And jag klickar på hjärtat för "Stack Overflow: A Love Story"
    Then ska hjärtat för "The Pragmatic Procrastinator" vara markerat
    And ska hjärtat för "Stack Overflow: A Love Story" vara markerat
    And ska hjärtat för "Agile Is a Feeling" vara omarkerat

  Scenario: Hjärtmarkering finns kvar efter byte av vy
    Given jag klickar på hjärtat för "Agile Is a Feeling"
    When jag går till vyn "Statistik"
    And jag går till vyn "Katalog"
    Then ska hjärtat för "Agile Is a Feeling" vara markerat
