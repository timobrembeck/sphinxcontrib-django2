Changelog
=========

Unreleased
----------

Merge this fork `sphinxcontrib_django2 <https://pypi.org/project/sphinxcontrib-django2/>`_ back into the original package `sphinxcontrib_django <https://pypi.org/project/sphinxcontrib-django/>`_.
This changelog continues `here <https://github.com/edoburu/sphinxcontrib-django/blob/main/CHANGES.rst>`_.


Version 1.6 (2022-11-24)
------------------------

* Add inline docstrings of model fields to parameter documentation of models
* Add support for Python 3.11
* Add support for Django 4.1
* Drop support for Django 2.2


Version 1.5 (2022-01-05)
------------------------

* Support string foreign keys of abstract models


Version 1.4 (2022-01-05)
------------------------

* Do not reference related names of abstract models
* Drop support for Python 3.6
* Drop support for Django 3.1
* Add support for Django 4.0


Version 1.3 (2021-11-20)
------------------------

* Fix ``AttributeError`` when ``django.contrib.contenttypes`` is not in ``INSTALLED_APPS``
* Emit sphinx event ``django-configured`` after ``django.setup()`` is finished to allow monkeypatching django during
  documentation build


Version 1.2 (2021-11-08)
------------------------

* Add support for Python 3.10
* Add support for Django 3.2
* Drop support for Django 3.0
* Add option ``django_show_db_tables`` to list the database table names of Django models in their docstring


Version 1.1.1 (2021-03-02)
--------------------------

* Support django.db.models.JSONField
* List choices of choice fields


Version 1.1 (2021-03-02)
------------------------

* Add support for Python 3.9
* Add support for django-mptt with Django >=3.1
* Append initial docstrings to attributes
* Fix mutable references of pre-commit hooks
* Fix tests for sphinx 3.5.0


Version 1.0.2 (2021-02-02)
--------------------------

* Add support for GenericForeignKey field of django.contrib.contenttypes


Version 1.0.1 (2021-02-02)
--------------------------

* Fix Intersphinx mappings to AppConfig and Manager classes


Version 1.0 (2021-01-24)
------------------------

* Fix more Intersphinx mappings to Django classes
* Refactor package structure
* Refactor tests
* Improve docstring output
* Improve handling of related and reverse related fields
* Add documentation for sphinxcontrib_django2 itself
* Improve docstrings of iterable data
* Add config value for Django settings
* Load autodoc and intersphinx extensions in setup()
* Provide default intersphinx_mapping
* Return extension metadata in setup()
* Move dev dependencies from Pipfile to setup.py
* Add readthedocs.io integration


Version 0.7 (2020-11-30)
------------------------

* Fix Intersphinx mappings to Django classes
* 100% test coverage


Version 0.6 (2020-11-16)
--------------------------

* Fix deferred attribute for Django >=2.1, <3.0
* Django: Drop support for [1.11, 2.0], add support for [2.2, 3.0, 3.1]
* Python: Drop support for [2.7, 3.5], add support for [3.6, 3.7, 3.8]
* Replace force_text by force_str (deprecated in Django 4.0)
* Improved test coverage
* Support for Django ModelFields


Version 0.5.1 (2020-01-26)
--------------------------

* Fix deferred attribute for Django 3.0.


Version 0.5 (2019-08-09)
------------------------

* Model fields always show verbose name if present.
* Model fields are skipped when they are already documented.
* Support "self" in foreign keys.
* Allow ``:setting:`` registration to fail
* Fixed ``runtests.py`` for Django 2.2
* Reformatted all source code with black, isort and flake8


Version 0.4 (2018-07-26)
------------------------

* Fixed Django 2.0 behavior when foreignkeys are strings.


Version 0.3.1 (2018-03-11)
--------------------------

* Fixed Python 2 issue with ``list.clear()``.


Version 0.3 (2018-02-19)
------------------------

* Fixed Django 2.0 support
* Fixed missing form fields
* Fixed handling of ``ForeignKey('modelname')``


Version 0.2.1 (2018-01-02)
------------------------

* Fixed bad packaging of 0.2


Version 0.2 (2018-01-02)
------------------------

* Support more Python versions (removed f-strings)


version 0.1 (2017-12-07)
------------------------

* Initial version
