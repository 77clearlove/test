# -*- coding: UTF-8 -*-
from bluepy import btle

'''
READ
READ WRITE
INDICATE
NOTIFY
WRITE NO RESPONSE WRITE
'''

class Ble:

    def __init__(self, addr, addrType):
        self.addr = addr
        self.addrType = addrType

    def getInfo(self):
        # if properties=='READ', readType and readMsg
        info = {} # {service1:{chara1:[handle, properties, readType, readMsg], chara2}}
        try:
            d = btle.Peripheral(self.addr, self.addrType)
        except:
            return 1
        try:
            for ser in d.getServices():
                dict1 = {}
                for chara in ser.getCharacteristics():
                    list1 = []
                    list1.append(str(chara.getHandle()))
                    list1.append(chara.propertiesToString())
                    if (chara.supportsRead()):
                        list1.append(type(chara.read()))
                        list1.append(chara.read())
                    dict1[str(chara)] = list1
                info[str(ser)] = dict1
        except:
            return 2
        d.disconnect()
        return info

