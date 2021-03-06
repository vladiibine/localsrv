===============================
localsrv
===============================

| |docs| |travis| |appveyor| |coveralls| |landscape| |scrutinizer|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/localsrv/badge/?style=flat
    :target: https://readthedocs.org/projects/localsrv
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/vladiibine/localsrv/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/vladiibine/localsrv

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/vladiibine/localsrv?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/vladiibine/localsrv

.. |coveralls| image:: http://img.shields.io/coveralls/vladiibine/localsrv/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/vladiibine/localsrv

.. |landscape| image:: https://landscape.io/github/vladiibine/localsrv/master/landscape.svg?style=flat
    :target: https://landscape.io/github/vladiibine/localsrv/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/django-localsrv.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-localsrv

.. |downloads| image:: http://img.shields.io/pypi/dm/django-localsrv.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-localsrv

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-localsrv.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-localsrv

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-localsrv.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-localsrv

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-localsrv.svg?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/django-localsrv

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/vladiibine/localsrv/master.png?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/vladiibine/localsrv/

**django-localsrv** is a django app that allows you to serve content (files, strings, etc.) at configurable paths, with configurable response HTTP headers.

It's intended as a more useful test server than Python's SimpleHTTPServer, mainly because of the configuration options.

* Free software: MIT license


Installation
============

For the love of mankind, please use virtualenv.

::

    pip install django-localsrv

Then in your settings file of your django project (usually `settings.py`)

::

    INSTALLED_APPS = (
     ...
     'localsrv',
     ...
    )

In your url configuration file (usually `urls.py`) add the root path to where you want to serve the content from

::

  from localsrv import urls as localsrv_urls

  urlpatterns = (
   ...
   # Put this at the end of the list, since it will capture any url beginning with /localsrv
   # You can also use a pattern like r'', and that will match any pattern that wasn't
   # matched by any other pattern. That can get confusing, so it's best to use a namespace
   # like the one in this example
   url(r'^localsrv/', include(localsrv_urls))
  )
  

Additional steps for the eager ones
===================================
The app includes a simple settings file, that you can use to start using the app instantly. It's the module **localsrv.test_settings**

Let's use it!
This app contains models, so we'll need to run migrations for our app

::

    django-admin.py migrate --settings=localsrv.settings
    
This will create a sqlite database file in directory where the package was installed. If you don't have a problem with that, 
you will be able to start the server now, and enjoy the app. If you want to integrate the app into some project of yours,
though I advise against it, you can do so. I won't teach you how, but it's a simple matter of including 'localsrv' in the 
INSTALLED_APPS list of the settings file of your project.

Create a superuser, to access the admin web console:

::

    django-admin.py createsuperuser --settings=localsrv.test_settings
    
And then run the server:

::

    django-admin.py runserver 0:8989 --settings=localsrv.test_settings

Now you're ready to start configuring what content you're going to serve at the url /localsrv/

Specifying the content to serve
===============================
Since this is a django app, if you did all the above steps (setting the app as a member of the INSTALLED_APPS list is the important thing),
you'll, you'll have access to the `Localsrv` entry on your django admin page.

Working on a simpler, command line interface to the app, with perhaps a simple configuration dictionary.

Things to know: there are at the moment 3 types of content that you can serve:

 + Strings
 + Content found at another URL
 + Files on the local file system (these are a little buggy at the moment, but still usable)

To serve any of these, you need to create their corresponding resources. These are called `String Source`, `URL Source` and `File Source`.
You'll find all of these on the admin page, in the entry for the app `Localsrv`. Try to create a `String Source`, and specify the content
to be this JSON for example (you can use any string you wish, of course)

.. code-block:: json

    {
        "asdf": "zxcv",
        "qwer": [1, 2, 3]
    }

Also, along with the content, you can specify what additional HTTP Headers should be provided. Specifying these is easy. You must create
a `Servable Http Header`, where you'll be prompted for a name (e.g. **content-type**) and a value (e.g. **application/json**)


Now finally, you'll need to specify where to serve your content. This is done by creating a `Servable Content` object, on the same admin page.
For it, you'll use a source that you defined previously, and (optionally) a header that you also defined. You'll also have to specify a path
to serve this content from.

Since in this example we introduced the url pattern `r'^localsrv/`, let's stick to this pattern and specify a path of `/localsrv/my_json`.
The path you choose here can be anything (that ca be considered a URL). We namespaced the url with `/localsrv/` just to avoid any collisions
with previous url pattern. The way `localsrv` handles requests is that it will respond to any unmatched URL, that starts with the namespace
provided, so in our example **/localsrv/asdaf/4/foo/bar** will match the `localsrv` urls, and will return either a 404, or some content
that you defined for this path.

Finally, when accessing the URLs you configred (in our example `/localsrv/my_json`) you'll see your json string delivered with the proper
content type header.


Development
===========

To run the all tests run::

    tox
