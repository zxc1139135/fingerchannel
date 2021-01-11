#include "request.h"
#include "ui_request.h"

#include <QDebug>
#include <QMessageBox>
#include <QHostAddress>

Request::Request(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Request)
{
    ui->setupUi(this);
    tcpSocket = new QTcpSocket(this);
    connect(tcpSocket, &QTcpSocket::readyRead,
            [=]()
            {
                //获取对方发送的内容
                QByteArray array = tcpSocket->readAll();
                //追加到编辑区中
                //ui->textEditRead->append(array);
            }

            );

}



Request::~Request()
{
    delete ui;
}

void Request::on_pushButton_clicked()
{
    emit mySignal();
}



