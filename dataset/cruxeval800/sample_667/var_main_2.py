def f(text):
    new_text = []	## new_text = []
    for i in range(len(text) // 3):	## text = []
        new_text.append(f"< {text[i * 3: i * 3 + 3]} level={i} >")
    last_item = text[len(text) // 3 * 3:]	## last_item = [] | text = []
    new_text.append(f"< {last_item} level={len(text) // 3} >")	## new_text = [] | last_item = [] | text = []
    return new_text	## new_text = []
