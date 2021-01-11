#ifndef CLIENT_H
#define CLIENT_H

#include <QWidget>
#include <QTcpSocket> //通信套接字
#include "clientfile.h"
#include "form.h"
#include "register.h"
#include "cancel.h"

namespace Ui {
class Client;
}

class Client : public QWidget
{
    Q_OBJECT

public:
    explicit Client(QWidget *parent = 0);
    ~Client();

private slots:
    void on_ButtonConnect_clicked();

    void on_ButtonSend_clicked();

    void on_ButtonClose_clicked();

    void dealW2();

    void on_pushButton_clicked();

    void on_pushButton2_clicked();

    void on_pushButton3_clicked();

    void on_pushButton4_clicked();

    void dealW3();

    void dealW4();

    void dealW5();
private:
    Ui::Client *ui;

    ClientFile w2;

    Form w3;

    Register w4;

    Cancel w5;

    QTcpSocket *tcpSocket; //通信套接字
};

#endif // CLIENT_H
