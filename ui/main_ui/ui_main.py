import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QLabel, QMessageBox, QDialog, QListView, QAbstractItemView
from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex
class SecondWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        """ Dùng ẻeer """
        self.setWindowTitle('Cửa sổ thứ hai')
        self.setGeometry(200, 200, 400, 300)

        # Tạo group box cho phần nhập dữ liệu
        input_groupbox = QGroupBox("Nhập dữ liệu")
        input_layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.input_label = QLabel("Số tiền chi tiêu")

        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_text)
        input_groupbox.setLayout(input_layout)

        # Tạo group box cho phần danh sách
        list_groupbox = QGroupBox("Danh sách")
        list_layout = QVBoxLayout()

        self.list_view = QListView()
        self.list_view.setSelectionMode(QAbstractItemView.MultiSelection)

        # Tạo mảng dữ liệu nhóm và option
        data = [
            {"group": "Nhóm 1", "option": ["Tùy chọn 1", "Tùy chọn 2", "Tùy chọn 3"]},
            {"group": "Nhóm 2", "option": ["Tùy chọn 4", "Tùy chọn 5", "Tùy chọn 6"]}
        ]

        model = OptionGroupModel(data)

        self.list_view.setModel(model)

        list_layout.addWidget(self.list_view)
        list_groupbox.setLayout(list_layout)

        # Tạo nút "Start"
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_button_clicked)

        # Tạo layout chính và thêm các group box vào layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(input_groupbox)
        main_layout.addWidget(list_groupbox)
        main_layout.addWidget(self.start_button)

        self.setLayout(main_layout)

    def start_button_clicked(self):
        # Xử lý sự kiện click của nút "Start"
        selected_indexes = self.list_view.selectedIndexes()
        selected_texts = [index.data() for index in selected_indexes]
        print("Các mục đã chọn:")
        for text in selected_texts:
            print(text)

from PyQt5.QtCore import QModelIndex, Qt, QAbstractItemModel

class OptionGroupModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent):
        if not parent.isValid():
            return len(self._data)
        elif parent.column() == 0:
            group = self._data[parent.row()]
            return len(group['option'])
        return 0

    def index(self, row, column, parent):
        if not parent.isValid():
            return self.createIndex(row, column)
        group = self._data[parent.row()]
        return self.createIndex(row, column, group['option'][row])

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        return QModelIndex()

    def data(self, index, role):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            if index.parent().isValid():
                group = self._data[index.parent().row()]
                return group['option'][index.row()]
            else:
                return self._data[index.row()]['group']
        return None
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    profiles = []

    def initUI(self):
        # Tạo group box cho phần login
        login_groupbox = QGroupBox("Login")
        login_layout = QVBoxLayout()

        self.login_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login_button_clicked)

        login_layout.addWidget(self.login_input)
        login_layout.addWidget(self.login_button)
        login_groupbox.setLayout(login_layout)

        # Tạo group box cho phần danh sách
        list_groupbox = QGroupBox("Danh sách Profile")
        list_layout = QVBoxLayout()

        self.list_view = QListWidget()
        self.list_view.setSelectionMode(QListWidget.MultiSelection)

        # Tạo mảng dữ liệu
        from source.source_genloin.gen_connect import GenloginConnection
        info_gen = GenloginConnection().get_profile(0,999)
        print(info_gen)
        for i in info_gen['profiles']:
            try:
                self.profiles.append(
                    {"name": i['profile_data']['name'], "profile_group_ids": i["profile_group_ids"][0], "id": i["id"]})
            except:
                self.profiles.append(
                    {"name": i['profile_data']['name'], "profile_group_ids": "0", "id": i["id"]})


        self.data = [i["name"] for i in self.profiles]

        # Nhúng mảng dữ liệu vào danh sách
        self.update_list_view()

        self.print_button = QPushButton("Trả Quest")
        self.print_button.clicked.connect(self.print_button_clicked)

        self.select_all_button = QPushButton("Chọn tất cả")
        self.select_all_button.clicked.connect(self.select_all_button_clicked)

        self.deselect_all_button = QPushButton("Bỏ chọn tất cả")
        self.deselect_all_button.clicked.connect(self.deselect_all_button_clicked)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Tìm kiếm...")
        self.search_input.textChanged.connect(self.search_text_changed)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_button_clicked)

        # Thêm các nút chọn tất cả và bỏ chọn tất cả vào layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.select_all_button)
        button_layout.addWidget(self.deselect_all_button)
        button_layout.addWidget(self.search_input)
        button_layout.addWidget(self.reset_button)

        list_layout.addWidget(self.list_view)
        list_layout.addWidget(self.print_button)
        list_layout.addLayout(button_layout)
        list_groupbox.setLayout(list_layout)

        # Tạo layout chính và thêm các group box vào layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(login_groupbox)
        main_layout.addWidget(list_groupbox)

        self.setLayout(main_layout)

        # Cài đặt cửa sổ
        self.setWindowTitle('Thanh Automation')
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def login_button_clicked(self):
        # Xử lý sự kiện click của button login
        username = self.login_input.text()
        if username.strip():  # Kiểm tra xem người dùng có nhập dữ liệu không
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công!")
        else:
            QMessageBox.warning(self, "Thông báo", "Đăng nhập thất bại! liên hệ tele @Thanh2218")

    def print_button_clicked(self):
        # Mở profile
        from ui import click_open_multiple
        profiles = []

        # Danh sách
        selected_items = self.list_view.selectedItems()
        selected_texts = [item.text() for item in selected_items]
        print("Danh sách các mục đã chọn:")
        try:
            for text in selected_texts:
                for item in self.profiles:
                    if item.get("name") == text:
                        profiles.append(item)
        except Exception as e:
            print(e)
        print("text > ",profiles)
        click_open_multiple.open_profile(profiles)
        # Xử lý sự kiện click của button in danh sách
        # second_window = SecondWindow()
        # second_window.exec_()

    def select_all_button_clicked(self):
        # Chọn tất cả các mục trong danh sách
        for i in range(self.list_view.count()):
            item = self.list_view.item(i)
            item.setSelected(True)

    def deselect_all_button_clicked(self):
        # Bỏ chọn tất cả các mục trong danh sách
        for i in range(self.list_view.count()):
            item = self.list_view.item(i)
            item.setSelected(False)

    def search_text_changed(self):
        # Xử lý sự kiện khi người dùng thay đổi nội dung của ô tìm kiếm
        keyword = self.search_input.text()
        self.update_list_view(keyword)

    def reset_button_clicked(self):
        # Xử lý sự kiện khi người dùng nhấn vào nút reset
        self.search_input.clear()
        self.update_list_view()

    def update_list_view(self, keyword=None):
        # Cập nhật danh sách hiển thị trong list view dựa trên từ khóa tìm kiếm
        self.list_view.clear()
        if keyword:
            filtered_data = [item for item in self.data if keyword.lower() in item.lower()]
            self.list_view.addItems(filtered_data)
        else:
            self.list_view.addItems(self.data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
