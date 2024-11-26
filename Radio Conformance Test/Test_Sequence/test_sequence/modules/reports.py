#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import xlsxwriter
from setup import dir

class reports():
    def __init__(self):
        pass

    def new(self):
        pass

    def write(self):
        pass

    def output_txt(self, result):
        test_case = result["test_case"]
        test_data = result["test_data"]
        test_time = result["test_time"]
        test_result = result["test_result"]
        test_results = [
            {"test_case": "test_case", "test_data": "test_data", "test_time": "test_time", "test_result": "test_result", },
            {"test_case": test_case, "test_data": test_data, "test_time": test_time, "test_result": test_result, },
            {"test_case": "", "test_data": "", "test_time": "", "test_result": "", },
            {"test_case": "", "test_data": "", "test_time": "", "test_result": "", },
            {"test_case": "", "test_data": "", "test_time": "", "test_result": "", },
            {"test_case": "", "test_data": "", "test_time": "", "test_result": "", },
        ]
        print(dir)
        with open(dir+"test_report.txt", 'w') as report:
            # for i in range(len(txt)):
            #     report.write(txt[i]["test_case"]+"\n")
            #     report.write(txt[i]["test_data"]+"\n")
            #     report.write(txt[i]["test_result"]+"\n")
            #     report.write(txt[i]["test_time"]+"\n")

            report.write("Test Report\n")
            report.write("=" * 40 + "\n")
            for case in test_results:
                # report.write(f"Test Case:{result["test_case"]}\n")
                report.write(f"test_case: {case['test_case']}\n")
                report.write(f"test_data: {case['test_data']}\n")
                report.write(f"test_time: {case['test_time']}\n")
                report.write(f"test_result: {case['test_result']}\n")
                report.write("-" * 40 + "\n")

        return report


    def output_HTML(self,result):
        test_case = result["test_case"]
        test_data = result["test_data"]
        test_time = result["test_time"]
        test_result = result["test_result"]

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{test_case}</title>
        </head>
        <body>
            <tr>
                <td>test_case: {test_case}<br></td>
                <td>test_data: {test_data}<br></td>
                <td>test_time: {test_time}<br></td>
                <td>test_result: {test_result}<br></td>
            </tr>
        </body>
        </html>
        """
        with open(dir+'report.html', 'w') as report:
            report.write(html_content)

        return report

    def output_csv(self,result):
        test_case = result["test_case"]
        test_data = result["test_data"]
        test_time = result["test_time"]
        test_result = result["test_result"]

        # report=xlsxwriter.Workbook('report.xlsx')
        print(dir)
        with open(dir+'report.csv','w') as report:
            report.write("test_case,test_data,test_time,test_result,\n")
            report.write(f"{test_case},{test_data},{test_time},{test_result},\n")
            report.write("-" * 40 + "\n")
        # report.add_worksheet(name=f"{test_case}")
        # report.close()

        return report


if __name__ == '__main__':
    # report = reports()
    # print(dir)
    # result = {
    #     "test_case": "tx_power",
    #     "test_result": "pass",
    #     "test_data": "7dBm",
    #     "test_time": "1s",
    # }
    # print(report.output_txt(result))
    # print(report.output_HTML(result))
    # print(report.output_csv(result))
    from test_sequence.testcases.data_testcase import for_result
    result = for_result().get_result()
    report = reports()
    print(report.output_txt(result))
    print(report.output_HTML(result))
    print(report.output_csv(result))


