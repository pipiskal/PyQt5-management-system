import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table, self).__init__(parent)
        #Set title and initial size
        self.setWindowTitle('QTableView table check box case')
        self.resize(600,300)
        self.tableView=QTableView()
        self.model = QStandardItemModel(self.tableView)

                 #Set the data hierarchy,4Row4Column
        self.model=QStandardItemModel(4,4)
        self.check_box = QCheckBox(self)
                 #Set the text content of the four header labels in the horizontal direction
        self.model.setHorizontalHeaderLabels(['status','Name','ID card','address'])

        for row in range(4):
            for column in range(4):
                item_checked = QStandardItem()
                item_checked.setCheckState(Qt.Checked)
                item_checked.setCheckable(True)
                self.model.setItem(column,0, item_checked)
                item=QStandardItem('row %s,column %s'%(row,column))
                                 #Set the text value of each position
                self.model.setItem(row,column,item)

        self.tableView.setModel(self.model)
                 #Set layout
        layout=QVBoxLayout()
        layout.addWidget(self.check_box)
        layout.addWidget(self.tableView)
        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    table=Table()
    table.show()
    sys.exit(app.exec_())