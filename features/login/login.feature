Feature: Fight or flight
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  Background: Test
   Given This is testing background for "AWT-01"
  @test
  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
    When attacked by a samurai
    And attacked by a samurai
    Then the ninja should engage the opponent
  @Smoke
  Scenario Outline: Blenders
    Given I put <thing> in a blender,
    When I switch the blender on
    Then it should transform into <other thing>

    Examples: Amphibians
      | thing         | other thing |
      | Red Tree Frog | mush        |

    Examples: Consumer Electronics
      | thing        | other thing |
      | iPhone       | toxic waste |
      | Galaxy Nexus | toxic waste |
  @sanity
  Scenario: some scenario
    Given a set of specific users
      | name      | department  |
      | Barry     | Beer Cans   |
      | Pudey     | Silly Walks |
      | Two-Lumps | Silly Walks |

    When we count the number of people in each department
    And I do the same thing as before
    Then we will find two people in "Silly Walks"
    But we will find one person in "Beer Cans"
