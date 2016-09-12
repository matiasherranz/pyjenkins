# Python demo project for Jenkins course

## Setup

- Install virtualenvwrapper
- Create and activate a virtualenv with a name of your choosing
- Install the requirements (requirements.txt has them all)
- Run the tests:

```bash
$ cd pyjenkins_demo/
$ python manage.py test
```

Something like this should be the output of the latest command:

```bash
(pyjenkins) --> pyjenkins_demo (git: master ? m) $ python manage.py test
Creating test database for alias 'default'...

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
Destroying test database for alias 'default'...
```
