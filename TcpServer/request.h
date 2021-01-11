#ifndef REQUEST_H
#define REQUEST_H

#include <QWidget>
#include <QTcpSocket>
#include <QFile>


namespace Ui {
class Request;
}

class Request : public QWidget
{
    Q_OBJECT

public:
    explicit Request(QWidget *parent = 0);
    ~Request();

private slots:

    void on_pushButton_clicked();


signals:

     void mySignal();



private:
     Ui::Request *ui;
     QTcpSocket *tcpSocket;


};

#endif // REQUEST_H
