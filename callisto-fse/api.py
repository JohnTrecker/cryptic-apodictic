from callisto_core.notification.api import CallistoCoreNotificationApi as CallistoAPI
import gnupg
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

    def encrypt_file(self, file_data, public_key):
        gpg = gnupg.GPG()
        data = 'this is only a test'
        imported_keys = gpg.import_keys(public_key)
        return gpg.encrypt(
            data,
            imported_keys.fingerprints[0],
            armor=True,
            always_trust=True,
        ).data

    def create_encrypted_report(self, inputFile, outputFile):
        publicKey = self.getPublicKey()
        inputData = self.getReport(inputFile)
        encryptedData = self.encrypt_file(inputData, publicKey)
        print ('[api.py] encryptedData', str(encryptedData))
        self.writeOutputFile(encryptedData, outputFile)
