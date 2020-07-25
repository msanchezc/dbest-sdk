import dbest_sdk, time

last_state = None


class MyStatusChangedListener(dbest_sdk.StatusChangedListener):
    def onStateChanged(self, state):
        global last_state
        last_state = state
        print("onStateChanged with state %s" % state)


dbest_instance = dbest_sdk.Dbest(ip="localhost:50051")
dbest_instance.connect()

my_status_changed_listener = MyStatusChangedListener(dbest_instance)
my_status_changed_listener.subscribe()
time.sleep(10)
my_status_changed_listener.unsubscribe()

print("WAITING FOR STATE")

state = str((int(last_state) + 3))
if int(state) <= 9:
    state = "0" + state

dbest_instance.wait_for_state(state)  # Blocking
print("FINISH WAITING FOR STATE")

res = dbest_instance._simple_request("1")
print("SIMPLE REQUEST, ANSWER %s" % res)
res = dbest_instance._simple_request("2")
print("SIMPLE REQUEST, ANSWER %s" % res)

dbest_instance.disconnect()
