![image](https://github.com/user-attachments/assets/b0945086-c5b0-4ea1-938d-244876dda117)

# Bin2C-PySide6

`Bin2C-PySide6`는 `Bin2C` 프로그램을 클론코딩한 것이며, 바이너리 파일을 **C 배열 형식으로 변환**하는 PySide6 기반 GUI 애플리케이션입니다.

## 🔹 사용 환경 (System Requirements)
✅ **운영체제**: Windows 10 이상, macOS 11(Big Sur) 이상, Linux (Ubuntu 20.04 이상)  
✅ **Python 버전**: Python **3.8 ~ 3.13** 지원  
✅ **필수 라이브러리**: `PySide6`  
✅ **권장 사양**: 최소 2GB RAM, 100MB 여유 디스크 공간  

## 🚀 기능
- **파일 선택**: 바이너리 파일을 선택하여 변환
- **C 배열 변환**: 변환된 데이터를 `unsigned char`, `unsigned short`, `unsigned int` 형식으로 출력
- **데이터 크기 선택**: `1 byte`, `2 byte`, `4 byte` 단위 선택 가능
- **출력 개수 설정**: 한 줄에 출력될 바이트 수 설정 가능
- **총 데이터 개수 출력**: 변환된 배열의 총 요소 개수 표시


## 🛠️ 설치 방법
Bin2C Converter는 `PySide6` 라이브러리를 사용합니다.

### 1️⃣ **Python 및 라이브러리 설치**
```bash
pip install PySide6
```

### 2️⃣ 프로젝트 다운로드
```bash
git clone https://github.com/your-repo/bin2c-converter.git
cd bin2c-converter
```

### 3️⃣ 실행
```bash
python main.py
```

## 🖥️ 사용법
- `Select File` 버튼을 클릭하여 변환할 바이너리 파일 선택
- `Bytes per line` 옵션에서 한 줄에 출력할 바이트 개수 설정
- `Data size` 옵션에서 변환할 데이터 크기 선택 (`1 byte`, `2 byte`, `4 byte`)
- `Convert to C Array` 버튼을 눌러 변환 실행
- 변환된 C 배열 코드와 총 데이터 개수를 확인

## 🏗️ 빌드 및 배포 (Standalone 실행파일 만들기)
### 1️⃣ PyInstaller 설치
```bash
pip install pyinstaller
```

### 2️⃣ Windows에서 실행 파일 (.exe) 생성
```bash
pyinstaller --onedir --windowed --name "Bin2C-OIS" main.py
```
`dist/Bin2C.exe` 파일이 생성됩니다.

### 3️⃣ macOS에서 .app 파일 생성
```bash
pyinstaller --onedir --windowed --icon=icon.icns --name "Bin2C-OIS" main.py
```
dist/Bin2C.app 파일이 생성됩니다.<br>
실행 오류가 발생하면 다음 명령어 실행:

```bash
xattr -dr com.apple.quarantine dist/Bin2C.app
```

## 📝 C 코드 출력 예시
### 1️⃣ 1 byte 변환 (unsigned char)

```c
unsigned char data[] = {
    0xDE, 0xAD, 0xBE, 0xEF, 0x00, 0x01, 0x02, 0x03,
    0xFF, 0xFE, 0xFD, 0xFC
};
```

### 2️⃣ 2 byte 변환 (unsigned short)

```c
unsigned short data[] = {
    0xBEEF, 0xADDE, 0x0201, 0x0000,
    0xFDFE, 0xFCFF
};
```


### 3️⃣ 4 byte 변환 (unsigned int)

```c
unsigned int data[] = {
    0xBEEFADDE, 0x00000201,
    0xFCFFFDFE
};
```

## 📜 라이선스 (License)
이 프로젝트는 LGPL v3 라이선스를 따릅니다.
Bin2C-OIS는 PySide6 (LGPL v3)를 기반으로 개발되었으며,
사용자는 소스 코드를 자유롭게 수정 및 배포할 수 있습니다.

### ⚠️ LGPL v3 라이선스 주의 사항:

이 프로그램을 수정한 경우, 수정된 소스를 제공해야 합니다.
PySide6의 원본 라이선스 (LGPL v3)를 유지해야 합니다.
이 소프트웨어를 다른 프로그램에 통합하여 배포할 경우,
LGPL v3 조건을 준수해야 합니다.
자세한 내용은 LICENSE 파일을 참조하세요.
