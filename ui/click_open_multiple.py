from typing import List

from source.source_genloin.gen_connect import GenloginConnection
from source.source_genloin.gen_connect import GenloginAction
from thread.threading_multi import ThreadingMulti


def open_profile(profiles:List[dict]):
    list_profiles_id = [i['id'] for i in profiles]
    try:
        ThreadingMulti().start_thread(profiles_id=list_profiles_id)

        ThreadingMulti().stop_thread()
    except Exception as e:
        print(e)
        ThreadingMulti().stop_thread()
        [GenloginAction().stop_profile(profiles_id=id) for id in list_profiles_id]