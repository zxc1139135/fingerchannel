#ifndef SERVERFILE_H
#define SERVERFILE_H

#include <QWidget>
#include <QTcpServer> //监听套接字
#include <QTcpSocket> //通信套接字
#include <QFile>
#include <QTimer>

namespace Ui {
class ServerFile;
}

class ServerFile : public QWidget
{
    Q_OBJECT

public:
    explicit ServerFile(QWidget *parent = 0);
    ~ServerFile();

    void sendData(); //发送文件数据

private slots:
    void on_ButtonChance_clicked();

    void on_ButtonSend_clicked();

    void on_pushButton_3_clicked();

signals:
    void mySignal();

private:
    Ui::ServerFile *ui;


    QTcpServer *tcpServer; //监听套接字
    QTcpSocket *tcpSocket; //通信套接字

    QFile file; //文件对象
    QString fileName; //文件名字
    qint64 fileSize; //文件大小
    qint64 sendSize; //已经发送文件的大小

    QTimer timer; //定时器

};

#endif // SERVERFILE_H
