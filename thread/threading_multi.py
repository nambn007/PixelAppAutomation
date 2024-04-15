import threading
from typing import List
import const
from source.source_genloin.gen_connect import GenloginAction
from thread import action_thread


class ThreadingMulti:
    def __init__(self):
        self.threads = []

    def start_thread(self, profiles_id: List[int]) -> None:
        for index, id in enumerate(profiles_id):
            print(f"Starting thread - profile id: {id}")
            ws_endpoint: str = GenloginAction().startProfile(profile_id=id)
            driver = const.chorm_driver(ws_endpoint=ws_endpoint, index=index)
            thread = threading.Thread(target=action_thread.action, args=(driver, id))
            thread.start()
            self.threads.append(thread)

    def stop_thread(self) -> None:
        print(f"Finishing thread")
        for thread in self.threads:
            thread.join()
        print("All threads finished")
