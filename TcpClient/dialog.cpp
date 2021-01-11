#include "dialog.h"
#include "ui_dialog.h"

#include <QDebug>
#include <QMessageBox>
#include <QHostAddress>

Dialog::Dialog(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);

    tcpSocket = new QTcpSocket(this);

}



Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_pushButton_clicked()
{
    emit mySignal();
}

