import requests
import pandas as pd

# Lấy danh sách Pokémon đầu tiên
pokemon_data = []
for i in range(1, 101):  # Lấy 100 Pokémon đầu tiên
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    if response.status_code == 200:
        p = response.json()
        pokemon_data.append({
            "number": p["id"],
            "name": p["name"],
            "type": ", ".join([t["type"]["name"] for t in p["types"]]),  # Lưu các type thành chuỗi
            "height": p["height"],
            "weight": p["weight"],
            "ThumbnailImage": p["sprites"]["front_default"]
        })

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(pokemon_data)

# Ghi dữ liệu vào file Excel
excel_file = "pokemon.csv"
df.to_excel(excel_file, index=False)

print(f"Dữ liệu đã được lưu vào file '{excel_file}'")

# Lọc các Pokémon có type = "poison"
poison_pokemon = df[df["type"].apply(lambda types: "poison" in types)]
print("\nCác Pokémon có type = poison:")
print(poison_pokemon)
