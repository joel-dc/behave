Feature: Demo stuff things
  In order to look like I passed first grade
  As a person who has
  I want to demonstrate that I can greet others and count

  Scenario: greet
    Given a name
    When approached by others
    Then greet appropriately by saying hello
      | name      | greeting      |
      | Bob       | Hello, Bob    |
      | Jan       | Hello, Jan    |
      | Greg      | Hello, Greg   |

  Scenario: count
    Given an initialized counter
      | val |
      | 0   |
      | 1   |
    When the counter is incremented
    Then the counter should be incremented
      | incr |
      | 1    |
      | 2    |