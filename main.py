import sonarrApiInfo

#sonarr_api_key = YOUR SONARR API KEY GOES HERE
#sonarr_address = YOUR SONARR SERVER'S local address:8989/api

neweps = sonarrApiInfo.sonarrInfo(sonarr_address, sonarr_api_key)

neweps.upcomingep()
print('\n\n\n')
neweps.completedep()
print('\n\n\n')
neweps.currentdownloads()
