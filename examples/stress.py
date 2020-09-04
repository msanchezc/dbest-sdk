import dbest_sdk, time


dbest_instance = dbest_sdk.Dbest(ip="localhost:50051")
dbest_instance.connect()

sleep_seconds = 5
cont = 0
res = dbest_instance._simple_request("02") # dbest_instance.unlock()
print(res)

while True:
    print("iteración %s" % cont)

    res = dbest_instance._simple_request("03") # dbest_instance.prepare_to_descent()
    print(res)

    res = dbest_instance._simple_request("04") # dbest_instance.prepare_to_land()
    print(res)

    res = dbest_instance._simple_request("05") # dbest_instance.take_drone_in()
    print(res)

    if cont % 2 == 0:
        res = dbest_instance._simple_request("06") #dbest_instance.exchange_battery(1)
    else:
        res = dbest_instance._simple_request("07") #dbest_instance.exchange_battery(2)
    
    print(res)

    cont = cont + 1

    res = dbest_instance._simple_request("08") #dbest_instance.take_drone_out()
    print(res)

    res = dbest_instance._simple_request("09") #dbest_instance.retract_top_platform()
    print(res)

    time.sleep(sleep_seconds)

dbest_instance.disconnect()
