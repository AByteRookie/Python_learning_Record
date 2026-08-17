def describe_city(city, country= 'france'):
    print(f"{city.title()} is in {country.title()}!")
    
describe_city('santiago', 'chile')
describe_city('paris')
describe_city('beijing', 'china')