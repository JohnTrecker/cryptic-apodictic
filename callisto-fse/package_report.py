from django.conf import settings

settings.configure()

from api import FSENotificationAPI

"""
This program uses a sub-set of the callisto-core.notification.api to
encrypt files and save them to the disk.
"""

api = FSENotificationAPI()
inputFile = './test-report.txt'
outputFile = './test-report.txt.asc'

api_status = api.create_encrypted_report(inputFile, outputFile)
exit(api_status)
