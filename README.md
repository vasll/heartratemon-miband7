# web-heartrate-monitor
I did not find an easy way to get the heart rate data from a Mi Band 7, without a rooted phone you can't get the API key from xiaomi so I had to improvise.

This project is mainly for the Mi Band 7 but the webapp can be taken and modified to suit any data source.

# Phone setup
**Apps**
- Notify for Mi Band: _Connects to the Mi Band 7, displays the BPM data in real time a permanent notification_
  - Set continuous heart rate monitoring mode
- Tasker: _Automation tool to send the BPM data to an HTTP endpiont_
  1. Create AutoNotificationIntercept profile
  2. Add HTTP Request Action to POST on `http://<machine_ip>:8081`
  3. In Body put `%antexts()`
- AutoNotification: _Tasker plugin to read notification data_
  - Give required permissions
  - When adding the AutoNotificationIntercept profile on tasker, the config will be done in this app, make it so it tracks the Notify for Mi Band app

# PC setup
1. `cd web && npm ci`
2. `pip install -r requirements.txt`

# Credits
- web graph modified from [here](https://github.com/Jaapp-/miband-5-heart-rate-monitor)
