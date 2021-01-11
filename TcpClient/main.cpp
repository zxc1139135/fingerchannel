#include "client.h"
#include <QApplication>
#include <qtextcodec.h>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Client w;
    w.show();
    return a.exec();


}
