import os
import sys
import usb.core
import usb.util

def device_handler(r,g,b):
    dev = usb.core.find(idVendor=0x1038, idProduct=0x1500)
    if dev is None:
        raise ValueError('Device not found.')
        # if dev.is_kernel_driver_active(0) is True:

        #     dev.detach_kernel_driver(0)
    dev.set_configuration()

    R = int(r)
    G = int(g)
    B = int(b)

    if R < 0 or R > 255 or G < 0 or G > 255 or B < 0 or B > 255:
        raise ValueError('R G B values need to be between 0 and 255.')

    dev.ctrl_transfer(0x21,0x09,0x200,0,[0x07,0x00,R,G,B])


# device_handler(250,0,0)
