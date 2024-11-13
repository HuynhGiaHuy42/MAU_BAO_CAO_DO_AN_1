import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#2e2e2e")  # Màu nền cho giao diện chính
        
        # Entry để hiển thị các phép tính
        self.entry = tk.Entry(
            root, font=("Helvetica", 28, "bold"), borderwidth=5, relief="solid", 
            justify="right", bg="#2e2e2e", fg="white", insertbackground="white"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Khởi tạo biến để lưu phép tính
        self.expression = ""
        
        # Định nghĩa các nút bấm cùng với màu sắc và font chữ
        buttons = [
            ('7', '#4a4a4a'), ('8', '#4a4a4a'), ('9', '#4a4a4a'), ('/', '#ff9500'),
            ('4', '#4a4a4a'), ('5', '#4a4a4a'), ('6', '#4a4a4a'), ('*', '#ff9500'),
            ('1', '#4a4a4a'), ('2', '#4a4a4a'), ('3', '#4a4a4a'), ('-', '#ff9500'),
            ('0', '#4a4a4a'), ('.', '#4a4a4a'), ('=', '#ff9500'), ('+', '#ff9500')
        ]
        
        # Tạo các nút và định vị chúng trong giao diện
        row_val = 1
        col_val = 0
        for button_text, color in buttons:
            self.create_button(button_text, color, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Nút Clear (Xóa)
        self.clear_button = tk.Button(
            root, text="C", font=("Helvetica", 18, "bold"), bg="#d32f2f", fg="white",
            command=self.clear, relief="flat", highlightthickness=0, activebackground="#e57373"
        )
        self.clear_button.grid(row=row_val, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
    
    # Hàm tạo nút với các thông số về giá trị, màu sắc và vị trí
    def create_button(self, value, color, row, col):
        button = tk.Button(
            self.root, text=value, font=("Helvetica", 20, "bold"), bg=color, fg="white",
            command=lambda: self.click(value), relief="flat", highlightthickness=0, 
            activebackground="#555555"
        )
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    
    # Hàm xử lý khi người dùng nhấn nút
    def click(self, value):
        if value == "=":
            self.calculate()  # Tính toán khi nhấn "="
        else:
            self.expression += str(value)  # Thêm giá trị vào biểu thức
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
    
    # Hàm thực hiện tính toán
    def calculate(self):
        try:
            result = str(eval(self.expression))  # Sử dụng eval để tính toán biểu thức
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = result  # Lưu kết quả để tiếp tục tính toán
        except Exception:
            messagebox.showerror("Error", "Invalid Input")  # Hiển thị thông báo lỗi nếu biểu thức không hợp lệ
            self.clear()
    
    # Hàm xóa biểu thức hiện tại
    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

# Chạy ứng dụng
root = tk.Tk()
calculator = Calculator(root)

# Cấu hình các dòng và cột để giao diện tự điều chỉnh khi thay đổi kích thước
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
