# heartratemon-miband7
Getting real-time heartrate data from a Mi Band 7 in a nice way is impossible without a rooted phone [unless you can get the auth API key](https://gadgetbridge.org/basics/pairing/huami-xiaomi-server/) from xiaomi or whatever auth your Mi Band manufacturer uses somehow.

With this method you install an app that shows your Mi Band 7 heartrate in a permanent notification, and you use [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) along with a plugin to read the real-time heartrate from that notification, to then send it to an HTTP endpoint (the one in `./main.py`).

This project is for the Mi Band 7 but the webapp can be taken and modified to suit any data source, with the [Notify for Mi Band](https://play.google.com/store/apps/details?id=com.mc.miband1) app you can use any Mi Band model that's supported.

# Phone setup
**Apps**
- [Notify for Mi Band](https://play.google.com/store/apps/details?id=com.mc.miband1): _Connects to the Mi Band 7, displays the BPM data in real time a permanent notification_
  - Set continuous heart rate monitoring mode
- [AutoNotification](https://play.google.com/store/apps/details?id=com.joaomgcd.autonotification): _Tasker plugin to read notification data_
  - When adding the AutoNotificationIntercept profile on tasker, the config will be done in this app, make it so it tracks the Notify for Mi Band app
- [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm): _Automation tool used to send the BPM data to the HTTP endpoint_
  1. Create AutoNotificationIntercept profile (You need the AutoNotification plugin listed above)
  2. Add HTTP Request Action to POST on `http://<machine_ip>:8081`
  3. In Body put `%antexts()`

For all apps remember to give the required permissions

# PC setup
1. `cd web && npm ci` - Install node modules
2. `pip install -r requirements.txt` - Install python deps

# Credits
- Web graph modified from [here](https://github.com/Jaapp-/miband-5-heart-rate-monitor)
