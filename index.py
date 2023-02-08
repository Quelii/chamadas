import time

def schedule_call(phone_number, call_time):
    call_time_seconds = time.mktime(time.strptime(call_time, "%Y-%m-%d %H:%M:%S"))
    time_remaining = call_time_seconds - time.time()
    if time_remaining > 0:
        time.sleep(time_remaining)
        # aqui você pode fazer a chamada telefônica
        print("Making call to " + phone_number)
    else:
        print("Call time has already passed")

schedule_call("71986149005", "2023-02-07 03:33:00")
