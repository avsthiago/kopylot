# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/avsthiago/kopylot/issues>

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with \"bug\"
and \"help wanted\" is open to whoever wants to implement a fix for it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
\"enhancement\" and \"help wanted\" is open to whoever wants to
implement it.

### Write Documentation

Cookiecutter PyPackage could always use more documentation, whether as
part of the official docs, in docstrings, or even on the web in blog
posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/avsthiago/kopylot/issues>.

If you are proposing a new feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here\'s how to set up [kopylot]{.title-ref} for
local development. Please note this documentation assumes you already
have [poetry]{.title-ref} and [Git]{.title-ref} installed and ready to
go.

| 1. Fork the [kopylot]{.title-ref} repo on GitHub.

| 2. Clone your fork locally:

> ``` bash
> cd <directory_in_which_repo_should_be_created>
> git clone git@github.com:YOUR_NAME/kopylot.git
> ```

| 3. Now we need to install the environment. Navigate into the directory

> ``` bash
> cd kopylot
> ```
>
> If you are using `pyenv`, select a version to use locally. (See
> installed versions with `pyenv versions`)
>
> ``` bash
> pyenv local <x.y.z>
> ```
>
> NOTE: later on, to be able to run the `tox` command with 4 different
> versions, a set-up may be needed where python 3.8.x, 3.9.x, 3.10.x and
> 3.11.x are needed. A possible approach is described below. For now,
> just setting a pyenv local to a proper version (e.g. 3.11) is enough.
>
> Then, install the environment with:
>
> ``` bash
> make install
> ```
>
> This will run the poetry install and also install the pre-commit.
>

| 4. Create a branch for local development:

> ``` bash
> git checkout -b name-of-your-bugfix-or-feature
> ```
>
> Now you can make your changes locally.

| 5. Do not forget to add test cases for your added functionality to the
  `tests` directory.
> You can run the tests with
> ``` bash
> make test
> ```

| 6. When you are done making changes, check that your changes pass the
  formatting checks.

> ``` bash
> make check
> ```

| 7. Now, validate that all unit tests are passing:

> ``` bash
> make test
> ```

| 8. Before raising a pull request you should also run tox. This will
  run the tests across different versions of Python:

> Running tox for the different python versions involves some complexity.
> This requires you to have multiple versions of python installed. This
> step is also triggered in the CI/CD pipeline, so you could also choose
> to skip this step locally.
>
> If you want to run it locally, one possible way to do this is:
>
> ```bash
> pyenv install 3.8
> pyenv install 3.9
> pyenv install 3.10
> pyenv install 3.11
> ```
>
> In the command below, replace the `x` by the exact versions that where
> installed by the 4 commands (or see which pyenv versions are installed with
> `pyenv versions`.
>
> Also, the order of the versions is important. The first version in the list
> will be the default version selected by poetry install if the setting
> `virtualenvs.prefer-active-python = true` is set. So, set your preferred
> Python version as first argument to `pyenv global`.
>
> ``` bash
> pyenv global 3.11.x 3.10.x 3.9.x 3.8.x
> ```
>
> NOTE: to run tox successfully, there should _not_ be a `.python-version` file present.
> That `.python-version` may have been created by the `pyenv local <x.y.z>` command
> in the step 3 above. You have to remove it again to run tox successfully for
> all versions. When the .python-version is present, the errors reported by
> tox are:
>
> ``` bash
> py38 recreate: .../kopylot/.tox/py38
> ERROR: InterpreterNotFound: python3.8
> py39 recreate: .../kopylot/.tox/py39
> ERROR: InterpreterNotFound: python3.9
> ```
>
> A validation that all python versions are present and callable could be:
>
> ```bash
> python3.8 -V  # => Python 3.8.16
> python3.9 -V  # => Python 3.9.16
> python3.10 -V  # => Python 3.10.11
> python3.11 -V  # => Python 3.11.3
> ```
>
> After this preparation and validation, tox should run the tests successfully on all
> python versions.
>
> ``` bash
> poetry run tox
> ```
>

| 9. Commit your changes and push your branch to GitHub:

> ``` bash
> git add .
> git commit -m "Your detailed description of your changes."
> git push origin name-of-your-bugfix-or-feature
> ```

| 10. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
