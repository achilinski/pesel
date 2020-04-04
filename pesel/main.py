from pesel import validate, info


def date_getter(pesel):
    validator=validate.Validator(pesel)
    info_getter=info.Info(pesel)
    validator.checker()
    return info_getter.birth_date()

def gender_getter(pesel):
    validator=validate.Validator(pesel)
    info_getter=info.Info(pesel)
    validator.checker()
    return info_getter.gender_getter()


