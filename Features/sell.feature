Feature: Sell

  Scenario: Sell tab

    Given I open Application URL in the browser
    And I navigate to web page
    When I click on the Sell tab

  Scenario: Post Property

    Given I open Application URl in the browser
    And  I navigate to web page
    When I click on the Sell tab
    And I click the Post Property button
    And I am prompted to enter details about the seller type, property type, and WhatsApp number


  Scenario: View Ad Packages

    Given I open Application URl in the browser
    And  I navigate to web page
    When I click on the Sell tab
    And I click on the Ad Packages button
    Then I should see a list of available Ad Packages

  Scenario: ADVANTAGE POINTS FOR OWNERS - RESIDENTIAL & COMMERCIAL

    Given I open Application URl in the browser
    And  I navigate to web page
    When I click on the Sell tab
    And I click on the iAdvantage option
    Then I can add package to my cart
    And I should click on got to cart option

  Scenario: Search for agents by city
    Given I open Application URl in the browser
    And  I navigate to web page
    When I click on the Sell tab
    And I click on the Find an Agent button
    Then I should see a list of Top Agents in city and in particular area

