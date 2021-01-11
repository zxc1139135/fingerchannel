#ifndef DIALOG_H
#define DIALOG_H

#include <QWidget>
#include <QTcpSocket>
#include <QFile>

namespace Ui {
class Dialog;
}

class Dialog : public QWidget
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = 0);
    ~Dialog();

private slots:
   
     void on_pushButton_clicked();

signals:

     void mySignal();
   

private:
     Ui::Dialog *ui;
     QTcpSocket *tcpSocket;
    
};

#endif // Dialog_H
