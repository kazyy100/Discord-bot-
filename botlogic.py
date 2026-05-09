import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_anime_quote(anime):

    quote_pool = {
        "NARUTO": [
            {"quote": "Aku tidak akan menyerah! Aku tidak akan mengalah! Aku tidak AKAN MENINGGALKAN TEMAN-TEMANKU!", "character": "Naruto Uzumaki"},
            {"quote": "Aku tidak peduli seberapa kuat musuhku, aku akan terus berjuang sampai akhir!", "character": "Sasuke Uchiha"},
            {"quote": "Kekuatan sejati datang dari dalam dirimu sendiri, bukan dari kekuatan yang diberikan oleh orang lain.", "character": "Kakashi Hatake"},
            {"quote": "Aku tidak akan pernah melupakan teman-temanku, bahkan jika aku harus berjuang sendirian!", "character": "Sakura Haruno"},    
        ],

    }

    quote = random.choice(quote_pool[anime])

    return f"{quote['quote']} - {quote['character']}"
