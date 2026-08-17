favorite_languages = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'phil': ['python'],
    'edward': ['ruby'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        if len(languages) == 2:
            print(f"\t{language.title()}")
        else:
            print(f"You should learn more languages.")
        
        