<!-- markdownlint-disable MD041 -->
<div style="text-align: center;" align="center">
  <img src="https://raw.githubusercontent.com/UCL-ARC/python-tooling/main/images/logo.svg" alt="UCL ARC Python tooling logo" width="120"/>
  <h1> UCL ARC Python Recommendations</h1>
</div>
<!-- markdownlint-restore -->

This repository collects our recommendations for a research software project in Python.
We have a [website], if you just need some advice, and a template if you're starting from scratch.

🍪 Our template uses [cookiecutter] to set up a new package with our preferred tools ready to go.

> [!NOTE]
> If you're making a package in research community that already has a template, use theirs instead!

## How to use our template

If you're comfortable with the command line, here are some quick start steps.
We also have a more detailed [tutorial](./tutorial.md) that has been presented in workshops for researchers at UCL.

If you have [uv] installed, run:

```sh
uvx cookiecutter gh:ucl-arc/python-tooling --checkout latest
```

If you don't want to use uv you can [install cookiecutter], then run without `uvx`:

```sh
cookiecutter gh:ucl-arc/python-tooling --checkout latest
```

[Cookiecutter] will ask you questions to set up your project.
Type your answer, or hit return without typing anything to use the defaults.

When finished, it prints some information to the terminal.
These are tips for next steps like creating a repository and making a website for your package.

It will have created a directory for your project:

```sh
ls -ltr | tail -n1 # Show the last directory that was created
```

You can see the structure with the `tree` command.
In our example we've called our project `example-research-software-project`:

```sh
tree example-research-software-project
```

To start working on your project:

- change directory to your project directory,
- initialise a `git` repository,
- and _install_ your new package editable mode.

You probably want to do this in a [virtual environment](./docs/pages/virtual.md).
The comments show how to do this in [uv] with `uv venv`:

```sh
cd example-research-software-project
git init
# uv venv
# source .venv/bin/activate
uv sync
```

## Need help?

You can ask questions in [discussions] or in the `#helpme` channel on UCL's [Research Programming Hub Slack].

<!-- links here -->

