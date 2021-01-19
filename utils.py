from PyQt5 import QtCore

def degrees_to_cardinal(d):
    '''
    note: this is highly approximate...
    '''
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    #dirs = ["Пн", "ПнПнСх", "ПнСх", "СхПнСх", "Сх", "СхПдСх", "ПдСх", "ПдПдСх",
    #        "Пд", "ПдПдЗх", "ПдЗх", "ЗхПдЗх", "Зх", "ЗхПнЗх", "ПнЗх", "ПнПнЗх"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]

def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))
