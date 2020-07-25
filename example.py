import dbest, time

last_state = None

class MyStatusChangedListener(dbest.StatusChangedListener):
    def onStateChanged(self, state):
        global last_state
        last_state = state
        print("onStateChanged %s" % state)


dbest_instance = dbest.Dbest()
dbest_instance.connect()

my_status_changed_listener = MyStatusChangedListener(dbest_instance)
my_status_changed_listener.subscribe()
time.sleep(10)
my_status_changed_listener.unsubscribe()

print("WAITING")

state = str((int(last_state) + 3))
if len(state) == 0:
    state = "0" + state

dbest_instance.wait_for_state(state) # Blocking
print("FINISH")

dbest_instance.disconnect()
