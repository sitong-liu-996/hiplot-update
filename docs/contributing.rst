.. _contributing:

Building HiPlot from source
==========================

Python developer setup
--------------------------

It is not necessary to build the Javascript bundle when developing the python side of HiPlot. However, the generated bundle (:code:`hiplot/static/built/hiplot.bundle.js`) is not
provided in the git repository. The easiest solution is to download the latest version generated by the CI: :download:`hiplot.bundle.js <../hiplot/static/built/hiplot.bundle.js>`

Building Javascript bundle
--------------------------

HiPlot's frontend is built with React in TypeScript.
Those files need to be compiled and bundled into plain Javascript to generate :code:`hiplot.bundle.js`.
Node/npm is required in order to build those files

.. code-block:: bash

    # First, install npm packages
    npm install
    # Then either:
    # (1) Dev (recommended): automatically re-build when a change is detected
    npm run build-dev-watch
    # (2) Build in release mode (for better performance)
    npm run webpack-dev-watch


It's also recommended to run a HiPlot server locally to experiment:

.. code-block:: bash

    pip install -e .
    python -m hiplot --dev

Now open your browser and play with the code :)

.. warning::

    Do not forget to refresh the page and clear the cache when changing javascript files (for Chrome: :code:`CMD+SHIFT+R` on MacOS, or :code:`CTRL+SHIFT+R` on Windows).


Building documentation
--------------------------

.. code-block:: bash

    pip install -r requirements/dev.txt
    cd docs
    make html
