Feature: ERPLY Point of Sale product search.
  As a web surfer,
  I want to login into application,
  so that I can search for the product available in the application.

  Background:
    Given the home page is displayed
    When fill "104572" and  "testassignment" then "PosTestAssignment123"
    Then verify applicaiton is rendered

 Scenario Outline: verify search for the product
    Given the search function with <some> value
    When maximum <rows> displayed
    Then select the <product>
    And verify the <product> result
   Examples:
     | some         | rows | product           |
     | empty        | 3    | Fanta             |
     | fanta        | 1    | Fanta             |
     | FANTA        | 1    | Fanta             |
     | €            | 1    | No results found. |
     | *&^          | 1    | No results found. |
     | 12           | 1    | No results found. |
     | 00           | 2    | Fanta             |
     | 00           | 2    | Example product   |
     | "          " | 1    | No results found. |
     | "          " | 2    | Fanta             |


  Scenario: verify exit-X button at search for the product
    Given the search function with fanta value
    When clicking at x button
    Then searched product should not be added

  Scenario: verify search icon functionality from the result
    Given the search function with straw value
    When clicking at search icon button
    Then searched product should not be added
    And product details should be displayed

  Scenario: verify selected search item is addition into receipt
    Given the search function with straw value
    Then select the Strawberry-Banana Margarita
    And the search function with straw value
    And select the Strawberry-Banana Margarita
    Then check 2 quatities added into receipt

  Scenario: verify multiple selected search item is addition into receipt
    Given the search function with straw value
    Then select the Strawberry-Banana Margarita
    And the search function with straw value
    And select the Strawberry-Banana Margarita
    Then the search function with Fanta value
    And select the Fanta
    Then the search function with straw value
    And select the Strawberry-Banana Margarita
    Then check 3 quatities of Strawberry-Banana Margarita added into receipt

  Scenario: search with accessibility F9
    Given the accessibility functionality through F9
    Then enter fanta into the product search box
    And select the Fanta product
    Then verify the Fanta result