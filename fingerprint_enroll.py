import time,os
from pyfingerprint import PyFingerprint
import sqlite3
class FingerPrintScan:
    
    def __init__(self):        
        self.f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if ( self.f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')
        print('Currently used templates: ' + str(self.f.getTemplateCount()) +'/'+ str(self.f.getStorageCapacity()))
        self.current_buffer = 0x01
    
    def scan_fingerprint(self):
        while ( self.f.readImage() == False ):
            pass
    
    def is_fingerprint_exist(self):
        result = self.f.searchTemplate()
        positionNumber = result[0]
        print(positionNumber)
        return positionNumber >= 0
    
    def get_template_id(self):
        result = self.f.searchTemplate()
        positionNumber = result[0]
        print(positionNumber)
        return positionNumber
    
    def save_fingerprint(self):
        self.f.createTemplate()
        return self.f.storeTemplate()
    
    def clear_all_fingerprint(self):
        for i in range(self.f.getTemplateCount()):
            if self.f.deleteTemplate(i):
                print('Template deleted - '+str(i))
    
    def clear_fingerprint(self,start,end):
        for i in range(start,end):
            if self.f.deleteTemplate(i):
                print('Template deleted - '+str(i))

    def save_to_char_buffer(self):
        self.f.convertImage(self.current_buffer)
        self.current_buffer = self.current_buffer + 1
    
    def save_as_image(self,file_name):
        imageDestination =  os.getcwd()+'/'+file_name+'.png'
        self.f.downloadImage(imageDestination)                
        
if __name__ == "__main__":
    try:
        finger_print_module = FingerPrintScan()
        finger_print_module.scan_fingerprint()
        finger_print_module.save_as_image('Linkon')
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))