<!-- prettier-ignore-start -->
[website]: https://github-pages.arc.ucl.ac.uk/python-tooling
[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable
[install cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/README.html#installation
[uv]: https://docs.astral.sh/uv
[discussions]: https://github.com/UCL-ARC/python-tooling/discussions
[Research Programming Hub Slack]: https://www.ucl.ac.uk/advanced-research-computing/community/ucl-research-programming-hub
<!-- prettier-ignore-end -->

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://paddyroddy.github.io"><img src="https://avatars.githubusercontent.com/u/15052188?v=4?s=100" width="100px;" alt="Patrick J. Roddy"/><br /><sub><b>Patrick J. Roddy</b></sub></a><br /><a href="#ideas-paddyroddy" title="Ideas, Planning, & Feedback">🤔</a> <a href="#bug-paddyroddy" title="Bug reports">🐛</a> <a href="#code-paddyroddy" title="Code">💻</a> <a href="#content-paddyroddy" title="Content">🖋</a> <a href="#doc-paddyroddy" title="Documentation">📖</a> <a href="#eventOrganizing-paddyroddy" title="Event Organizing">📋</a> <a href="#projectManagement-paddyroddy" title="Project Management">📆</a> <a href="#question-paddyroddy" title="Answering Questions">💬</a> <a href="#review-paddyroddy" title="Reviewed Pull Requests">👀</a> <a href="#talk-paddyroddy" title="Talks">📢</a> <a href="#test-paddyroddy" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://scnlf.me"><img src="https://avatars.githubusercontent.com/u/1836192?v=4?s=100" width="100px;" alt="Sam Cunliffe"/><br /><sub><b>Sam Cunliffe</b></sub></a><br /><a href="#ideas-samcunliffe" title="Ideas, Planning, & Feedback">🤔</a> <a href="#bug-samcunliffe" title="Bug reports">🐛</a> <a href="#code-samcunliffe" title="Code">💻</a> <a href="#content-samcunliffe" title="Content">🖋</a> <a href="#doc-samcunliffe" title="Documentation">📖</a> <a href="#eventOrganizing-samcunliffe" title="Event Organizing">📋</a> <a href="#projectManagement-samcunliffe" title="Project Management">📆</a> <a href="#question-samcunliffe" title="Answering Questions">💬</a> <a href="#review-samcunliffe" title="Reviewed Pull Requests">👀</a> <a href="#talk-samcunliffe" title="Talks">📢</a> <a href="#test-samcunliffe" title="Tests">⚠️</a> <a href="#tutorial-samcunliffe" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.davidstansby.com"><img src="https://avatars.githubusercontent.com/u/6197628?v=4?s=100" width="100px;" alt="David Stansby"/><br /><sub><b>David Stansby</b></sub></a><br /><a href="#ideas-dstansby" title="Ideas, Planning, & Feedback">🤔</a> <a href="#bug-dstansby" title="Bug reports">🐛</a> <a href="#code-dstansby" title="Code">💻</a> <a href="#content-dstansby" title="Content">🖋</a> <a href="#doc-dstansby" title="Documentation">📖</a> <a href="#eventOrganizing-dstansby" title="Event Organizing">📋</a> <a href="#projectManagement-dstansby" title="Project Management">📆</a> <a href="#review-dstansby" title="Reviewed Pull Requests">👀</a> <a href="#test-dstansby" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://matt-graham.github.io"><img src="https://avatars.githubusercontent.com/u/6746980?v=4?s=100" width="100px;" alt="Matt Graham"/><br /><sub><b>Matt Graham</b></sub></a><br /><a href="#bug-matt-graham" title="Bug reports">🐛</a> <a href="#code-matt-graham" title="Code">💻</a> <a href="#content-matt-graham" title="Content">🖋</a> <a href="#doc-matt-graham" title="Documentation">📖</a> <a href="#design-matt-graham" title="Design">🎨</a> <a href="#eventOrganizing-matt-graham" title="Event Organizing">📋</a> <a href="#review-matt-graham" title="Reviewed Pull Requests">👀</a> <a href="#talk-matt-graham" title="Talks">📢</a> <a href="#test-matt-graham" title="Tests">⚠️</a> <a href="#tutorial-matt-graham" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sfmig"><img src="https://avatars.githubusercontent.com/u/33267254?v=4?s=100" width="100px;" alt="sfmig"/><br /><sub><b>sfmig</b></sub></a><br /><a href="#bug-sfmig" title="Bug reports">🐛</a> <a href="#code-sfmig" title="Code">💻</a> <a href="#content-sfmig" title="Content">🖋</a> <a href="#review-sfmig" title="Reviewed Pull Requests">👀</a> <a href="#test-sfmig" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/p-j-smith"><img src="https://avatars.githubusercontent.com/u/29753790?v=4?s=100" width="100px;" alt="Paul Smith"/><br /><sub><b>Paul Smith</b></sub></a><br /><a href="#bug-p-j-smith" title="Bug reports">🐛</a> <a href="#code-p-j-smith" title="Code">💻</a> <a href="#content-p-j-smith" title="Content">🖋</a> <a href="#doc-p-j-smith" title="Documentation">📖</a> <a href="#question-p-j-smith" title="Answering Questions">💬</a> <a href="#review-p-j-smith" title="Reviewed Pull Requests">👀</a> <a href="#test-p-j-smith" title="Tests">⚠️</a> <a href="#tutorial-p-j-smith" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://docs.renovatebot.com/"><img src="https://avatars.githubusercontent.com/u/38656520?v=4?s=100" width="100px;" alt="Renovate Bot"/><br /><sub><b>Renovate Bot</b></sub></a><br /><a href="#maintenance-renovatebot" title="Maintenance">🚧</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ruaridhg"><img src="https://avatars.githubusercontent.com/u/32329546?v=4?s=100" width="100px;" alt="ruaridhg"/><br /><sub><b>ruaridhg</b></sub></a><br /><a href="#bug-ruaridhg" title="Bug reports">🐛</a> <a href="#code-ruaridhg" title="Code">💻</a> <a href="#content-ruaridhg" title="Content">🖋</a> <a href="#review-ruaridhg" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://mxochicale.github.io/"><img src="https://avatars.githubusercontent.com/u/11370681?v=4?s=100" width="100px;" alt="Miguel Xochicale, PhD"/><br /><sub><b>Miguel Xochicale, PhD</b></sub></a><br /><a href="#bug-mxochicale" title="Bug reports">🐛</a> <a href="#code-mxochicale" title="Code">💻</a> <a href="#content-mxochicale" title="Content">🖋</a> <a href="#design-mxochicale" title="Design">🎨</a> <a href="#doc-mxochicale" title="Documentation">📖</a> <a href="#review-mxochicale" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yidilozdemir"><img src="https://avatars.githubusercontent.com/u/30597301?v=4?s=100" width="100px;" alt="yidilozdemir"/><br /><sub><b>yidilozdemir</b></sub></a><br /><a href="#doc-yidilozdemir" title="Documentation">📖</a> <a href="#test-yidilozdemir" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://giordano.github.io"><img src="https://avatars.githubusercontent.com/u/765740?v=4?s=100" width="100px;" alt="Mosè Giordano"/><br /><sub><b>Mosè Giordano</b></sub></a><br /><a href="#bug-giordano" title="Bug reports">🐛</a> <a href="#doc-giordano" title="Documentation">📖</a> <a href="#review-giordano" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://t-young31.github.io"><img src="https://avatars.githubusercontent.com/u/39765193?v=4?s=100" width="100px;" alt="Tom Young"/><br /><sub><b>Tom Young</b></sub></a><br /><a href="#bug-t-young31" title="Bug reports">🐛</a> <a href="#content-t-young31" title="Content">🖋</a> <a href="#review-t-young31" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/alessandrofelder"><img src="https://avatars.githubusercontent.com/u/10500965?v=4?s=100" width="100px;" alt="Alessandro Felder"/><br /><sub><b>Alessandro Felder</b></sub></a><br /><a href="#bug-alessandrofelder" title="Bug reports">🐛</a> <a href="#content-alessandrofelder" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://adamltyson.com"><img src="https://avatars.githubusercontent.com/u/13147259?v=4?s=100" width="100px;" alt="Adam Tyson"/><br /><sub><b>Adam Tyson</b></sub></a><br /><a href="#content-adamltyson" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://willgraham01.github.io/"><img src="https://avatars.githubusercontent.com/u/32364977?v=4?s=100" width="100px;" alt="Will Graham"/><br /><sub><b>Will Graham</b></sub></a><br /><a href="#content-willGraham01" title="Content">🖋</a> <a href="#review-willGraham01" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nikk-nikaznan"><img src="https://avatars.githubusercontent.com/u/48319650?v=4?s=100" width="100px;" alt="nikk-nikaznan"/><br /><sub><b>nikk-nikaznan</b></sub></a><br /><a href="#content-nikk-nikaznan" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/katiebuntic"><img src="https://avatars.githubusercontent.com/u/96536608?v=4?s=100" width="100px;" alt="Katie Buntic"/><br /><sub><b>Katie Buntic</b></sub></a><br /><a href="#content-katiebuntic" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/robertvi"><img src="https://avatars.githubusercontent.com/u/456100?v=4?s=100" width="100px;" alt="Robert Vickerstaff"/><br /><sub><b>Robert Vickerstaff</b></sub></a><br /><a href="#doc-robertvi" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://dpshelio.github.io"><img src="https://avatars.githubusercontent.com/u/963242?v=4?s=100" width="100px;" alt="David Pérez-Suárez"/><br /><sub><b>David Pérez-Suárez</b></sub></a><br /><a href="#code-dpshelio" title="Code">💻</a> <a href="#question-dpshelio" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LLapira"><img src="https://avatars.githubusercontent.com/u/48060852?v=4?s=100" width="100px;" alt="llapira"/><br /><sub><b>llapira</b></sub></a><br /><a href="#bug-llapira" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://pre-commit.ci"><img src="https://avatars.githubusercontent.com/u/64617429?v=4?s=100" width="100px;" alt="pre-commit.ci"/><br /><sub><b>pre-commit.ci</b></sub></a><br /><a href="#maintenance-pre-commit-ci" title="Maintenance">🚧</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://saransh-cpp.github.io/"><img src="https://avatars.githubusercontent.com/u/74055102?v=4?s=100" width="100px;" alt="Saransh Chopra"/><br /><sub><b>Saransh Chopra</b></sub></a><br /><a href="#doc-Saransh-cpp" title="Documentation">📖</a> <a href="#content-Saransh-cpp" title="Content">🖋</a> <a href="#maintenance-Saransh-cpp" title="Maintenance">🚧</a> <a href="#review-Saransh-cpp" title="Reviewed Pull Requests">👀</a> <a href="#talk-Saransh-cpp" title="Talks">📢</a> <a href="#tutorial-Saransh-cpp" title="Tutorials">✅</a> <a href="#eventOrganizing-Saransh-cpp" title="Event Organizing">📋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://drandrewmitchell.com"><img src="https://avatars.githubusercontent.com/u/22335636?v=4?s=100" width="100px;" alt="Andrew Mitchell"/><br /><sub><b>Andrew Mitchell</b></sub></a><br /><a href="#bug-MitchellAcoustics" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.ucl.ac.uk/advanced-research-computing/advanced-research-computing-centre"><img src="https://avatars.githubusercontent.com/u/24316371?v=4?s=100" width="100px;" alt="Kimberly Meechan"/><br /><sub><b>Kimberly Meechan</b></sub></a><br /><a href="#bug-K-Meech" title="Bug reports">🐛</a> <a href="#a11y-K-Meech" title="Accessibility">️️️️♿️</a> <a href="#review-K-Meech" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-K-Meech" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jamesprime"><img src="https://avatars.githubusercontent.com/u/17751241?v=4?s=100" width="100px;" alt="James Prime"/><br /><sub><b>James Prime</b></sub></a><br /><a href="#a11y-jamesprime" title="Accessibility">️️️️♿️</a> <a href="#ideas-jamesprime" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cuteshaun"><img src="https://avatars.githubusercontent.com/u/28014041?v=4?s=100" width="100px;" alt="Andrii Tsapko"/><br /><sub><b>Andrii Tsapko</b></sub></a><br /><a href="#a11y-cuteshaun" title="Accessibility">️️️️♿️</a> <a href="#code-cuteshaun" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://james.briant.co.uk"><img src="https://avatars.githubusercontent.com/u/6298711?v=4?s=100" width="100px;" alt="James Briant"/><br /><sub><b>James Briant</b></sub></a><br /><a href="#bug-jamesbriant" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
