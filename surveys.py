'''
A Python script creating copies of Software Carpentry surveys from a Google Form template
Created on 26 Mar 2015

@author: aleksandra
'''

from apiclient.discovery import build
from apiclient import errors
from oauth2client.client import OAuth2WebServerFlow


#Provide credentials (TO DO)
#CLIENT_ID = 'YOUR_CLIENT_ID'
#CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

ORIGIN_SURVEY = "https://docs.google.com/forms/d/1-bVa0VzMtCB5zpozsjcwTvltkmTcwQ0IYvorl8OiPDo/edit"
SURVEY_COPY_NAME = "test_ignore_"

def copy_file(service, origin_file_id, copy_title):
  """Copy an existing file.

  Args:
    service: Drive API service instance.
    origin_file_id: ID of the origin file to copy.
    copy_title: Title of the copy.

  Returns:
    The copied file if successful, None otherwise.
  """
   copied_file = {'title': copy_title}
   try:
    return service.files().copy(fileId=origin_file_id, body=copied_file).execute()
   except errors.HttpError, error:
     print 'An error occurred: %s' % error
   return None


#Whether you are using simple or authorized API access, you use the build() function to create a service object. 
#It takes an API name and API version as arguments. 
#You can see the list of all API versions on the Supported APIs page. 
#The service object is constructed with methods specific to the given API. 

myService = build("drive","v2")

COPY_URL = copy_file(myService, ORIGIN_SURVEY, SURVEY_COPY_NAME)



#if __name__ == '__main__':
#    pass
