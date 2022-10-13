run = True
while run:
    import speedtest
    import time
    from datetime import datetime

    test = speedtest.Speedtest()
    ## INITIALIZE TEST
    print(f"Please give some times as the test needs some time to get the result ", end='')
    for i in range(25):
        print(' . ', end="")
        time.sleep(0.2)

    # INITIALIZE UPLOAD SPEED, DOWNLOAD SPEED AND PING
    upload_speed = test.upload()
    download_speed = test.download()
    ping = test.best
    # GET THE VALUES  kbps in
    if float(download_speed) < 1024:
        download_float = float(download_speed) / 1024
        upload_float = float(upload_speed) / 1024 ** 2
        upload_float = (f"{upload_float: .4f}")
        download_float = (f"{download_float: .4f}")
        download_speed_modified = str(download_float) + 'kbps'
        upload_speed_modified = str(upload_float) + 'mbps'
    else:
        download_float = float(download_speed) / 1024 ** 2
        upload_float = float(upload_speed) / 1024 ** 2
        download_float = (f"{download_float: .4f}ad")
        upload_float = (f"{upload_float: .4f}")
        download_speed_modified = str(download_float) + 'mbps'
        upload_speed_modified = str(upload_float) + 'mbps'
    url = ping['url']
    lat = ping['lat']
    lon = ping['lon']
    name = ping['name']
    country = ping['country']
    sponsor = ping['sponsor']
    host = ping['host']
    latency = ping['latency']
    ## print time:
    now = datetime.now()
    print("\n")
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print("\n")
    ## print everything now

    # print(f"{z:.4f}")
    print(f"Download speed: {download_speed_modified}")
    print(f"Upload speed: {upload_speed_modified}")
    print(f"Latitude : {lat}")
    print(f"Longitude: {lon}")
    print(f"Country: {country}")
    print(f"Name: {name}")
    print(f"URL: {url}")
    print(f"Sponsor: {sponsor}")
    print(f"Host: {host}")
    print(f"Latency: {latency}")
    print("\n")
    check = input("Do you want to test again ?(y/n): ")
    if check.lower()[0] == 'y':
        run =True
    else:
        run = False