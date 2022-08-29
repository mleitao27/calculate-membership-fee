# calculate-membership-fee
Python script that calculates the membership fee paid by the tenants for a flatbond.

## Usage
Run:
```
$ python main.py <rent_amount> <rent_period> <organisation_unit>
```
  
## Data model
I used the provided example data and added a field with the parent organisation unit to each entry on the data array to better highlight the origanisation's structure and facilitate the search for each unit's configuration.
  
## Big O notation
O(4N), where N is the size of the client's organisation data array.

## Some assumptions
- When calculating the fee (one week of rent + VAT) for "month" rent periods I assumed that each month was composed of 4 weeks.

## Future iterations
- Get some hard coded values such as rent limits, VAT percentage and minimum rent from a configuration file.
