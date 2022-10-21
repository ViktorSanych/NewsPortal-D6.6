word_1 = 'редиска'
word_2 = 'баран'
Post_text = 'Есть много вариантов редиска Ipsum, но большинство из них имеет не всегда приемлемые баран.'


def censor(text):
    if not isinstance(text, str):
        raise ValueError('Можно применить только к строке!')    # Если строка, то в ней уже поищем плохие слова
    text = text.replace(word_1, 'р******')
    text = text.replace(word_2, 'б****')
    return text


print(censor(text=Post_text))
