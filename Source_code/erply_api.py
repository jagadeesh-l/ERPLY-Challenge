import os
import requests
import json
import csv
import xlsxwriter
from datetime import datetime


# DOMAIN_URL = r'https://reqres.in/'


class WebService:
    def __init__(self):
        self.csv_list = []
        cur_dir = os.getcwd()
        self.workbook = xlsxwriter.Workbook(
            cur_dir + os.sep + 'result' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.xlsx')
        self.worksheet = self.workbook.add_worksheet('result_sheet')
        self.response_session_key = {}

    def convert_csv_to_list(self, csv_file):
        row_col_list = []
        header_key = {}
        csv_file_obj = open(csv_file, 'r')
        csv_values = csv.reader(csv_file_obj)
        header = next(csv_values)
        print(header)
        key = next(csv_values)
        index_runflag = key.index('Runflag')
        filtered_csv = filter(lambda row: '1' == row[index_runflag], csv_values)
        csv_values_list = list(filtered_csv)
        for index in range(len(header)):
            if header[index] not in header_key:
                header_key[header[index]] = [key[index]]
            else:
                header_key[header[index]] = header_key[header[index]] + [key[index]]
        for row in csv_values_list:
            tdict = {}
            for index in range(len(key)):
                if row[index]:
                    tdict[key[index]] = row[index]
            row_col_list.append(tdict)
        for dictny in row_col_list:
            dictt = {}
            for key, value in header_key.items():
                tdict = {}
                for rk, rv in dictny.items():
                    if rk in value:
                        tdict[rk] = rv
                dictt[key] = tdict
            self.csv_list.append(dictt)
        print("Converted csv to list")

    def execute_testsuite(self):
        result_row = 7
        for testcase in self.csv_list:
            testid = testcase['info']['TestID']
            url = testcase['info']['url']
            request_method = testcase['info']['RequestMethod']
            # auth = testcase['auth']
            headers = testcase['headers']
            print(headers)
            print(type(headers))
            # if testcase['files']:
            #     files = open(testcase['files']['file'], 'rb')
            # else:
            #     files = testcase['files']
            param = testcase['param']
            if headers['Content-Type'] != 'application/json':
                joiner = '&'
                payload = ''
                len_param = len(param)
                for i, j in param.items():
                    payload = payload + i + '=' + j
                    len_param -= 1
                    if len_param != 0:
                        payload = payload + joiner
                param = payload
            else:
                print("Inside Else")
                print(param)
                param = json.loads(param['payload'])
                param = json.dumps(param)
                headers.update(self.response_session_key)
            print(param)
            web_request = {'testid': testid,
                           'RequestMethod': request_method,
                           'url': url,
                           # 'auth': auth,
                           'headers': headers,
                           'param': param,
                           'Expected_Response': testcase['Expected_Response']}

            call_service = Mapper().function_mapper(request_method, url, headers, param)
            try:
                response = call_service()
            except:
                pass
            print("Hey")
            print(response.status_code)
            print(response.text)
            try:
                self.response_session_key['sessionKey'] = json.loads(response.text)['records'][0]['sessionKey']
                print(self.response_session_key)
            except:
                pass
            self.generate_report(web_request, response, result_row)
            result_row += 1
            try:
                print(response.json())
            except:
                print(response.text)
        self.workbook.close()

    def generate_report(self, web_request, response, result_row):
        Expected_Response = json.dumps(web_request['Expected_Response'])
        status_code = str(response.status_code)

        title = ['TESTID', 'RequestMethod', 'URL', 'ExpectedResponse', 'ActualResponse', 'ActualResponseCode', 'Result']
        try:
            if ':' in web_request['Expected_Response']['Content_Response']:
                Content_Response = web_request['Expected_Response']['Content_Response'].split(':')[1]
            else:
                Content_Response = web_request['Expected_Response']['Content_Response']
            assert status_code == str(web_request['Expected_Response']['Response_code'])
            print(Content_Response, response.text)
            assert Content_Response in response.text
            pass_format = self.result_sheet_format('#9ACD32')
            result = ['Pass', pass_format]
        except AssertionError:
            fail_format = self.result_sheet_format('#FF7F50')
            result = ['Fail', fail_format]
        row = [web_request['testid'], web_request['RequestMethod'], web_request['url'], Expected_Response,
               response.text, status_code, result[0]]
        text_font = self.result_sheet_format('#778899')
        text_font.set_bold()

        self.worksheet.write_row('C6', title, text_font)
        self.worksheet.write_row('C' + str(result_row), row, result[1])
        return

    def result_sheet_format(self, colour_code):
        cell_font = self.workbook.add_format()
        cell_font.set_pattern(1)  # This is optional when using a solid fill.
        cell_font.set_bg_color(colour_code)  # colour_code
        cell_font.set_border()
        return cell_font


class Mapper:
    def function_mapper(self, request_method, url, headers, param):
        vobj = verbs(url, headers, param)
        mapper = {'get': vobj.get,
                  'post': vobj.post,
                  'put': vobj.put,
                  'delete': vobj.delete,
                  'patch': vobj.patch,
                  'head': vobj.head}
        if request_method.lower() in mapper:
            return mapper[request_method.lower()]


class verbs:
    def __init__(self, url, headers, param, auth=None, files=None):
        self.url = url
        self.auth = auth
        self.headers = headers
        self.files = files
        self.param = param

    def get(self):
        #         allow_redirects - Allows redirection of URL.
        #         verify          - For Unverified HTTPS request is being made.
        output = requests.get(self.url, allow_redirects=True, verify=True, auth=self.auth, headers=self.headers,
                              params=self.param)
        return output

    def post(self):
        output = requests.post(self.url, verify=True, auth=self.auth, headers=self.headers, data=self.param,
                               files=self.files)
        return output

    def delete(self):
        output = requests.delete(self.url, verify=True, auth=self.auth, headers=self.headers, params=self.param,
                                 files=self.files)
        return output

    def put(self):
        output = requests.put(self.url, verify=True, auth=self.auth, headers=self.headers, params=self.param,
                              files=self.files)
        return output

    def patch(self):
        output = requests.patch(self.url, verify=True, auth=self.auth, headers=self.headers, params=self.param,
                                files=self.files)
        return output

    def head(self):
        output = requests.head(self.url, verify=True, auth=self.auth, headers=self.headers, params=self.param)
        return output


if __name__ == '__main__':
    testcase_csv_path = "Challenge.csv"
    obj = WebService()
    obj.convert_csv_to_list(testcase_csv_path)
    obj.execute_testsuite()
