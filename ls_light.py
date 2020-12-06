from bluepy import btle
import time


def getInfo(addr, addrType):
    # if properties=='READ', readType and readMsg
    info = {}  # {service1:{chara1:[handle, properties, readType, readMsg], chara2}}
    try:
        d = btle.Peripheral(addr, addrType)
    except:
        print 'connect failed......'
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
        print 'connect ended......'
        return 2
    d.disconnect()
    return info

'''
08005a16ec17b60f0000
0800cf2101268c170000
08008929ea2e7a1d0000
0800062d1534c5200000
0800d32e3c37e8220000
08000330dc38d1240000
0800c430d239cc260000
08009432363b82270000
08004733053c85280000
0800c733903cb2280000
0800ae32303c4a280000
0800f230473b3d290000
08001830b83a3d2a0000
0800822e093afd2a0000
0800d02f433a992e0000
0800df2f6a3a7d310000
08002b30dd3a80320000
0800532fb73a46330000
0800552d173aa8320000
0800a02cba396c330000
0800b42c663aaf330000
080083347241cb330000
08003e59dd5823380000
08004c83aa6d67390000
0800d782655f80270000
080005461a248f220000
080047014701c15e0000
080047014701e86c0000
08007a4b590594490000
0800c7cae958412f0000
0800fffffba0c1270000
\x08\x00\xff\xff\xfb\xa0\xc1\x27\x00\x00
\x08\x00\xcf\x21\x01\x26\x8c\x17\x00\x00

close: \x08\x00\x00\x00\x00\x00\x00\x00\x00\x00

'''

if __name__ == '__main__':
    addr = 'f0:45:da:f4:41:37'
    addrType = 'public'
    d = btle.Peripheral(addr, addrType)
    # print d.writeCharacteristic(25, '\x08\x00\xff\xff\xfb\xa0\xc1\x27\x00\x00', withResponse=True)
    code = "\x00\x00\x00\x00\x00\x00"
    print d.writeCharacteristic(25, '\x08\x00' + code + '\x00\x00')
    print d.writeCharacteristic(18, '\x08\x00' + code + '\x00\x00')