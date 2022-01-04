Contributing
============

Ready15 is living, breating document maintained through community efforts.

If you would like to contribute
but don't know how, you've come to the right place!
Before adding to the documentation,
remember that all members of our community are expected to follow our :doc:`/code_of_conduct`.
Please make sure you are welcoming and friendly in all of our spaces.

Ready15 uses `reStructuredText <https://docutils.sourceforge.io/rst.html>`_ and `Sphinx <https://www.sphinx-doc.org>`_ to generate HTML which is then hosted on `GitHub Pages <https://pages.github.com/>`_ using the `Read the Docs <https://readthedocs.org/>`_ `theme <https://github.com/readthedocs/sphinx_rtd_theme>`_.

Getting started
---------------


First steps
~~~~~~~~~~~
At a minimum, the only things you will need to contribute are a web browser,
an Internet connection, and a GitHub account (you can `register for a free account <https://github.com/signup>`_ if you don't have one).

If you're making small changes to the documentation,
using the :ref:`Github UI <contributing:Contributing through the Github UI>` is the simplest method.
Otherwise, we suggest :ref:`setting up a development environment <contributing:Contributing from your local machine>` on your computer to better verify changes locally before pushing upstream.

Contributing through the GitHub UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you find an error on a page, or would like to make a minor amendment you can verify those changes through the documentation generated when you open a `pull request <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_ and can be accessed using the Github UI.

#. on a Ready15 page, click the :guilabel:`Edit on GitHub` link in the top right corner

#. on the tab that opens, click the pencil icon to the top right of the document. This will `Fork this project and edit the file`

#. make your changes and click the :guilabel:`Propose changes` button

#. review your changes and click :guilabel:`Create pull request` when ready

#. on the pull request page, fill in details about the changes you've made to allow us to better review, and click :guilabel:`Create pull request` when ready

#. your pull request has been created and one of the Ready15 maintainers will review your changes. When accepted, a maintainer will merge, and the website will be automatically updated!

Contributing from your local machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're making large changes to the documentation,
you may want to verify those changes locally before pushing upstream.

#. clone the `ready15.com` repository:

   .. code-block:: console

      $ git clone --recurse-submodules https://github.com/RhysDeimel/ready15.git

#. create a virtual environment with Python 3.9, activate it, and upgrade pip:

   .. code-block:: console

      $ cd ready15.com
      $ python3.9 -m venv .venv
      $ source .venv/bin/activate
      (.venv) $ python -m pip install -U pip

#. install documentation requirements

   .. code-block:: console

      (.venv) $ pip install -r docs/requirements.txt

#. build and display the documents

   .. code-block:: console

      (.venv) $ cd docs
      (.venv) $ make livehtml

#. the documents will be available at http://127.0.0.1:8000/ and will rebuild each time you edit and save a file.

Guidelines
----------

Please follow these guidelines when updating our docs.
Let us know if you have any questions or something isn't clear.

The optimal section length is `7 minutes <https://medium.com/data-lab/the-optimal-post-is-7-minutes-74b9f41509b>`_. This equates to 1400~1750 words. If a page exceeds this, consider breaking it into multiple pages.

For page titles, or Heading1 as they are sometimes called, we use title-case.

If the page includes multiple sub-headings (H2, H3),
we usually use sentence-case unless the titles include terminology that is supposed to be capitalized.


* Do not break the content across multiple lines at 80 characters,
  but rather break them on semantic meaning (e.g. periods or commas).
  Read more about this `here <https://rhodesmill.org/brandon/2012/one-sentence-per-line/>`_.
* If you are cross-referencing to a different page within our website,
  use the ``doc`` role and not a hyperlink.
* If you are cross-referencing to a section within our website,
  use the ``ref`` role with the label from the `autosectionlabel extension <http://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html>`__.


Where to go from here
---------------------

This is the end of the contribution page.

Here you have some resources to continue learning about documentation
and Ready15:

- To make the most of the documentation generator you can read the `Sphinx tutorial <https://www.sphinx-doc.org/en/master/tutorial/index.html>`_.

Happy documenting!
