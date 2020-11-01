import smbus
import time
import Settings
from PyQt5 import QtGui

i2c_cmd = 0x5E


def init():

    global LINKED
    LINKED = True

    global IR_stat
    IR_stat = False

    global IR_imaging
    IR_imaging = False

    global imaging
    imaging = False

    global busy
    busy = False

    global log_sensor
    log_sensor = False

    global sensor_flag
    sensor_flag = False

    global log_duration
    log_duration = 1

    global frame_RPM
    frame_RPM = 0.3

    global core_RPM
    core_RPM = 0.3

    global frame_enabled
    frame_enabled = True

    global core_enabled
    core_enabled = True

    global frame_microstep
    frame_microstep = 256

    global core_microstep
    core_microstep = 256

    global frame_interval
    frame_interval = 1126

    global core_interval
    core_interval = 1126

    global acc_attached
    acc_attached = False

    global temp_attached
    temp_attached = False

    global tag_index
    tag_index = 0

    global ACC_X_text
    ACC_X_text = "offline"
    global ACC_Y_text
    ACC_Y_text = "offline"
    global ACC_Z_text
    ACC_Z_text = "offline"

    global TEMP_text
    TEMP_text = "offline"
    global HUD_text
    HUD_text = "offline"

    global PR_text
    PR_text = "offline"

    global sequence_name
    sequence_name = ""

    global current_image
    current_image = ""

    global default_dir
    default_dir = "/home/pi/Desktop"

    global full_dir
    full_dir = ""

    global date
    date = time.strftime('%m_%d_%Y')

    global prelog_dir
    prelog_dir = "/home/pi/Desktop/sensor_log/"

    global log_dir
    log_dir = "/home/pi/Desktop/sensor_log/" + date

    global AOI_X
    AOI_X = 0
    global AOI_Y
    AOI_Y = 0
    global AOI_W
    AOI_W = 1
    global AOI_H
    AOI_H = 1

    global interval
    interval = 2

    global duration
    duration = 2

    global total
    total = 1

    global current
    current = 0

    global rotation
    rotation = 0

    global frame_dir
    frame_dir = False

    global core_dir
    core_dir = False

    global x_resolution
    x_resolution = 2464

    global y_resolution
    y_resolution = 2464

    global imaging_mode
    imaging_mode = 1

    global trasmitted
    trasmitted = 0

    global commands_list
    commands_list = []

    global timelapse_running
    timelapse_running = False

    global cycle_running
    cycle_running = False

    global cycle_time
    cycle_time = 60

    global time_elipsed
    time_elipsed = 0

    global log_start_time
    log_start_time = 0

    global sample_time
    sample_time = 0

    global forward
    forward = QtGui.QIcon()
    forward.addPixmap(QtGui.QPixmap("../_image/forward.png"),
                      QtGui.QIcon.Normal, QtGui.QIcon.Off)

    global reverse
    reverse = QtGui.QIcon()
    reverse.addPixmap(QtGui.QPixmap("../_image/Reverse.png"),
                      QtGui.QIcon.Normal, QtGui.QIcon.Off)

    global linked
    linked = QtGui.QIcon()
    linked.addPixmap(QtGui.QPixmap("../_image/Link.png"),
                     QtGui.QIcon.Normal, QtGui.QIcon.Off)

    global broken
    broken = QtGui.QIcon()
    broken.addPixmap(QtGui.QPixmap("../_image/Broken_Link.png"),
                     QtGui.QIcon.Normal, QtGui.QIcon.Off)

    global speed_dict
    speed_dict = {
        10: 825,
        15: 549,
        20: 394,
        25: 310,
        30: 254,
        35: 214,
        40: 189,
        45: 162,
        50: 146,

        55: 278,
        60: 260,
        65: 231,
        70: 214,
        75: 198,
        80: 182,
        85: 171,
        90: 162,

        95: 329,
        100: 310,
        105: 295,
        110: 278,
        115: 262,
        120: 255,
        125: 246,
        130: 230,
        135: 225,
        140: 214,
        145: 209,
        150: 198,
        155: 194,
        160: 182,
        165: 178,
        170: 172,

        175: 361,
        180: 346,
        185: 336,
        190: 330,
        195: 316,
        200: 310,
        205: 298,
        210: 294,
        215: 284,
        220: 278,
        225: 274,

        230: 557,
        235: 545,
        240: 530,
        245: 518,
        250: 510,
        255: 497,
        260: 490,
        265: 478,
        270: 468,
        275: 462,
        280: 450,
        285: 445,
        290: 434,
        295: 428,
        300: 418,
        305: 410,
        310: 408,
        315: 397,
        320: 394,
        325: 385,
        330: 378,
        335: 376,
        340: 366,
        345: 362,
        350: 361,
        355: 349,
        360: 346,
        365: 342,
        370: 334,
        375: 330,
        380: 329,
        385: 325,
        390: 318,

        395: 650,
        400: 642,
        405: 634,
        410: 626,
        415: 618,
        420: 610,
        425: 601,
        430: 598,
        435: 590,
        440: 582,
        445: 578,
        450: 566,
        455: 562,
        460: 553,
        465: 550,
        470: 542,
        475: 534,
        480: 530,
        485: 526,
        490: 518,
        495: 514,
        500: 510,


    }


def sendCMD(cont):
    print("sending command...\n" + cont)
    temp = cont + "\n"
    try:
        if Settings.busy:
            time.sleep(0.02)

        Settings.busy = True
        bus = smbus.SMBus(1)
        converted = []
        for b in temp:
            converted.append(ord(b))
        bus.write_i2c_block_data(0x08, i2c_cmd, converted)
        time.sleep(0.02)
        Settings.busy = False
    except Exception as e:
        print(e, "command send failure,contact Jerry for support")
