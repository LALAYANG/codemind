def f(text):
    return not any([c.isupper() for c in text])	## <state>c = CLRJ | text = CLRJ</state>
