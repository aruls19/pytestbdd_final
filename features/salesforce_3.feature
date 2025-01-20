Feature: Salesforce functionality

  Scenario: Use case2-Create an account and attach the contact and opportunity
    Given I am logged in to salesforce
    When I am create an account
    And create contact and attach to created account
    And create opportunity and attach to created account
    Then Contact and opportunity should successfully attached with account
