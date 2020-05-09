def translate(phrase):
    translation=""
    for i in phrase:
        print(i)
        if i.lower() in "aeiou":
            if i.isupper():
                translation = translation + "G"
            else:
                translation= translation + "g"
        else:
            translation= translation + i
    return translation

print(translate(input("Enter a phrase: ")))
