def person_info(name, age):
info = {}
info['name'] = upper_name = name.upper()
info['age_in_10_years'] = age + 10
info['is_adult'] = age >= 18
return info
adult = person_info("ali", 30)
print(adult)
