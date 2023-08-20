import paralleldots
paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

def ner(text):
    response = paralleldots.ner(text)
    return response

def sentiment_analysis(text):
    response = paralleldots.sentiment(text)
    return response