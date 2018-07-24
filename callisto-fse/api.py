from callisto_core.notification.api import CallistoCoreNotificationApi as CallistoAPI
"""
This is a program that uses the callisto notification API to package an
encrypted GPG file and saves it to the disk for testing encryption in a
development enviorment. This setup would never be used in production, but
is very useful to maintain for debugging locally.
"""


class FSENotificationAPI(CallistoAPI):
    publicKeyPath = './callisto_key.pub'

    def writeOutputFile(self, encryptedData, outputFile):
        with open(outputFile, 'w') as output:
            return output.write(str(encryptedData))

    def getPublicKey(self):
        with open(self.publicKeyPath, 'r') as keyFile:
            return keyFile.read()

    def getReport(self, inputFile):
        with open(inputFile, 'r') as report:
            return report.read()

    def create_encrypted_report(self, inputFile, outputFile):
        publicKey = self.getPublicKey()
        inputData = self.getReport(inputFile)
        encryptedData = self._encrypt_file(inputData, publicKey)
        self.writeOutputFile(encryptedData, outputFile)
