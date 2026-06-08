def Display_student(student_list):
    print("\n----- HIỂN THỊ DANH SÁCH SINH VIÊN -------")
    if not student_list:
        print("danh sách không có sinh viên nào")
        return
    print(f"{"mã sv":<8} | {"Họ và tên":<12} | {"điểm toán":<10} | {"điểm lý":<10} | {"điểm hóa":<10} | {"trung bình":<10} | xếp loại học lực")
    print("-"*95)
    for student in student_list:
        print(f"{student['id']:<8} | {student['full_name']:<15} | {student['math_score']:<10.2f} | {student['physics_score']:<10.2f} | {student['chemistry_score']:<10.2f} | {student['average_score']:<10.2f} | {student['academic_ranking']}")
        print("-"*95)
def add_student():
    print("\n----- TIẾP NHẬN SINH VIÊN -------")
    while True:
        flag = False
        new_id = input("nhập mã sinh viên: ").strip.upper()
        for student in student_list:
            if student["id"] == new_id:
                flag = True
                break
        if flag:
            print(f"đã có id {new_id} vui lòng nhập lại!")
        else:
            break
    new_name = input("nhập tên sinh viên: ").strip()
    while True:
        try:
            new_math_score = float(input("Nhập điểm toán: "))
        except:
            print("điểm toán không hợp lệ") 
        if new_math_score >=0:
            break
        else:
            print("điểm toán phải >= 0")
    while True:
        try:
            new_physics_score = float(input("Nhập điểm lý: "))
        except:
            print("điểm lý không hợp lệ") 
        if new_physics_score >=0:
            break
        else:
            print("điểm lý phải >= 0")
    while True:
        try:
            new_chemistry_score = float(input("Nhập điểm hóa: "))
        except:
            print("điểm hóa không hợp lệ") 
        if new_chemistry_score >=0:
            break
        else:
            print("điểm hóa phải >= 0")
    new_average_score = (new_math_score + new_chemistry_score + new_physics_score) / 3
    new_academic_ranking = ""
    if new_average_score < 5.0:
        new_academic_ranking = "Yếu"
    elif new_average_score < 7.0:
        new_academic_ranking = "Trung bình"
    elif new_average_score < 8.0:
        new_academic_ranking = "khá"
    else:
        new_academic_ranking = "giỏi"
    new_student_list = {
        "id":new_id,
        "full_name": new_name,
        "math_score": new_math_score,
        "physics_score": new_physics_score,
        "chemistry_score": new_chemistry_score,
        "average_score": new_average_score,
        "academic_ranking": new_academic_ranking
    }
    student_list.append(new_student_list)
def  update_score():
    if not student_list:
        print("danh sách trống")
        return
    print("\n----- Cập nhật kết quả học tập --------")
    while True:
        flag = False
        id_update = input("nhập mã sinh viên muốn cập nhật: ")
        for student in student_list:
            if id_update == student["id"]:
                flag = True
                value = student
                break
        if flag:
            break
        else:
            print(f"không có sin viên nào có id {id_update}, vui lòng nhập lại")
    while True:
        try:
            new_math_score = float(input("Nhập điểm toán: "))
        except:
            print("điểm toán không hợp lệ") 
        if new_math_score >=0:
            break
        else:
            print("điểm toán phải >= 0")
    while True:
        try:
            new_physics_score = float(input("Nhập điểm lý: "))
        except:
            print("điểm lý không hợp lệ") 
        if new_physics_score >=0:
            break
        else:
            print("điểm lý phải >= 0")
    while True:
        try:
            new_chemistry_score = float(input("Nhập điểm hóa: "))
        except:
            print("điểm hóa không hợp lệ") 
        if new_chemistry_score >=0:
            break
        else:
            print("điểm hóa phải >= 0")
    new_average_score = (new_math_score + new_chemistry_score + new_physics_score) / 3
    new_academic_ranking = ""
    if new_average_score < 5.0:
        new_academic_ranking = "Yếu"
    elif  new_average_score < 7.0:
        new_academic_ranking = "Trung bình"
    elif new_average_score < 8.0:
        new_academic_ranking = "khá"
    else:
        new_academic_ranking = "giỏi"
    value["math_score"] = new_math_score
    value["physics_score"] = new_physics_score
    value["chemistry_score"]=new_chemistry_score
    value["average_score"] = new_average_score
    value["academic_ranking"] = new_academic_ranking
def delete_student(studnt_list):
    print("\n----- Xóa sinh viên --------")
    if not student_list:
        print("danh sách trống")
        return
    while True:
        flag = False
        id_update = input("nhập mã sinh viên muốn xóa: ")
        for index,student in enumerate(student_list):
            if id_update == student["id"]:
                flag = True
                value = index
                break
        if flag:
            break
        else:
            print(f"không có sin viên nào có id {id_update}, vui lòng nhập lại")
    confirm = input("xác nhận muốn xóa sinh viên (có/không): ").strip().lower()
    if confirm == "có":
       student_list.pop(value)
       print("xóa thành công")
    elif  confirm == "không":
        print("hủy xóa thành công")
    
def seach_student():
    if not student_list:
        print("Danh sách trống!")
        return
        
    name_search = input("Nhập tên hoặc id sinh viên muốn tìm kiếm: ").strip()
    for student in student_list:
        if student["id"] == name_search or name_search in student["full_name"]:
            Display_student([student])
            return     
    print(f"Không tìm thấy sinh viên có tên {name_search}.")
def statistics_rank():
    count_y = 0
    count_tb = 0
    count_k = 0
    count_g = 0
    for value in student_list:
        if value["average_score"] < 5.0:
           count_y+=1
        elif  value["average_score"] < 7.0:
           count_tb+=1
        elif value["average_score"] < 8.0:
            count_k +=1
        else:
            count_g+=1
    print("----- THỐNG KÊ --------")
    print(f"Giỏi: {count_g}")
    print(f"Khá: {count_k}")
    print(f"Trung bình : {count_tb}")
    print(f"Yếu: {count_y}")
student_list = [{
    "id":"SV001",
    "full_name":"Nguyen Van A",
    "math_score": 8.5,
    "physics_score": 7.0,
    "chemistry_score": 9.0,
    "average_score": 8.17,
    "academic_ranking": "giỏi"
}]
while True:
    print("\n-----MENU------")
    print("1. Hiển thị danh sách sinh viên ")
    print("2. Tiếp nhận sinh viên")
    print("3. Cập nhật kết quả học tập")
    print("4. xóa sinh viên")
    print("5. tìm kiếm sinh viên")
    print("6. thống kê điểm TB")
    print("7. Thoát")
    choice = input("nhập lựa chọn của bạn: ")
    match choice:
        case "1":
            Display_student(student_list)
        case "2":
            add_student()
        case "3":
            update_score()
        case "4":
            delete_student()
        case "5":
            seach_student()
        case "6":
            statistics_rank()
        case "7":
            print("thoát chương trình thành công")
            break
        case _:
            print("lựa chọn không hợp lệ")