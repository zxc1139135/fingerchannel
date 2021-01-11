#include "client.h"
#include "ui_client.h"
#include <QHostAddress>
#include <QMessageBox>

Client::Client(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Client)
{
    ui->setupUi(this);
    //ui->ButtonSend->setStyleSheet("background:white;");
    //ui->ButtonConnect->setStyleSheet("background:white;");
    //ui->pushButton->setStyleSheet("background:white;");
    //ui->ButtonClose->setStyleSheet("background:white;");
    //ui->pushButton2->setStyleSheet("background:white;");
    //ui->pushButton3->setStyleSheet("background:white;");
    //ui->pushButton4->setStyleSheet("background:white;");
    QPalette pal = this->palette();
    pal.setBrush(QPalette::Background,QBrush(QPixmap(":/new/prefix1/icon/back.jpg")));
    setPalette(pal);
    //QPalette pal0 = ui->show_text->palette();
    //pal0.setBrush(QPalette::Base, Qt::transparent);
    //ui->show_text->setPalette(pal0);
    //QPalette pal1 = ui->textEditRead->palette();
    //pal1.setBrush(QPalette::Base, Qt::transparent);
    //ui->show_text->setPalette(pal1);
    //QPalette pal2 = ui->textEditRead->palette();
   // pal2.setBrush(QPalette::Base, Qt::transparent);
   // ui->lineEditIP->setPalette(pal2);
    //QPalette pal3 = ui->textEditRead->palette();
   // pal3.setBrush(QPalette::Base, Qt::transparent);
    //ui->lineEditPort->setPalette(pal3);
    //QPalette pal4 = ui->textEditRead->palette();
    //pal4.setBrush(QPalette::Base, Qt::transparent);
    //ui->textEditRead->setPalette(pal4);
    tcpSocket = NULL;

    //分配空间，指定父对象
    tcpSocket = new QTcpSocket(this);

    setWindowTitle("客户端");

    connect(&w2, SIGNAL(mySignal()), this, SLOT(dealW2()) );
	
    connect(&w3, SIGNAL(mySignal()), this, SLOT(dealW3()) );

    connect(&w4, SIGNAL(mySignal()), this, SLOT(dealW4()) );

    connect(&w5, SIGNAL(mySignal()), this, SLOT(dealW5()) );

    connect(tcpSocket, &QTcpSocket::connected,
            [=]()
            {
                //ui->textEditRead->setText("成功和服务器建立好连接");
            }
            );

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

Client::~Client()
{
    delete ui;
}

void Client::on_ButtonConnect_clicked()
{
    //获取服务器ip和端口
    //QString ip = ui->lineEditIP->text();
    //qint16 port = ui->lineEditPort->text().toInt();

    //主动和服务器建立连接
    //tcpSocket->connectToHost(QHostAddress(ip), port);
}

void Client::on_ButtonSend_clicked()
{
    //获取编辑框内容
   // QString str = ui->textEditWrite->toPlainText();
    //发送数据
    //tcpSocket->write( str.toUtf8().data() );
    //清除编辑区内容
    //ui->textEditWrite->clear();
}

void Client::on_ButtonClose_clicked()
{
    //主动和对方断开连接
    tcpSocket->write("客户端已断开");
    tcpSocket->disconnectFromHost();
    tcpSocket->close();
}



void Client::on_pushButton_clicked()
{
    this->hide();
    w2.show();
}

void Client::dealW2()
{
    w2.hide();
    show();
}
//登录
void Client::on_pushButton2_clicked()
{
    QFile file("G:/xinan/TcpFile/runclient/user.txt");//文件命名
    if (!file.open(QFile::WriteOnly | QFile::Text))		//检测文件是否打开
    {
        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
        return;
    }
    QTextStream out(&file);					//分行写入文件
    out <<"1 ";
	this->hide();
    w3.show();
}

void Client::dealW3()
{
    w3.hide();
    show();
}
//注册
void Client::on_pushButton3_clicked()
{
    QFile file("G:/xinan/TcpFile/runclient/user.txt");//文件命名
    if (!file.open(QFile::WriteOnly | QFile::Text))		//检测文件是否打开
    {
        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
        return;
    }
    QTextStream out(&file);					//分行写入文件
    out <<"0 ";
    this->hide();
    w4.show();
}

void Client::dealW4()
{
    w4.hide();
    show();
}
//注销
void Client::on_pushButton4_clicked()
{
    QFile file("G:/xinan/TcpFile/runclient/user.txt");//文件命名
    if (!file.open(QFile::WriteOnly | QFile::Text))		//检测文件是否打开
    {
        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
        return;
    }
    QTextStream out(&file);					//分行写入文件
    out <<"1 ";
    this->hide();
    w5.show();
}

void Client::dealW5()
{
    w5.hide();
    show();
}
