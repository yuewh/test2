# coding:utf-8
__author__ = 'luws'
import xlrd
from src.common import log
from config.globalparameter import test_data_path

'''
读取excel文件
'''


class excel_data:
    def __init__(self):
        self.mylog = log.log()

    def open_excel(self, file):
        '''读取excel文件'''
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            self.mylog.error("打开excel文件失败")

    # 以表头为key，形成字典，构成列表
    # def dictdata(self):
    #     if self.nrows <= 1:
    #         print('excel文件行数小于等于1')
    #     else:
    #         list = []
    #         j = 1
    #         for rownum in range(1, self.nrows):
    #             temp = {}
    #             value = self.table.row_values(j)
    #             for i in range(self.nclos):
    #                 temp[self.keys[i]] = value[i]
    #             list.append(temp)
    #             j += 1
    #         return list

    def excel_list(self, file, sheetName):
        data = self.open_excel(file)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取行数
        Trows = table.nrows

        list = []
        for rownum in range(1, Trows):
            temp = table.row_values(rownum)
            list.append(temp)
        return list

    def get_list(self, sheetname):
        try:
            data_list = self.excel_list(test_data_path, sheetname)
            assert len(data_list) > 0, 'excel标签页:' + sheetname + '为空'
            # self.mylog.info('excel文件读取成功' + str(data_list))
            return data_list
        except AssertionError as e:
            self.mylog.error('excel标签页:' + sheetname + '为空')
            raise e
        except xlrd.biffh.XLRDError as e:
            self.mylog.error('excel标签页:' + sheetname + '不存在')
            raise e


if __name__ == '__main__':
    excel_data().get_list('creatimumuban')
