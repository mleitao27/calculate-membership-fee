#!/usr/bin/python

import sys
import json

def get_unit_config(data, organisation_unit):
  for d in data:
    if d['name'] == organisation_unit:
      if d['config']:
        return d['config']
      elif not d['parent']:
        return None
      else:
        return get_unit_config(data, d['parent'])
  

def calculate_membership_fee(rent_amount, rent_period, organisation_unit):
  rent_amount = int(rent_amount)
  # Validating rent_amount
  if rent_amount < 1:
    print('ERROR : The rent amount must be at least 1')
    return -1
  elif rent_amount > sys.maxsize:
    print('ERROR : The rent amount must be not exceed ' + str(sys.maxsize))
    return -1
  
  # Validating rent_period
  if rent_period != 'week' and rent_period != 'month':
    print('ERROR : The rent period must be either "week" or "month"')
    return -1
  
  # Validating amount for period
  if rent_period == 'week' and rent_amount < 2500 or rent_amount > 200000:
    print('ERROR : For the "week" renting period the rent amount must be between 25£ and 2000£')
    return -1
  elif rent_period == 'month' and rent_amount < 11000 or rent_amount > 866000:
    print('ERROR : For the "month" renting period the rent amount must be between 110£ and 8660£')
    return -1
  
  # Opening JSON data file
  f = open('assets/data.json')
  # Returning JSON object
  data = json.load(f)
  # Closing file
  f.close()

  # Find unit config
  config = get_unit_config(data, organisation_unit)
  if not config:
    print('ERROR : Invalid structure in data file. No valid config found.')

  # Calculate fee
  if config['has_fixed_membership_fee']:
    print(config['fixed_membership_fee_amount'])
  else:
    match rent_period:
      case 'week':
        rent = rent_amount
      case 'month':
        # Assuming a month has 4 weeeks
        rent = rent_amount / 4
    if(rent < 12000):
      rent = 12000
    # Calculate VAT
    vat = rent * 0.2
    print(round(rent + vat))
    

def main():
  if len(sys.argv) < 2:
    print('ERROR : Missing rent amount')
  elif len(sys.argv) < 3:
    print('ERROR : Missing rent period')
  elif len(sys.argv) < 4:
    print('ERROR : Missing organisation unit')
  else:
    calculate_membership_fee(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()