monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print (monthConversions["Mar"])
print (monthConversions.get("Feb"))
print (monthConversions.get("Jul", "if you dont want null, give some default value here so that it will be printed"))