'''
Created on 04.06.2015

@author: jrenken
'''
from PyQt4.Qt import QObject
from PyQt4.QtCore import QTimer, pyqtSlot, pyqtSignal



class DataDevice(QObject):
    '''
    Baseclass for all data devices
    '''

    readyRead = pyqtSignal()
    deviceConnected = pyqtSignal()
    deviceDisconnected = pyqtSignal()

    def __init__(self, params = {}, parent = None):
        '''
        Constructor
        '''
        super(DataDevice, self).__init__(parent)
        self.timer = QTimer()
        self.buffered = False
        
    def readData(self):
        pass
    
    def connectDevice(self):
        pass
    
    def disconnectDevice(self):
        pass
    
    @pyqtSlot()
    def onReconnectTimer(self):
        self.connectDevice()
        
        
