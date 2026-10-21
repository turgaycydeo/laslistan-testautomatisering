#noinspection CucumberUndefinedStep
Feature: Lägga till en ny bok

  Background:
    Given att jag är på Läslistans startsida
    And jag går till vyn "Lägg till bok"

  Scenario: Formuläret är tomt och knappen inaktiv från början
    Then ska formulärets fält vara tomma
    And ska knappen "Lägg till ny bok" vara inaktiv

  Scenario Outline: Knappen är inaktiv om bara ett fält är ifyllt
    When jag bara fyller i fältet "<fält>" med "<text>"
    Then ska knappen "Lägg till ny bok" vara inaktiv

    Examples:
      | fält       | text            |
      | Titel      | Clean Code      |
      | Författare | Robert C. Martin |

  Scenario: Knappen blir aktiv när båda fälten är ifyllda
    When jag fyller i titeln "Clean Code" och författaren "Robert C. Martin"
    Then ska knappen "Lägg till ny bok" vara aktiv

  Scenario: Knappen blir inaktiv igen om ett fält töms
    Given jag fyller i titeln "Clean Code" och författaren "Robert C. Martin"
    When jag tömmer fältet "Titel"
    Then ska knappen "Lägg till ny bok" vara inaktiv

  Scenario: Formuläret töms när boken har lagts till
    When jag lägger till boken "Clean Code" av "Robert C. Martin"
    Then ska formulärets fält vara tomma
    And ska knappen "Lägg till ny bok" vara inaktiv

  Scenario Outline: En tillagd bok visas i katalogen
    When jag lägger till boken "<titel>" av "<författare>"
    And jag går till vyn "Katalog"
    Then ska boken "<titel>" av "<författare>" finnas i katalogen
    And ska katalogen visa 14 böcker

    Examples:
      | titel                         | författare        |
      | Clean Code                    | Robert C. Martin  |
      | Åsa-Nisses äventyr i kodskogen | Örjan Ängström    |
      | Test-Driven Development       | Kent Beck         |

  Scenario: Lägga till flera böcker
    When jag lägger till boken "Clean Code" av "Robert C. Martin"
    And jag lägger till boken "Refactoring" av "Martin Fowler"
    And jag går till vyn "Katalog"
    Then ska katalogen visa 15 böcker
    And ska boken "Clean Code" av "Robert C. Martin" finnas i katalogen
    And ska boken "Refactoring" av "Martin Fowler" finnas i katalogen

  Scenario: En tillagd bok kan hjärtmarkeras
    Given jag lägger till boken "Clean Code" av "Robert C. Martin"
    And jag går till vyn "Katalog"
    When jag klickar på hjärtat för "Clean Code"
    And jag går till vyn "Mina böcker"
    Then ska "Clean Code" finnas bland mina böcker
