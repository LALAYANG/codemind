def f(text):
    if text.isalnum() and all(i.isdigit() for i in text):	## text = []
        return 'integer'
    return 'string'