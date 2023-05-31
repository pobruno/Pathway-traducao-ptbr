import json
from translate import Translator

# Array com os caminhos dos arquivos JSON
json_paths = [
    "./pt-BR/Achievements.json",
    "./pt-BR/Codex.json",
    "./pt-BR/Events.json",
    "./pt-BR/GameUI.json",
    "./pt-BR/Items.json",
    "./pt-BR/Perks.json",
    "./pt-BR/Quotes.json",
    "./pt-BR/Tutorial.json"
]

# Crie uma instância do tradutor
translator = Translator(to_lang="pt")

# Percorra os arquivos JSON
for json_path in json_paths:
    # Carregue o arquivo JSON
    with open(json_path, "r", encoding="utf-8") as json_file:
        json_content = json.load(json_file)

    # Percorra os objetos e traduza o campo "text"
    for row in json_content["rows"]:
        translated = translator.translate(row["text"])
        row["text"] = translated

    # Salve o arquivo JSON traduzido
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)



#Test V2

#from translate import Translator
#import json
#
## Carregue o arquivo JSON
#json_path = "./pt-BR/Achievements.json"
#with open(json_path, "r", encoding="utf-8") as json_file:
#    json_content = json.load(json_file)
#
## Crie uma instância do tradutor
#translator = Translator(to_lang="pt")
#
## Percorra os objetos e traduza o campo "text"
#for row in json_content["rows"]:
#    translated = translator.translate(row["text"])
#    row["text"] = translated
#
## Salve o arquivo JSON traduzido
#with open(json_path, "w", encoding="utf-8") as json_file:
#    json.dump(json_content, json_file, ensure_ascii=False, indent=4)


# Test v1

#import json
#from googletrans import Translator
#
## Carregue o arquivo JSON
#json_path = "./pt-BR/Achievements.json"
#
#with open(json_path, "r", encoding="utf-8") as json_file:
#    json_content = json.load(json_file)
#
## Crie uma instância do tradutor do Google
#translator = Translator(service_urls=["translate.google.com"])
#
## Percorra os objetos e traduza o campo "text"
#for row in json_content["rows"]:
#    translated = translator.translate(row["text"], dest="pt")
#    row["text"] = translated.text
#
## Salve o arquivo JSON traduzido
#with open(json_path, "w", encoding="utf-8") as json_file:
#    json.dump(json_content, json_file, ensure_ascii=False, indent=4)



