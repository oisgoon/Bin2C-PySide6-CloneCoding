from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit,
    QFileDialog, QSpinBox, QLabel, QComboBox
)
import sys

class Bin2CApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bin2C Converter")
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()

        # 파일 선택 버튼
        self.select_button = QPushButton("Select File")
        self.select_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.select_button)

        # 한 줄당 출력 개수 설정
        self.line_length_label = QLabel("Bytes per line:")
        layout.addWidget(self.line_length_label)

        self.line_length_input = QSpinBox()
        self.line_length_input.setRange(1, 32)
        self.line_length_input.setValue(8)  # 기본값 8개
        layout.addWidget(self.line_length_input)

        # 데이터 크기 선택 (1, 2, 4 byte)
        self.byte_size_label = QLabel("Data size:")
        layout.addWidget(self.byte_size_label)

        self.byte_size_selector = QComboBox()
        self.byte_size_selector.addItems(["1 byte", "2 byte", "4 byte"])
        layout.addWidget(self.byte_size_selector)

        # 변환 버튼
        self.convert_button = QPushButton("Convert to C Array")
        self.convert_button.clicked.connect(self.convert_file)
        layout.addWidget(self.convert_button)

        # 변환된 코드 출력 창
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        # 배열 크기 출력 라벨
        self.array_size_label = QLabel("")
        layout.addWidget(self.array_size_label)

        self.setLayout(layout)
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

            # 사용자 설정 가져오기
            bytes_per_line = self.line_length_input.value()
            byte_size_option = self.byte_size_selector.currentText()
            byte_size = int(byte_size_option.split()[0])  # "1 byte" → 1

            # 데이터 크기 맞추기 (2 byte 또는 4 byte 선택 시 패딩 추가)
            if len(data) % byte_size != 0:
                padding = byte_size - (len(data) % byte_size)
                data += b'\x00' * padding  # 빈 공간을 0으로 패딩

            # C 배열 형식으로 변환
            c_array_lines = []
            for i in range(0, len(data), bytes_per_line * byte_size):
                chunk = data[i:i + (bytes_per_line * byte_size)]
                formatted_chunk = ', '.join(
                    f'0x{int.from_bytes(chunk[j:j+byte_size], "little"):0{byte_size*2}X}'
                    for j in range(0, len(chunk), byte_size)
                )
                c_array_lines.append(f"    {formatted_chunk}")

            # 총 배열 크기 출력
            array_size = len(data) // byte_size
            c_code = (
                f"unsigned {'short' if byte_size == 2 else 'int' if byte_size == 4 else 'char'} data[{array_size}] = {{\n"
                + ",\n".join(c_array_lines) +
                "\n};"
            )

            # 결과 출력
            self.result_text.setText(c_code)
            self.array_size_label.setText(f"Total Elements: {array_size} ({len(data)} bytes)")

        except Exception as e:
            self.result_text.setText(f"Error: {str(e)}")

# PySide 앱 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Bin2CApp()
    window.show()
    sys.exit(app.exec())