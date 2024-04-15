import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from service.login_service import LoginService
from source.source_genloin.gen_connect import GenloginConnection, GenloginAction
from thread.threading_multi import ThreadingMulti

APP_NAME = "PixelAppAutomation"


class LoginWidget(QWidget):
    def __init__(self):
        super(LoginWidget, self).__init__()

        self.setWindowTitle(APP_NAME)
        self.setGeometry(300, 300, 300, 150)

        self.login_input = QLineEdit()
        self.login_button = QPushButton("Login")

        self.login_layout = QVBoxLayout()
        self.login_layout.addWidget(self.login_input)
        self.login_layout.addWidget(self.login_button)

        login_groupbox = QGroupBox("Login")
        login_groupbox.setLayout(self.login_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(login_groupbox)

        self.setLayout(self.main_layout)


class ProfilePixelWidget(QWidget):
    def __init__(self):
        super(ProfilePixelWidget, self).__init__()

        self.profiles = []
        self.get_profiles()
        self.list_profiles_name = [profile["name"] for profile in self.profiles]

        self.setWindowTitle(APP_NAME)
        self.setGeometry(300, 300, 400, 300)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        list_profile_groupbox = QGroupBox("List profile")
        self.list_view = QListWidget()
        self.list_view.setSelectionMode(QListWidget.MultiSelection)
        self.update_list_view_profile()

        self.return_quest_button = QPushButton("Return Quest")
        self.return_quest_button.clicked.connect(self.return_quest_button_clicked)

        self.select_all_profile_button = QPushButton("Select all")
        self.select_all_profile_button.clicked.connect(self.select_all_profile_clicked)

        self.unselect_all_profile_button = QPushButton("Unselect all")
        self.unselect_all_profile_button.clicked.connect(self.unselect_all_profile_clicked)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_button_clicked)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Searching...")
        self.search_input.textChanged.connect(self.search_text_changed)

        functional_layout = QHBoxLayout()
        functional_layout.addWidget(self.select_all_profile_button)
        functional_layout.addWidget(self.unselect_all_profile_button)
        functional_layout.addWidget(self.search_input)
        functional_layout.addWidget(self.reset_button)
        list_profile_groupbox.setLayout(functional_layout)

        self.main_layout.addWidget(self.list_view)
        self.main_layout.addWidget(self.return_quest_button)
        self.main_layout.addWidget(list_profile_groupbox)

    def reset_button_clicked(self):
        self.search_input.clear()
        self.update_list_view_profile()

    def search_text_changed(self):
        keyword = self.search_input.text()
        self.update_list_view_profile(keyword)

    def select_all_profile_clicked(self):
        for i in range(self.list_view.count()):
            item = self.list_view.item(i)
            item.setSelected(True)

    def unselect_all_profile_clicked(self):
        for i in range(self.list_view.count()):
            item = self.list_view.item(i)
            item.setSelected(False)

    def return_quest_button_clicked(self):
        print("Hello world")
        selected_profiles = []
        selected_items = self.list_view.selectedItems()
        selected_texts = [item.text() for item in selected_items]
        print("Hello world 1")
        try:
            for text in selected_texts:
                for profile in self.profiles:
                    if text == profile.get("name"):
                        selected_profiles.append(profile)
        except Exception as e:
            print(e)
        print("Hello world 2")
        selected_profiles_id = [profile["id"] for profile in selected_profiles]
        try:
            ThreadingMulti().start_thread(profiles_id=selected_profiles_id)
            ThreadingMulti().stop_thread()
            print("Hello world 3")
        except Exception as e:
            print(e)
            ThreadingMulti().stop_thread()
            [GenloginAction().stop_profile(profiles_id=id) for id in selected_profiles_id]

    def update_list_view_profile(self, keyword=None):
        self.list_view.clear()
        if keyword:
            filtered_data = [item for item in self.list_profiles_name if keyword.lower() in item.lower()]
            self.list_view.addItems(filtered_data)
        else:
            self.list_view.addItems(self.list_profiles_name)

    def get_profiles(self):
        info_gen = GenloginConnection().get_profile(0, 999)
        for profile in info_gen["profiles"]:
            try:
                self.profiles.append(
                    {"name": profile['profile_data']['name'],
                     "profile_group_ids": profile["profile_group_ids"][0],
                     "id": profile["id"]})
            except Exception as e:
                print(e)
                self.profiles.append(
                    {"name": profile['profile_data']['name'],
                     "profile_group_ids": "0",
                     "id": profile["id"]})


class PixelApp(QApplication):
    def __init__(self):
        super(PixelApp, self).__init__(sys.argv)

        self.login_widget = LoginWidget()
        self.profile_widget = ProfilePixelWidget()

        # For LoginWidget
        self.login_widget.login_button.clicked.connect(self.login_button_clicked)
        self.login_widget.show()
        self.is_logged = False
        # For ProfilesWidget

    def login_button_clicked(self):
        token = self.login_widget.login_input.text()
        print('Token is', token)
        self.is_logged = True
        if self.is_logged:
            self.login_widget.hide()
            self.profile_widget.show()


if __name__ == "__main__":
    pixel_app = PixelApp()
    pixel_app.exec_()
