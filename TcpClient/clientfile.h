#ifndef CLIENTFILE_H
#define CLIENTFILE_H

#include <QWidget>
#include <QTcpSocket>
#include <QFile>

namespace Ui {
class ClientFile;
}

class ClientFile : public QWidget
{
    Q_OBJECT

public:
    explicit ClientFile(QWidget *parent = 0);
    ~ClientFile();

private slots:
    void on_ButtonConnect_clicked();

    void on_pushButton_2_clicked();
    void on_pushButton_clicked();

signals:
    void mySignal();


private:
    Ui::ClientFile *ui;

    QTcpSocket *tcpSocket;

    QFile file; //文件对象
    QString fileName; //文件名字
    qint64 fileSize; //文件大小
    qint64 recvSize; //已经接收文件的大小



    qint64 sendSize; //已经发送文件的大小


    bool isStart;   //标志位，是否为头部信息
};

#endif // CLIENTFILE_H
