#include "clientfile.h"
#include "ui_clientfile.h"

#include <QDebug>
#include <QMessageBox>
#include <QHostAddress>
#include <QFileDialog>
#include <QFileInfo>

ClientFile::ClientFile(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ClientFile)
{
    ui->setupUi(this);

    tcpSocket = new QTcpSocket(this);

    isStart = true;

    ui->progressBar->setValue(0); //当前值

    setWindowTitle("客户端");

    connect(tcpSocket, &QTcpSocket::connected,
    [=]()
    {
        //提示连接成功
        ui->textEdit->clear();
        ui->textEdit->append("准备就绪，等待服务器传送文件……");
    }
    );

    connect(tcpSocket, &QTcpSocket::readyRead,
    [=]()
    {
        //取出接收的内容
        QByteArray buf = tcpSocket->readAll();

        if(true == isStart)
        {
            isStart = false;
            fileName = QString(buf).section("##",0,0);
            fileSize = QString(buf).section("##",1,1).toInt();
            recvSize = 0;
            file.setFileName(fileName);
            bool isOk = file.open(QIODevice::WriteOnly);
            if(false == isOk)
            {
                qDebug()<<"WriteOnly error 49";
                tcpSocket->disconnectFromHost();
                tcpSocket->close();
                return;
            }
            QString str = QString("接收的文件: [%1: %2kb]").arg(fileName).arg(fileSize/1024);
            //QMessageBox::information(this, "文件信息", str);
            ui->textEdit->setText(str);
            ui->progressBar->setMinimum(0); //最小值
            ui->progressBar->setMaximum(fileSize/1024); //最大值
            ui->progressBar->setValue(0); //当前值
        }
        else {
            qDebug()<<"123456";
            qint64 len = file.write(buf);
            if(len > 0)
            {
                recvSize += len; //累计接收大小
                qDebug() << len;
            }
            ui->progressBar->setValue(recvSize/1024);
            if(recvSize == fileSize)
            {
                                //先给服务发送(接收文件完成的信息)
                                tcpSocket->write("file done");
                                ui->progressBar->setValue(fileSize/1024); //最大值

                                QMessageBox::information(this, "完成", "文件接收完成");

                                file.close(); //关闭文件
                                ui->progressBar->setValue(0); //当前值
                                //断开连接
                                tcpSocket->disconnectFromHost();
                                tcpSocket->close();
            }
        }

        }

    );
}



ClientFile::~ClientFile()
{
    delete ui;
}

void ClientFile::on_ButtonConnect_clicked()
{
    //获取服务器的ip和端口
    QString ip = ui->lineEditIP->text();
    quint16 port = ui->lineEditPort->text().toInt();

    //主动和服务器连接
    tcpSocket->connectToHost(QHostAddress(ip), port);

    isStart = true;

    //设置进度条
    ui->progressBar->setValue(0);
}

void ClientFile::on_pushButton_2_clicked()
{
    emit mySignal();
}

void ClientFile::on_pushButton_clicked()
{
    QString filePath = QFileDialog::getOpenFileName(this, "open", "../");
    if(false == filePath.isEmpty()) //如果选择文件路径有效
    {
        fileName.clear();
        fileSize = 0;

        //获取文件信息
        QFileInfo info(filePath);
        fileName = info.fileName(); //获取文件名字
        fileSize = info.size(); //获取文件大小

        sendSize = 0; //发送文件的大小

        //只读方式打开文件
        //指定文件的名字
        file.setFileName(filePath);

        //打开文件
        bool isOk = file.open(QIODevice::ReadOnly);
        if(false == isOk)
        {
            qDebug() << "只读方式打开文件失败 106";
        }

        //提示打开文件的路径
        ui->textEdit->append(filePath);

        ui->pushButton->setEnabled(false);
        ui->pushButton_3->setEnabled(true);

    }
    else
    {
        qDebug() << "选择文件路径出错 118";
    }
}
