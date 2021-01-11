#include "cancel.h"
#include "ui_cancel.h"

#include <QDebug>
#include <QMessageBox>
#include <QHostAddress>
#include <QFileDialog>
#include <QFileInfo>
#include <QProcess>

Cancel::Cancel(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Cancel)
{

    QPalette pal = this->palette();
    pal.setBrush(QPalette::Background,QBrush(QPixmap(":/new/prefix1/icon/gback.png")));
    setPalette(pal);
    ui->setupUi(this);
    //ui->pushButton_1->setStyleSheet("background:white;");
    //ui->pushButton_2->setStyleSheet("background:white;");
    //ui->pushButton->setStyleSheet("background:white;");
    //ui->pushButton_4->setStyleSheet("background:white;");
    //ui->pushButton_5->setStyleSheet("background:white;");
    //ui->pushButton_6->setStyleSheet("background:white;");
    //QPalette pal0 = ui->lineEdit->palette();
    //pal0.setBrush(QPalette::Base, Qt::transparent);
    //ui->lineEdit->setPalette(pal0);
   // QPalette pal1 = ui->lineEdit_2->palette();
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



Cancel::~Cancel()
{
    delete ui;
}

void Cancel::on_pushButton_clicked()
{
    QFile file("G:/xinan/TcpFile/runclient/user.txt");//文件命名
    if (!file.open(QFile::WriteOnly | QFile::Text))		//检测文件是否打开
    {
        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
        return;
    }
    QTextStream out(&file);					//分行写入文件
    out <<"#DELETE";

    QString str = ui->textEdit->toPlainText();
    //将文本框数据取出并按行排列
    QFile file0("G:/xinan/TcpFile/runclient/user.txt");//文件命名
    if (!file0.open(QFile::Append | QFile::Text))		//检测文件是否打开
    {
        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
        return;
    }
    //QTextStream out(&file0);					//分行写入文件
    out << ui->textEdit->toPlainText();
    ui->textEdit->clear();

}
void Cancel::on_pushButton_1_clicked()
{
    ui->show_txt->clear();
    emit mySignal();
}

void Cancel::on_pushButton_2_clicked()
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

    //清除编辑区内容
    //ui->textEdit->clear();
    out <<" 123 ";
}
void Cancel::on_pushButton_3_clicked()
{
    QProcess p(0);
    QProcess process(this);
    process.execute("test_recover.exe");
    QFile *file=new QFile("G:/xinan/new_code/test/result_login.txt");
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

void Cancel::on_pushButton_4_clicked()
{
    //主动和对方断开连接
    tcpSocket->write("客户端已断开");
    tcpSocket->disconnectFromHost();
    tcpSocket->close();
}

//void Cancel::on_pushButton_5_clicked()
//{
    //将文本框数据取出并按行排列
//    QFile file("G:/xinan/TcpFile/runclient/user.txt");//文件命名
//    if (!file.open(QFile::WriteOnly | QFile::Text))		//检测文件是否打开
//    {
//        QMessageBox::information(this, "Error Message", "Please Select a Text File!");
//        return;
//    }
//    QTextStream out(&file);					//分行写入文件
//    out <<"#DELETE";
//    out << ui->textEdit->toPlainText();
//
//}

void Cancel::on_pushButton_6_clicked()
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




