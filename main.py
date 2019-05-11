import sonarrApiInfo

#sonarr_api_key = YOUR SONARR API KEY GOES HERE
#sonarr_address = YOUR SONARR SERVER'S local address:8989/api

sonarr_api_key = "b6ce3dd706b94cf9bd35998c0c284e6d"
sonarr_address = 'http://192.168.1.2:8989/api/'

neweps = sonarrApiInfo.sonarrInfo(sonarr_address, sonarr_api_key)

neweps.upcomingep()
print('\n\n\n')
neweps.completedep()
print('\n\n\n')
neweps.currentdownloads()