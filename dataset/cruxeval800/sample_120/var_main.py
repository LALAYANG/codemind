def f(countries):
    language_country = dict()	## {"language_country" : ''}
    for country, language in countries.items():	## {"countries" : ''}
        if language not in language_country:
            language_country[language] = []
        language_country[language].append(country)
    return language_country	## {"language_country" : ''}
