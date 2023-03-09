import defe2

while True:
    text = input('SC >')

    result, error = defe2.run('<srdin>', text)

    if error: 
        print(error.as_string())
    else:
        print(result)