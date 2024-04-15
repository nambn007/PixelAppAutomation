from source.source_genloin.gen_connect import GenloginConnection
from source.source_genloin.gen_connect import GenloginAction
from thread.threading_multi import ThreadingMulti



def action():
    group_profile_id:int = 17529
    list_profiles_id = GenloginConnection().get_id_by_group_profile(profile_group_ids=group_profile_id)

    try:


        ThreadingMulti().start_thread(profiles_id=list_profiles_id[:1])

        ThreadingMulti().stop_thread()
    except Exception as e:
        print(e)
        ThreadingMulti().stop_thread()
        [GenloginAction().stop_profile(profiles_id=id) for id in list_profiles_id[:1]]

def run():
    action()
