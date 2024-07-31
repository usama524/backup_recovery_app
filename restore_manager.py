import gzip
import os
import shutil
import tarfile
from cryptography.fernet import Fernet # type: ignore

class RestoreThread(QThread):
    progress = pyqtSignal(str)
    
    def __init__(self, filename, destination, encryption_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.destination = destination
        self.encryption_key = encryption_key

    def run(self):
        self.progress.emit("Restore started...")
        
        # Decrypt the backup
        if self.encryption_key:
            cipher = Fernet(self.encryption_key)
            with open(self.filename, 'rb') as f_in:
                encrypted_data = f_in.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            with open("temp.tar.gz", 'wb') as f_out:
                f_out.write(decrypted_data)
        else:
            shutil.copy(self.filename, "temp.tar.gz")
        
        # Decompress the backup
        with gzip.open("temp.tar.gz", 'rb') as f_in:
            with open("temp.tar", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        os.remove("temp.tar.gz")
        
        # Extract the tar file
        with tarfile.open("temp.tar", "r") as tar:
            tar.extractall(path=self.destination)
        
        os.remove("temp.tar")
        self.progress.emit("Restore completed.")
