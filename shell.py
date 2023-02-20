#called shell , trynna make a languge, gonna try to make a lexor that can read tokens
import basic

while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)