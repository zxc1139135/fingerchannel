#ifndef SERVER_H
#define SERVER_H

#include <QWidget>
#include <QTcpServer> //监听套接字
#include <QTcpSocket> //通信套接字

#include "serverfile.h"
#include "request.h"

namespace Ui {
class Server;
}

class Server : public QWidget
{
    Q_OBJECT

public:
    explicit Server(QWidget *parent = 0);
    ~Server();

private slots:
    void on_ButtonSend_clicked();

    void on_ButtonClose_clicked();

    void on_ButtonFile_clicked();

    void dealW2();

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();



    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();


private:
    Ui::Server *ui;
    ServerFile w2;
    Request w3;

    QTcpServer *tcpServer; //监听套接字
    QTcpSocket *tcpSocket; //通信套接字
    QFile file; //文件对象
    QString fileName; //文件名字
    qint64 fileSize; //文件大小
    qint64 sendSize; //已经发送文件的大小
};

#endif // SERVER_H
