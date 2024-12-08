Feature: Validate car registrations

  Scenario: Validate the car registrations with input and output files
    Given User reads the input file "resources/input/car_input.txt"
    When User extracts vehicle registration numbers based on patterns
    Then User compares results of registration numbers from the website with the output file
