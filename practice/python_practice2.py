counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
print(counties_dict.items())
for county in counties_dict:
    print(county)
for voters in counties_dict:
    print(voters)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, voters)
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters")
voting_data = [{"county":"Arapahoe", "registered_voters":422829}, {"county":"Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]
print(voting_data)
for county in range(len(voting_data)):

