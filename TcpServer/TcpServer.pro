#-------------------------------------------------
#
# Project created by QtCreator 2018-07-25T10:36:40
#
#-------------------------------------------------

QT       += core gui  network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = TcpServer
TEMPLATE = app


SOURCES += main.cpp\
    request.cpp \
        server.cpp \
    serverfile.cpp

HEADERS  += server.h \
    request.h \
    serverfile.h

FORMS    += server.ui \
    request.ui \
    serverfile.ui \
    test.ui

CONFIG  += C++11

RC_ICONS = favicon.ico

RESOURCES += \
    picture.qrc
