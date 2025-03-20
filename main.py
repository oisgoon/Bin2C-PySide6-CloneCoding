from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView

class Bin2CApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # 파일 선택기
        self.file_chooser = FileChooserListView(size_hint_y=0.8)
        layout.add_widget(self.file_chooser)

        # 변환 버튼
        self.convert_button = Button(text='Convert to C Array', size_hint_y=0.1)
        self.convert_button.bind(on_press=self.convert_file)
        layout.add_widget(self.convert_button)

        # 변환된 코드 표시
        self.result_text = TextInput(readonly=True, size_hint_y=0.1)
        layout.add_widget(self.result_text)

        return layout

    def convert_file(self, instance):
        selection = self.file_chooser.selection
        if not selection:
            self.result_text.text = "No file selected!"
            return

        try:
            with open(selection[0], 'rb') as f:
                data = f.read()

            # 바이너리를 C 배열 형식으로 변환
            c_array = ', '.join(f'0x{byte:02X}' for byte in data)

            # 결과 표시
            self.result_text.text = f"unsigned char data[] = {{{c_array}}};"
        except Exception as e:
            self.result_text.text = f"Error: {str(e)}"

if __name__ == '__main__':
    Bin2CApp().run()