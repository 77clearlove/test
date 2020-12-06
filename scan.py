# -*- coding: UTF-8 -*-
from bluepy.btle import Scanner, DefaultDelegate
import btle_m


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr


if __name__ == '__main__':
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan()
    for dev in devices:
        print '**************************************************************************'
        print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        if "f0:45" not in dev.addr:
            continue
        for (adtype, desc, value) in dev.getScanData():
            print "  %s = %s" % (desc, value)
        services = ''
        b = btle_m.Ble(dev.addr, dev.addrType)
        info = b.getInfo()
        if info == 1 or info == 2:
            print 'the host is down...'
        else:
            for k, v in info.items():
                print '*************************************************************************************************'
                print '>>>>', k
                if v:
                    for ch, detail in v.items():
                        print '>>>>>>>>>>>', ch
                        print '>>>>>>>>>>>>', detail