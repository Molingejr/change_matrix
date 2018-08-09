# Testing
This part of the project contains our test suit with test cases for some data structures and features in our project.
### Run test suits
You can run the test by using the command
`$ python test_file`

If you want to run all the tests at once and see descriptive informations, install *pytest* to run all your test cases as a suit with the following command
```
$ pip install pytest
$ pytest tests
```
Where tests is our *test* directory which contains all the test files.


### Note
If you run the test and it complains about module imports, do either of the following:
* Include this repository in your environmental variables
* Run the following command in your root directory:
    - `$ python -m tests.test_name` where test_name is the name of your test file without .py
