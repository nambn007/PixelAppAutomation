import json
from typing import List

from source.source_genloin.Genlogin import Genlogin
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class GenloginConnection:
    def __init__(self):
        self.gen = Genlogin("")

    def get_profile(self, offset: int, limit: int) -> List[dict]:
        return self.gen.getProfiles(offset, limit)

    def get_id_by_group_profile(self, profile_group_ids: int) -> List[int]:
        gen = self.gen.getProfiles(0, 30)
        # Lọc các hồ sơ có "profile_group_ids"
        return [profile["id"] for profile in gen['profiles'] if
                profile['profile_group_ids'] == [profile_group_ids]]

    def get_id_profile_running(self):
        gen = self.gen.getProfilesRunning()
        # Lọc các hồ sơ có "profile_group_ids"
        return [profile["id"] for profile in gen['data']]
class GenloginAction:
    def __init__(self):
        self.gen = Genlogin("")

    def startProfile(self, profile_id: int) -> str:
        wsEndpoint = self.gen.runProfile(profile_id)["wsEndpoint"].replace("ws://", "").split('/')[0]
        return wsEndpoint

    def stop_profile(self, profile_id) -> None:
        # self.gen.stopProfile(profile_id)
        pass











