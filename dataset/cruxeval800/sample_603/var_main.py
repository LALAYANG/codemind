def f(sentences):
    if all([sentence.isdecimal() for sentence in sentences.split('.')]):	## {"sentence" : '',"sentences" : ''}
        return 'oscillating' 
    else:
        return 'not oscillating'