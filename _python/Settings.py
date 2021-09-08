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

    global on_time
    on_time = 60

    global off_time
    off_time = 60

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
        10: 1152,
        15: 741,
        20: 554,
        25: 430,
        30: 362,
        35: 309,
        40: 262,
        45: 230,
        50: 208,

        55: 394,
        60: 361,
        65: 330,
        70: 306,
        75: 278,
        80: 262,
        85: 246,
        90: 230,
        95: 214,
        100: 203,

        105: 410,
        110: 393,
        115: 377,
        120: 362,
        125: 342,
        130: 328,
        135: 313,
        140: 302,
        145: 294,
        150: 282,
        155: 271,
        160: 262,
        165: 252,
        170: 246,
        175: 238,
        180: 230,
        185: 226,
        190: 213,
        195: 210,
        200: 202,

        205: 426,
        210: 410,
        215: 402,
        220: 394,
        225: 378,
        230: 377,
        235: 361,
        240: 360,
        245: 350,
        250: 346,

        255: 694,
        260: 682,
        265: 666,
        270: 656,
        275: 642,
        280: 630,
        285: 618,
        290: 610,
        295: 596,
        300: 584,
        305: 578,
        310: 566,
        315: 558,
        320: 546,
        325: 542,
        330: 530,
        335: 525,
        340: 514,
        345: 510,
        350: 498,

        355: 1013,
        360: 990,
        365: 981,
        370: 966,
        375: 958,
        380: 942,
        385: 930,
        390: 914,
        395: 906,
        400: 894,
        405: 882,
        410: 866,
        415: 861,
        420: 850,
        425: 838,
        430: 829,
        435: 814,
        440: 810,
        445: 798,
        450: 790,
        455: 782,
        460: 773,
        465: 762,
        470: 755,
        475: 746,
        480: 742,
        485: 734,
        490: 726,
        495: 714,
        500: 710,

        505: 1430,
        510: 1413,
        515: 1398,
        520: 1389,
        525: 1373,
        530: 1360,
        535: 1345,
        540: 1333,
        545: 1319,
        550: 1310,
        555: 1298,
        560: 1282,
        565: 1274,
        570: 1262,
        575: 1249,
        580: 1241,
        585: 1230,
        590: 1217,
        595: 1209,
        600: 1197,
        605: 1185,
        610: 1178,
        615: 1161,
        620: 1158,
        625: 1146,
        630: 1141,
        635: 1130,
        640: 1121,
        645: 1113,
        650: 1105,
        655: 1094,
        660: 1083,
        665: 1078,
        670: 1067,
        675: 1062,
        680: 1050,
        685: 1046,
        690: 1042,
        695: 1030,
        700: 1026,

        705: 2096,
        710: 2042,
        715: 2026,
        720: 2010,
        725: 1997,
        730: 1982,
        735: 1973,
        740: 1958,
        745: 1942,
        750: 1930,
        755: 1914,
        760: 1906,
        765: 1893,
        770: 1878,
        775: 1866,
        780: 1857,
        785: 1842,
        790: 1830,
        795: 1820,
        800: 1810,
        805: 1796,
        810: 1784,
        815: 1774,
        820: 1762,
        825: 1750,
        830: 1742,
        835: 1730,
        840: 1721,
        845: 1710,
        850: 1698,
        855: 1690,
        860: 1678,
        865: 1669,
        870: 1662,
        875: 1650,
        880: 1642,
        885: 1630,
        890: 1625,
        895: 1614,
        900: 1605,
        905: 1594,
        910: 1586,
        915: 1578,
        920: 1566,
        925: 1562,
        930: 1550,
        935: 1542,
        940: 1534,
        945: 1526,
        950: 1518,
        955: 1514,
        960: 1502,
        965: 1494,
        970: 1486,
        975: 1478,
        980: 1474,
        985: 1462,
        990: 1458,
        995: 1446,
        1000: 1442


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
