import pandas as pd

# Bước 1: Đọc dữ liệu từ Google Sheets
url = "https://docs.google.com/spreadsheets/d/1BnOzoEG0s6c8MpiUANZ0_pawXNHqdkid/export?format=csv"
df = pd.read_csv(url)

# Bước 2: Lọc dữ liệu theo điều kiện: vpv2 và pDisCharge chẵn, prec lẻ
df_filtered = df[(df['vpv2'] % 2 == 0) & 
                 (df['pDisCharge'] % 2 == 0) & 
                 (df['prec'] % 2 == 1)].copy()

# Bước 3: Tính tổng vBus1 và vBus2 → cột Sum_vBUS
df_filtered.loc[:, 'Sum_vBUS'] = df_filtered['vBus1'] + df_filtered['vBus2']

# Bước 4: Lưu dữ liệu đã xử lý vào file CSV
df_filtered.to_csv("Data.csv", index=False)

print(" Đã lưu kết quả vào file Data_new.csv thành công.")