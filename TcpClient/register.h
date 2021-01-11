#ifndef REGISTER_H
#define REGISTER_H

#include <QWidget>
#include <QTcpSocket>
#include <QFile>

namespace Ui {
class Register;
}

class Register : public QWidget
{
    Q_OBJECT

public:
    explicit Register(QWidget *parent = 0);
    ~Register();

private slots:

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_7_clicked();

    void on_pushButton_9_clicked();
signals:

     void mySignal();



private:
     Ui::Register *ui;



     QTcpSocket *tcpSocket;

     QFile file; //文件对象
     QString fileName; //文件名字
     qint64 fileSize; //文件大小
     qint64 recvSize; //已经接收文件的大小



     qint64 sendSize; //已经发送文件的大小

};
#endif // REGISTER_H
