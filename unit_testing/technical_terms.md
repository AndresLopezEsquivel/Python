- **Test suite**: Collection of tests that target related functionality.
- Every test should be isolated and independent (each test tests a single unit or section of the program). This means that a test shouldn't rely on or affect other tests.
- **Test coverage / Code coverage**: Percentage of the codebase to which tests have been written for.
  - The goal is to write tests for the most critical parts of the business application.
- Unit tests are in-memory tests because they cannot connect to external entities such as databases (those external entities must be imitated or mocked).
- **TDD** (_Test Driven Development_):
  - Write tests before writing a single line of code.
  - This forces you to think about what your code should do.
- Check:
  - <a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug">unittest: Unit testing framework.</a>
  - <a href="https://www.youtube.com/watch?v=6tNS--WetLI">Python Tutorial: Unit Testing Your Code with the unittest Module</a>

# unittest: Unit testing framework

To run a test file:

```
python3 -m unittest test_calc.py
```

If we wanto to run our tests using `python3 test_calc.py`, we need to add to
`test_calc.py`:

```
if __name__ == "__main__":
  unittest.main()
```
