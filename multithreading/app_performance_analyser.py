"""
Problem statement: Design a system to gather performance metrics from the Android app of an E-commerce App

First: 
  Scoping 
  - Why are we building this? 
    Assuming the use case as the user of this system, they would want to know 
    - When does my app doesn't perform well (breaches SLA backend/page_render_time whichever is the case) 
    - Which app version/platform(device type) the performance is bad
  - Android app only
  - Metrics to gather
    1. App start time
    2. Page Load time
    3. Network Usage
    4. RAM usage
    5. Battery usage
  - Is this native app or react or hybrid with webview?   --> native with webview
  - Why are we building this? 
    Assuming the use case as the user of this system, they would want to know 
    - When does my app doesn't perform well (breaches SLA backend/page_render_time whichever is the case) 
    - Which app version/platform(device type) the performance is bad
    - 
   
  
 Ideas:
  1. Create a SDK to plug in, in the the E-commerce app
    Pros: we can get realtime data on each page(activity) triggered
    Cons: will make the app heavy on network calls if we start sending many data points (5 events as  per the problem and on each page, or which page..)
  2. How about a hybrid approach and Utilise the power of Android command line - ADB 
    - Capture all hardware metrics with it (network/RAM/Battery etc.)
    - And app specific with the sdk approach 
  3. How do we want to make it work in pre-prod? Setup to run with the existing test suites running on cloud (where multiple devices are connected)
  
  """

"""
HLD

HOST (connected with device) -> CAPTURE LOGs -> PARSE LOGs -> Streaming Storage (Kafka) -> ANALTICS -> DASHBOARD with filters [honeycomb styled to get info at as granular level as needed]

Questions: 
  - where should the ADB commands run, 
  - should there be a single consumer which is reading the ADB running logs always and bucketing them matching the log type. 
    Eg. APP_OPENED -> take stamp and put into storage 
    Or should it be separate commonds for each log filtering. 
    Eg. adb logcat | grep "APP_OPENED", adb logcat | grep "PAGE 2 loaded"
    
    Note: we still got to hit some commands at runtime like, track any hardware metrics (should they be on cron basis or just capture one time)
    
  - should capture and parse be single component
  - Multiple devices are connected on the same host where tracking the ADB logs 
  - Basis the decision on above, 
    - Decide to keep the listener always up or only start capturing when some signal is recieved from the automated test started 
    and stop once stop and also keep in mind that there are multiple devices connected to the same host which is reading the logs so what decision has to be made?
"""


### LLD

class ADB:
  def __init__(self):
    self.adb_base_cmd = "adb logcat"
    
  @property
  def network(self):
    ADB_NETWORK_CAPTURE_COMMAND = self.adb_base_cmd + ""
    """
    Some filtering logic on the command
    """
    return ADB_NETWORK_CAPTURE_COMMAND
  
  @property
  def ram(self):
    ADB_RAM_CAPTURE_COMMAND = self.adb_base_cmd + ""
    return ADB_RAM_CAPTURE_COMMAND
  
  @property
  def battery(self):
    ADB_RAM_CAPTURE_COMMAND = self.adb_base_cmd + ""
    return ADB_RAM_CAPTURE_COMMAND
    
    @property
    def app_opened()







 
    
