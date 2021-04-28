#upload to sharepoint online   
#load libraries needed for sharepoint upload
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

import pandas as pd
#setup access to sharepoint online
authcookie = Office365('https://urlname.sharepoint.com', username='email', password='password').GetCookies()
site = Site('https://urlname.sharepoint.com/sites/', version=Version.v2016, authcookie=authcookie)
folder = site.Folder('Shared Documents/Folder/')

with open('Output.xlsx', mode='rb') as file:
        fileContent = file.read()
folder.upload_file(fileContent, "Output.xlsx")
