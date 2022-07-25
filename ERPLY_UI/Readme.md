 UI Automation Testing - Validate all the possible scenarios by Playwright
===============================================================================

What framework used?
--------------------

- Pytest-BDD with playwright.
    - UI Automation through behaviour driven feature files
- Page Object Model (POM)
    - Maintaining all the Object Repository in page wise which helps to modify/change in one place.



What Packages used?
-------------------

- Playwright 	       - For UI Automation
- pytest-bdd  	      - For Behaviour Driven
- Allure             - For Reporting test run

How to use this Framework?
--------------------------


1. This is behaviour based framework, all the test-cases are written in feature file.
2. This feature file is to feed to the framework for execution.
3. Based on the Feature file scenarios, automation will be triggered.
- GOTO  tests.step_defs folder location and enter following command,
    - py.test --browser chromium --headed --slowmo 100 -s --alluredir='/../ERPLY_UI/report'



How reports are generated?
--------------------------


1. If Expected_Response matches with the Actual_Response, framework will generate the report as Pass else report will be generated as Fail.
2. Report will be generated in the ".json" format.
3. Report file is stored in the same folder where the tests folder is present.
- Able to launch results in HTML format with help of allure reporting by using following command,
    - allure serve '/../ERPLY_UI/report/'


Enhancements:
-------------

Reporting -> Allure or any interactive report

Bugs Found During Testing:
---------------------------

1. Accessibility is not working -> like tab tab and enter product name and press enter key.
2. Search for a code and if two results are coming and if we press enter, only first one is getting selected.
3. Searched items is added and incremented only sequentially.
4. Application is crashing while executing automation.

