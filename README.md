# media_api_requests
Interact with Sonarr Api calls

This program pulls JSON data from Sonarr's api and converts certain peices of information, 
like Series title and Episode title into a more readable format.

<h2>How To Use This Program</h2>


Clone the repository to your local machine.

Open up main.py. You will put your Sonarr apikey and sonarr's  local address in the designated fields. 

These variables will be passed to the class call which creates a class instance. This instance will have access to the methods that calls specific api endpoints: 

Calendar - grabs the series title and episode title of shows that will air that night and tomorrow night 
History - which will give us the series title and episode title of recently completed downloads 
Queue - which will give us the data on currently downloading episodes. 
