#ifndef CANCEL_H
#define CANCEL_H

#include <QWidget>
#include <QTcpSocket>
#include <QFile>

namespace Ui {
class Cancel;
}

class Cancel : public QWidget
{
    Q_OBJECT

public:
    explicit Cancel(QWidget *parent = 0);
    ~Cancel();

private slots:

    void on_pushButton_clicked();

    void on_pushButton_1_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_6_clicked();


signals:

    void mySignal();



private:
     Ui::Cancel *ui;

     QTcpSocket *tcpSocket;


};
#endif // CANCEL_H
