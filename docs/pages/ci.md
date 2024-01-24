---
title: CI
layout: default
---

# Continuous integration

| Name                                                                                  | Short description                                                                 | 🚦  |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | :-: |
| [GitHub Actions](https://docs.github.com/en/actions)                                  | Continuous integration and continuous delivery platform (integrated with GitHub). | 🟢  |
| [AppVeyor](https://www.appveyor.com/docs/)                                            | Continuous integration and continuous delivery platform.                          | 🟠  |
| [Bamboo](https://confluence.atlassian.com/bamboo/bamboo-documentation-289276551.html) | Atlassian continuous integration and continuous delivery platform.                | 🟠  |
| [Travis CI](https://docs.travis-ci.com/)                                              | Continuous integration and continuous delivery platform.                          | 🟠  |

<details>
<summary> 🟢 explanation</summary>
We have many projects using github CI, it's both convenient and works well. It's become the standard. Also, note that it's free for public repos.
</details>

# Coverage monitoring

You can check coverage simply in the terminal with the
[pytest-cov](https://pypi.org/project/pytest-cov/) plugin. However you might
consider a third-party code coverage analytics and reporting service. There are
two that we've used and they're both rather similar. They render the code with
highlighting to show which lines are not executed but the tests, and can track
test coverage over time.

| Name                                     | Short description                                                                                                                                | 🚦  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | :-: |
| [Codecov](https://docs.codecov.com/docs) | Hosted service to report code coverage metrics. Occasionally slow to update after a report is updated, can be configured to add extra CI checks. | 🟠  |
| [Coveralls](https://docs.coveralls.io/)  | Hosted service to report code coverage metrics. Very similar to codecov we don't recommend one over the other.                                   | 🟠  |
