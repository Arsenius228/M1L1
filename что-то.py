meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (большими буквами!): ")


if word in meme_dict.keys():
        # Что делать, если слово нашлось?
    print(meme_dict[word])
else:
        # Что делать, если слово не нашлось?
    print('Лошараа')
