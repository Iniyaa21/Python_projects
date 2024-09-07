from openpyxl import Workbook, load_workbook


def add_data():
    wb = Workbook()
    ws = wb.active
    ws.title = "Attendance"
    ws.append(["roll no", "mail id", "CI", "python", "data mining"])
    n = int(input("Enter the number of students: "))

    for i in range(n):
        print("FOR ROLL NO", i+1, ":\n")
        mail = input("Enter mail id: ")
        ws.append([i+1, mail, 0, 0, 0])
        print("\n\n\n")

    wb.save(r"C:\Users\kavit\OneDrive\Desktop\Attendance.xlsx")
