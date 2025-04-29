import pandas as pd

# Lớp Info_Xe chứa thông tin xe
class Info_Xe:
    def __init__(self, loai_xe, chu_xe, thoi_gian, bien_so_xe=None):
        self.loai_xe = loai_xe
        self.chu_xe = chu_xe
        self.thoi_gian = thoi_gian  # thời gian gửi xe tính theo giờ
        self.bien_so_xe = bien_so_xe

    def __str__(self):
        return f"Loại xe: {self.loai_xe}, Chủ xe: {self.chu_xe}, Thời gian gửi xe: {self.thoi_gian} giờ, Biển số: {self.bien_so_xe if self.bien_so_xe else 'Không có'}"

# Lớp Money_Time chứa thông tin về giá xe
class Money_Time:
    def __init__(self):
        # Định nghĩa giá tiền cho các loại xe
        self.gia_xe = {
            "Xe đạp": 2,
            "Xe máy": 5,
            "Xe điện": 3.5,
            "Ô tô": 10
        }
    
    def tinh_gia(self, loai_xe, thoi_gian):
        # Tính giá gửi xe theo loại xe và thời gian
        if loai_xe in self.gia_xe:
            return self.gia_xe[loai_xe] * thoi_gian
        return 0  # Nếu loại xe không hợp lệ, trả về 0

# Quản lý các xe gửi
class QuanLyXe:
    def __init__(self):
        self.danh_sach_xe = []
        self.money_time = Money_Time()

    def them_xe(self, xe):
        self.danh_sach_xe.append(xe)
    
    def sua_xe(self, bien_so_xe, loai_xe=None, chu_xe=None, thoi_gian=None):
        for xe in self.danh_sach_xe:
            if xe.bien_so_xe == bien_so_xe:
                if loai_xe: xe.loai_xe = loai_xe
                if chu_xe: xe.chu_xe = chu_xe
                if thoi_gian: xe.thoi_gian = thoi_gian
                break

    def xoa_xe(self, bien_so_xe):
        self.danh_sach_xe = [xe for xe in self.danh_sach_xe if xe.bien_so_xe != bien_so_xe]

    def tinh_gia_xe(self):
        # Tính tổng chi phí cho mỗi xe
        for xe in self.danh_sach_xe:
            xe.gia_gui = self.money_time.tinh_gia(xe.loai_xe, xe.thoi_gian)
    
    def xuat_thong_tin_xe_tren_20k(self):
        # Xuất thông tin xe có giá gửi trên 20k
        xe_tren_20k = [xe for xe in self.danh_sach_xe if xe.gia_gui > 20]
        return xe_tren_20k
    
    def ghi_du_lieu_vao_excel(self, filename="data_xe.xlsx"):
        # Ghi dữ liệu xe vào file Excel
        data = []
        for xe in self.danh_sach_xe:
            data.append([xe.loai_xe, xe.chu_xe, xe.thoi_gian, xe.bien_so_xe, xe.gia_gui])
        df = pd.DataFrame(data, columns=["Loại xe", "Chủ xe", "Thời gian gửi", "Biển số xe", "Giá gửi"])
        df.to_excel(filename, index=False)

# Chạy thử chương trình
ql_xe = QuanLyXe()

# Thêm một số xe vào danh sách
ql_xe.them_xe(Info_Xe("Xe đạp", "Nguyễn Văn A", 10, "29A-12345"))
ql_xe.them_xe(Info_Xe("Xe máy", "Trần Thị B", 3, "29B-67890"))
ql_xe.them_xe(Info_Xe("Xe điện", "Lê Minh C", 7, "29C-11223"))
ql_xe.them_xe(Info_Xe("Ô tô", "Hoàng Vũ D", 2, "29D-44556"))

# Tính toán giá gửi xe
ql_xe.tinh_gia_xe()
# In thông tin những xe có giá trên 20k
xe_tren_20k = ql_xe.xuat_thong_tin_xe_tren_20k()
print("Thông tin những xe có giá gửi trên 20k:")
for xe in xe_tren_20k:
    print(xe)

# Ghi dữ liệu vào file Excel
ql_xe.ghi_du_lieu_vao_excel("gui_xe.xlsx")