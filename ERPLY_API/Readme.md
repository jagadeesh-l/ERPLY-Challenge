 Web-service Testing - Validate all the possible scenarios by triggering APIs
===============================================================================

What framework used?
--------------------

Custom framework using Python with requests.



What Packages used?
-------------------


JSON 	   - For json conversion
CSV  	   - Fetching testcase fron csv
XLSXWRITER - For generating test report


How to use this Framework?
--------------------------


This is behaviour based framework, all the test-cases are written in csv file.
This csv file is feed to the framework for webservice execution.
Based on the request input, web-service will be triggered.
RUN dbs_api_testing.py and give your testcase.csv file along with the location. Eg: (/Project_webservice/testcase.csv)



How reports are generated?
--------------------------


If Expected_Response matches with the Actual_Response, framework will generate the report as Pass else report will be generated as Fail.
Report will be generated in the ".xlsx" format.
Report file is stored in the same folder where the script is present.
File will be in the "result" + "current_date_time".xlsx format. Eg: (result20190130185639.xlsx)



Define Implementation?
----------------------


Have defined each method for post, put, get, delete, patch, head


Define each Classes and Methods used?
-------------------------------------


Classes:

	1. WebService   - This class will form the data from the csv and it will trigger the APIs then generate the reports.
	      Methods   - 1. convert_csv_to_list: It will convert the csv to list of dictionary.
			  2. execute_testsuite  : It will execute the test suite by posting each test-case.
			  3. generate_report    : It will assert the test-case and it will generate the report.
			  4. result_sheet_format: It is used for cell formatting.


	2. Mapper     	- This will map the api request based on the request method.
		  Methods   - 1. function_mapper    : It will map request methods.


	3. verbs	- This will maintain all the request methods
		  Methods   - 1. get    : Get the data and return.
			      2. post   : Post the data and return.
			      3. put    : Update the data if not, create and return.
			      4. delete : Delete the data and return.
			      5. patch  : update the particular date and return.
			      6. head	: Get the header and return.


Scenarios coverage?
-------------------

1. Please view the "report_info.txt" for the scenario coverage.


Enhancements:
-------------


1. Generate the tokens on the fly and verify the cases.
2. Test and Create the scenarios based on the response on the fly.
3. Reporting -> Allure or any interactive report


Continuous Integration/ Continuous Deployment (CI/CD):
________________________________________________________

I have exposure only to Jenkins, so using Jenkins I will do continuous integration and Continuous deployment.
- How to do it?
	- I will first set the job pipeline and schedule the job in following manner.
	   - Based on new branch merge request into master/release branch, I will trigger the API automation once new code
           is merged.
	   - After successful API automation run, based on result report (if all pass), we can move the code base to deployment. If result fails,
           should abort the deployment(re-try can be done based on the investigation).


