def parse(content):
    passport_data = content.split("\n\n")
    passports = []
    for data in passport_data:
        data2 = data.replace(" ", "\n").split("\n")
        dict_ = {items.split(":")[0]: items.split(":")[1] for items in data2 if items}
        passports.append(dict_)
    return passports
