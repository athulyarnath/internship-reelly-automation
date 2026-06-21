Feature: QA Automation Reelly project

  Scenario: QAAR-1337-22 User can open the market tab and filter by agent option
    Given Open the main page
    When Click continue button after filling credentials
    Then Verify logo is visible in home page
    When Click on “market” in the left side menu.
    Then Verify the right page opens
    When Click on “Agent” filter at the top of the page
    Then Verify that all results shown have the “Agent” tag.

    Scenario: QAAR-1337-22 User can open the market tab and filter by agent option - Mobile
      Given Open the main page
      When Click continue button after filling credentials
      Then Verify logo is visible in home page
