from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QSpinBox, QLabel
import sys

class Bin2CApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bin2C Converter")
        self.setGeometry(100, 100, 600, 500)  # 창 크기 설정

        # 레이아웃 생성
        layout = QVBoxLayout()

        # 파일 선택 버튼
        self.select_button = QPushButton("Select File")
        self.select_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.select_button)

        # 한 줄당 출력 개수 설정 라벨 및 SpinBox
        self.line_length_label = QLabel("Bytes per line:")
        layout.addWidget(self.line_length_label)

        self.line_length_input = QSpinBox()
        self.line_length_input.setRange(1, 32)  # 최소 1개, 최대 32개
        self.line_length_input.setValue(8)  # 기본값 8개
        layout.addWidget(self.line_length_input)

        # 변환 버튼
        self.convert_button = QPushButton("Convert to C Array")
        self.convert_button.clicked.connect(self.convert_file)
        layout.addWidget(self.convert_button)

        # 변환된 코드 출력 창
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        # 레이아웃 설정
        self.setLayout(layout)

        # 선택된 파일 경로 저장 변수
        self.selected_file = None

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")

        if file_path:
            self.selected_file = file_path
            self.select_button.setText(f"Selected: {file_path.split('/')[-1]}")
        else:
            self.selected_file = None
            self.select_button.setText("Select File")

    def convert_file(self):
        if not self.selected_file:
            self.result_text.setText("No file selected!")
            return

        try:
            with open(self.selected_file, 'rb') as f:
                data = f.read()

            # 사용자 설정 값을 가져오기
            bytes_per_line = self.line_length_input.value()

            # 바이너리를 C 배열 형식으로 변환 (정렬 포함)
            c_array_lines = []
            for i in range(0, len(data), bytes_per_line):
                chunk = data[i:i + bytes_per_line]
                formatted_chunk = ', '.join(f'0x{byte:02X}' for byte in chunk)
                c_array_lines.append(f"    {formatted_chunk}")

            # 최종 C 코드 포맷
            c_code = (
                "unsigned char data[] = {\n"
                + ",\n".join(c_array_lines) +
                "\n};"
            )

            # 결과 표시
            self.result_text.setText(c_code)
        except Exception as e:
            self.result_text.setText(f"Error: {str(e)}")

# PySide 앱 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Bin2CApp()
    window.show()
    sys.exit(app.exec())