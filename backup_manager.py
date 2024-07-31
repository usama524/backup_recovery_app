import os
import tarfile
import gzip
import shutil
from cryptography.fernet import Fernet
from PyQt5.QtCore import QThread, pyqtSignal

class BackupThread(QThread):
    progress = pyqtSignal(str)
    
    def __init__(self, filename, source, destination, compression, encryption_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.source = source
        self.destination = destination
        self.compression = compression
        self.encryption_key = encryption_key

    def run(self):
        self.progress.emit("Backup started...")
        
        # Compress the backup
        tar_file = f"{self.filename}.tar"
        with tarfile.open(tar_file, "w") as tar:
            tar.add(self.source)
        
        if self.compression == "gzip":
            with open(tar_file, 'rb') as f_in:
                with gzip.open(f"{tar_file}.gz", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(tar_file)
            tar_file += ".gz"
        
        # Encrypt the backup
        if self.encryption_key:
            cipher = Fernet(self.encryption_key)
            with open(tar_file, 'rb') as f_in:
                encrypted_data = cipher.encrypt(f_in.read())
            with open(f"{tar_file}.enc", 'wb') as f_out:
                f_out.write(encrypted_data)
            os.remove(tar_file)

        # Move the file to destination
        shutil.move(f"{tar_file}.enc", os.path.join(self.destination, f"{self.filename}.enc"))
        
        self.progress.emit("Backup completed.")
