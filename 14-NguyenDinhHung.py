student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh  vien <ten> thanh cong."
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh  vien {name} thanh cong.")
def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra tiêu đề "--- DANH SACH SINH VIEN ---".
    - Nếu danh sách trống, in ra "Danh sach trong.".
    - Nếu không, duyệt qua `student_list` và in thông tin mỗi sinh viên
      trên một dòng theo định dạng: " - Ten: [Họ tên], Nam sinh: [Năm sinh], Dia chi: [Địa chỉ]"
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
        return
    for s in student_list:
        print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")


if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")
    
    # Yêu cầu 2: In danh sách
    print("\n2. In danh sach sinh vien:")
    print_student_list()
