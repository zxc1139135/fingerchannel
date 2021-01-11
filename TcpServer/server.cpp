#include "server.h"
#include "ui_server.h"
#include <QDebug>
#include <QMessageBox>
#include <QHostAddress>
#include <QFileDialog>
#include <QFileInfo>
#include <QProcess>
#include <QFile>

Server::Server(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Server)
{

    ui->setupUi(this);
    QPalette pal = this->palette();
    pal.setBrush(QPalette::Background,QBrush(QPixmap(":/new/prefix1/icon/pback.png")));
    this->setWindowIcon(QIcon(":/new/prefix1/icon/finger.bmp"));
    setPalette(pal);
    //ui->pushButton->setStyleSheet("background:white;");
    //ui->pushButton_2->setStyleSheet("background:white;");
    //ui->pushButton_3->setStyleSheet("background:white;");
    //ui->pushButton_4->setStyleSheet("background:white;");
    //ui->ButtonSend->setStyleSheet("background:white;");
   // ui->ButtonFile->setStyleSheet("background:white;");
    //ui->ButtonClose->setStyleSheet("background:white;");
    //connect(&w3, SIGNAL(clicked()), this, SLOT(on_pushButton_clicked()));
    QPalette pal0 = ui->textEditRead->palette();
    pal0.setBrush(QPalette::Base, Qt::transparent);
    ui->textEditRead->setPalette(pal0);
    //QPalette pal1 = ui->textEditWrite->palette();
    //pal1.setBrush(QPalette::Base, Qt::transparent);
    //ui->textEditWrite->setPalette(pal1);
    QPalette pal2 = ui->show_txt->palette();
    pal2.setBrush(QPalette::Base, Qt::transparent);
    ui->show_txt->setPalette(pal2);
    tcpServer = NULL;
    tcpSocket = NULL;

    //监听套接字，指定父对象，让其自动回收空间
    tcpServer = new QTcpServer(this);

    tcpServer->listen(QHostAddress::Any, 9999);

    setWindowTitle("服务端");
    connect(&w2, SIGNAL(mySignal()), this, SLOT(dealW2()) );
    connect(&w3, SIGNAL(mySignal()), this, SLOT(dealW3()) );
    connect(tcpServer, &QTcpServer::newConnection,
            [=]()
            {
                //取出建立好连接的套接字
                tcpSocket = tcpServer->nextPendingConnection();

                //获取对方的IP和端口
                QString ip = tcpSocket->peerAddress().toString();
                qint16 port = tcpSocket->peerPort();
                QString temp = QString("[%1:%2]:客户端成功连接至服务器, 如果不允许登录\\注册\\注销, 请断开连接").arg(ip).arg(port);

                ui->textEditRead->setText(temp);

                connect(tcpSocket, &QTcpSocket::readyRead,
                        [=]()
                        {
                            //从通信套接字中取出内容
                        QString temp = QString("客户端发送至服务器ID信息为\n");

                        ui->textEditRead->setText(temp);
                            QByteArray array = tcpSocket->readAll();
                            ui->textEditRead->append(array);
                        }

                        );


            }

            );
}


Server::~Server()
{
    delete ui;
}

void Server::on_ButtonSend_clicked()
{
    if(NULL == tcpSocket)
    {
        return;
    }
    //获取编辑区内容
   // QString str = ui->textEditWrite->toPlainText();
    //给对方发送数据， 使用套接字是tcpSocket
   // tcpSocket->write( str.toUtf8().data() );
    //清除编辑区内容
   // ui->textEditWrite->clear();
}



void Server::on_ButtonClose_clicked()
{
    if(NULL == tcpSocket)
    {
        return;
    }

    tcpSocket->write("服务端断开，请重新连接");
    //主动和客户端端口连接
    tcpSocket->disconnectFromHost();
    tcpSocket->close();
    tcpSocket = NULL;
}

//切换按钮
void Server::on_ButtonFile_clicked()
{
    this->hide();

    w2.show();

}

void Server::dealW2()
{
    //子窗口隐藏
    w2.hide();
    //本窗口显示
    show();
}

//登录验证
void Server::on_pushButton_clicked()
{
    QFile *file0=new QFile("G:/xinan/TcpFile/runsever/informationForLogin.txt");
    if (file0->open(QIODevice::ReadOnly | QIODevice::Text))
    {
        ui->show_txt->clear();
        while (!file0->atEnd())
        {
            QByteArray line = file0->readLine();
            QString str(line);

            ui->show_txt->append(tr("%1").arg(str.remove("\n")));
        }

        file0->close();
    }
    QProcess p(0);
    QProcess process(this);
    process.execute("test_login_check_server.exe");
    QFile *file=new QFile("G:/xinan/new_code/test/GBF.txt");
    if (file->open(QIODevice::ReadOnly | QIODevice::Text))
    {
        //ui->show_txt->clear();
        while (!file->atEnd())
        {
            QByteArray line = file->readLine();
            QString str(line);

            ui->show_txt->append(tr("%1").arg(str.remove("\n")));
        }

        file->close();
    }


}

//注册指纹信息
void Server::on_pushButton_2_clicked()
{
    QFile *file=new QFile("G:/xinan/TcpFile/runsever/informationForRegister.txt");
    if (file->open(QIODevice::ReadOnly | QIODevice::Text))
    {
        ui->show_txt->clear();
        while (!file->atEnd())
        {
            QByteArray line = file->readLine();
            QString str(line);

            ui->show_txt->append(tr("%1").arg(str.remove("\n")));
        }

        file->close();
    }
}



//服务器开启连接
void Server::on_pushButton_4_clicked()
{
    QProcess p0(0);
    QProcess process0(this);
    process0.execute("channel_server.exe");
    QFile *file0=new QFile("G:/xinan/new_code/test/channel_server_key.txt");
    if (file0->open(QIODevice::ReadOnly | QIODevice::Text))
     {
        ui->show_txt->clear();
        while (!file0->atEnd())
        {
            QByteArray line = file0->readLine();
            QString str(line);

            ui->textEditRead->append(tr("%1").arg(str.remove("\n")));
         }

         file0->close();
      }
    //QProcess p(0);
    QProcess process(this);
    process.execute("G:/xinan/aaa/new/server_withmysql.exe");
}

void Server::on_pushButton_5_clicked()
{
    QFile *file0=new QFile("G:/xinan/TcpFile/runsever/informationForLogin.txt");
    if (file0->open(QIODevice::ReadOnly | QIODevice::Text))
    {
        ui->show_txt->clear();
        while (!file0->atEnd())
        {
            QByteArray line = file0->readLine();
            QString str(line);

            ui->show_txt->append(tr("%1").arg(str.remove("\n")));
        }

        file0->close();
    }
    QProcess p(0);
    QProcess process(this);
    process.execute("test_login_check_server.exe");
    QFile *file=new QFile("G:/xinan/new_code/test/GBF.txt");
    if (file->open(QIODevice::ReadOnly | QIODevice::Text))
    {
        //ui->show_txt->clear();
        while (!file->atEnd())
        {
            QByteArray line = file->readLine();
            QString str(line);

            ui->show_txt->append(tr("%1").arg(str.remove("\n")));
        }

        file->close();
    }


}
