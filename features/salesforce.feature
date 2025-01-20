Feature: Salesforce functionality

  Scenario: Use case1-Log in salesforce and create a lead and convert by existing account
    Given I am logged in to salesforce
    When I am create a lead
    Then I am converting the lead to account by use existing account

