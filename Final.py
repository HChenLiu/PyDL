import sys
import UiSet
from PyQt5.QtWidgets import QApplication, QDialog
import requests

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UiSet.Ui_Dialog()
        self.ui.setupUi(self)
    
    def queryArticle(self):
        Category = self.ui.comboBox1.currentText()
        Type = self.ui.comboBox2.currentText()
        CategoryCode = self.get_CategoryCode(Category)
        TypeCode = self.get_TypeCode(Type)
        
        r = requests.get("https://gank.io/api/v2/data/category/{}/type/{}/page/1/count/10".format(CategoryCode,TypeCode))

        print(r.json())
        
        if r.json().get('status') == 200:
            weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
                r.json()['cityInfo']['city'],
                r.json()['data']['forecast'][0]['ymd'],
                r.json()['data']['forecast'][0]['type'],
                int(r.json()['data']['pm25']),
                r.json()['data']['quality'],
                r.json()['data']['wendu'],
                r.json()['data']['shidu'],
                r.json()['data']['forecast'][0]['fl'],
                r.json()['data']['forecast'][0]['notice'],
            )
        else:
            weatherMsg = '天气查询失败，请稍后再试！'
        
        self.ui.textEdit.setText(weatherMsg)
    
    def get_CategoryCode(self, Category):
        CategoryDict = {"Article": "Article",
                    "Skill": "GanHuo",
                    "Girl": "Girl"}
                 
        return CategoryDict.get(Category)

    def get_TypeCode(self, Type):
        CategoryDict = {"Android": "Android",
                    "iOS": "iOS",
                    "Flutter": "Flutter",
                    "frontend":"frontend",
                    "app":"app"}
                 
        return CategoryDict.get(Type)
    
    def clearText(self):
        self.ui.textEdit.clear()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())