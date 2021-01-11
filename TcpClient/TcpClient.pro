#-------------------------------------------------
#
# Project created by QtCreator 2018-07-25T10:45:12
#
#-------------------------------------------------

QT       += core gui  network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = TcpClient
TEMPLATE = app


SOURCES += main.cpp\
    cancel.cpp \
        client.cpp \
    clientfile.cpp \
    form.cpp \
    register.cpp

HEADERS  += client.h \
    cancel.h \
    clientfile.h \
    form.h \
    register.h

FORMS    += client.ui \
    cancel.ui \
    clientfile.ui \
    form.ui \
    register.ui

CONFIG += C++11
CONFIG += resources_big

RC_ICONS = favicon.ico

RESOURCES += \
    picture.qrc
