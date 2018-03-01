class ExcelXMLToPandas:
    from bs4 import BeautifulSoup
    import pandas as pd
    
    workbooks = []
    workbook_colNames = []
            
    def _clean_vars(self):
        self.workbooks = []
        self.workbook_colNames = []
    
    def read_excel_xml(self, path,skip_rows=0,is_header_first_row=True):
        self._clean_vars()
        
        file = open(fullpath).read()
        soup = BeautifulSoup(file,'xml')

        for xmlsheet in soup.findAll('Worksheet'): 
            sheet = []
            i=0
            isFirstProcessedRow = True
            for row in xmlsheet.findAll('Row'):
                if i>=skip_rows:
                    if isFirstProcessedRow:
                        isFirstProcessedRow=False
                        colNames = []
                        for cell in row.findAll('Cell'):
                            colNames.append(cell.Data.text)
                        self.workbook_colNames.append(colNames)
                    else:
                        row_as_list = []
                        for cell in row.findAll('Cell'):
                            row_as_list.append(cell.Data.text)
                        sheet.append(row_as_list)
                i+=1
            self.workbooks.append(sheet)
        
        self._column_names_complete()
        return self.workbooks,self.workbook_colNames

    def _column_names_complete(self):
        for i, wk in enumerate(self.workbooks):
            df = pd.DataFrame(self.workbooks[0])
            
            while (len(df.columns) - len(self.workbook_colNames[0])) >0:
                self.workbook_colNames[0].append("COL_X_"+str(i))
                
    def Get_DataFrame(self, index = 0):
        self._column_names_complete()
        df = pd.DataFrame(self.workbooks[index], columns=self.workbook_colNames[index])
        return df
