Feature: Salesforce 2 functionality

  Scenario: Use case1-Log in salesforce and create a lead and convert by create new account
    Given I am logged in to salesforce
    When I am create a lead
    Then I am converting the lead to account successfully by creating new account
