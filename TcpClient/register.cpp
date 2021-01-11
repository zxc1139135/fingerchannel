#include "register.h"
#include "ui_register.h"

#include <QProcess>
#include <QDebug>
#include <QMessageBox>
#include <QHostAddress>
#include <QFileDialog>
#include <QFileInfo>

Register::Register(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Register)
{
    QPalette pal = this->palette();
    pal.setBrush(QPalette::Background,QBrush(QPixmap(":/new/prefix1/icon/aback.png")));
    setPalette(pal);
    ui->setupUi(this);
    //ui->pushButton->setStyleSheet("background:white;");
    //ui->pushButton_2->setStyleSheet("background:white;");
    //ui->pushButton_3->setStyleSheet("background:white;");
    //ui->pushButton_4->setStyleSheet("background:white;");
    //ui->pushButton_5->setStyleSheet("background:white;");
    //ui->pushButton_6->setStyleSheet("background:white;");
    //ui->pushButton_7->setStyleSheet("background:white;");
    //ui->pushButton_8->setStyleSheet("background:white;");
    //ui->pushButton_9->setStyleSheet("background:white;");
    //QPalette pal0 = ui->lineEdit->palette();
    //pal0.setBrush(QPalette::Base, Qt::transparent);
    //ui->lineEdit->setPalette(pal0);
    //QPalette pal1 = ui->lineEdit_2->palette();
    //pal1.setBrush(QPalette::Base, Qt::transparent);
    //ui->lineEdit_2->setPalette(pal1);
    QPalette pal2 = ui->textEdit->palette();
    pal2.setBrush(QPalette::Base, Qt::transparent);
    ui->textEdit->setPalette(pal2);
    QPalette pal3 = ui->show_txt->palette();
    pal3.setBrush(QPalette::Base, Qt::transparent);
    ui->show_txt->setPalette(pal3);
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


Register::~Register()
{
    delete ui;
}


void Register::on_pushButton_clicked()
{
    ui->show_txt->clear();
    emit mySignal();
}

void Register::on_pushButton_2_clicked()
{

    QProcess p(0);
    QProcess process(this);
    process.execute("fingerprint_processing_client.exe");
    QFile *file=new QFile("G:/xinan/TcpFile/runclient/user.txt");
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

void Register::on_pushButton_4_clicked()
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
       // ui->pushButton_3->setEnabled(true);

    }
    else
    {
        qDebug() << "选择文件路径出错 118";
    }
}

void Register::on_pushButton_7_clicked()
{
    //获取编辑框内容
    QString str = ui->textEdit->toPlainText();
    //将文本框数据取出并按行排列
    QFile file("G:/xinan/TcpFile/runclient/user.txt");//文件命名
    if (!file.open(QFile::Append | QFile::Text))		//检测文件是否打开
    {
        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
        return;
    }
    QTextStream out(&file);					//分行写入文件
    out << ui->textEdit->toPlainText();

    //发送数据
    tcpSocket->write( str.toUtf8().data() );
    //清除编辑区内容
    ui->textEdit->clear();
    out <<" 789 ";
}
void Register::on_pushButton_5_clicked()
{
    //获取服务器ip和端口
   // QString ip = ui->lineEdit->text();
    //qint16 port = ui->lineEdit_2->text().toInt();

    //主动和服务器建立连接
    //tcpSocket->connectToHost(QHostAddress(ip), port);
}

void Register::on_pushButton_6_clicked()
{
    //主动和对方断开连接
    tcpSocket->write("客户端已断开");
    tcpSocket->disconnectFromHost();
    tcpSocket->close();
}


void Register::on_pushButton_9_clicked()
{
    QProcess p0(0);
    QProcess process0(this);
    process0.execute("channel_client.exe");
    QFile *file0=new QFile("G:/xinan/new_code/test/result_channel.txt");
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

    //QProcess p(0);
    QProcess process(this);
    process.execute("G:/xinan/aaa/new/imclient.exe");

    QFile *file=new QFile("G:/xinan/TcpFile/runclient/clientreceive.txt");

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
