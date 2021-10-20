import asyncio
import sys
import glob
import serial
import modules.receiveProcessing as receiveProcessing

ser = None
WR_TOUT = 0.1
RD_TOUT = 0.1

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def connect(_port, speed, pairity, data_bits, stop_bits):
    parity_dict = {"NONE": serial.PARITY_NONE,
                   "ODD": serial.PARITY_ODD,
                   "EVEN": serial.PARITY_EVEN,
                   "MARK": serial.PARITY_MARK,
                   "SPACE": serial.PARITY_SPACE}

    stop_bits_list = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]

    '''
        bytesyze_list = {5: serial.FIVEBITS,
                         6: serial.SIXBITS,
                         7: serial.SEVENBITS,
                         8: serial.EIGHTBITS}
    '''

    global ser
    ser = serial.Serial(port=_port, baudrate=int(speed), timeout=0,
                        parity=parity_dict[pairity],
                        stopbits=stop_bits_list[int(stop_bits)]
                        )
    try:
        ser.open()
    except serial.SerialException:
        print("error while openning serial")


def isConnected():
    return ser.is_open


async def write(msg):
    ser.write(msg)


async def writeSerial(msg, form):
    if ser is not None:
        try:
            await asyncio.wait_for(write(msg), WR_TOUT)
        except asyncio.TimeoutError:
            print("Send TimeOut")
            readAs([00, 00, 00, 00], form)
        except:
            print("Send err")
            readAs([00, 00, 00, 00], form)

        await readSerial(form)
    else:
        print("serial is not opened")


async def read():
    data = ser.readall()
    return data


async def readSerial(form):
    if ser is not None:
        try:
            data = await asyncio.wait_for(read(), RD_TOUT)
            readAs(data, form)
        except asyncio.TimeoutError:
            print("readTimeout")
            readAs([00, 00, 00, 00], form)
        except:
            print("read err")
            readAs([00, 00, 00, 00], form)
    else:
        print("serial is not opened")


def readAs(dataBytes, form):
    ctext = form.decodeAsComboBox.currentText()
    if ctext == 'dateTime':
         text = receiveProcessing.getDateTime(dataBytes)
    elif ctext == 'Ascii':
         text = receiveProcessing.getAscii(dataBytes)
    elif ctext == 'hex':
         text = receiveProcessing.getHex(dataBytes)
    else:
        text = receiveProcessing.getHex(dataBytes)
    form.listWidget.addItem(text)
