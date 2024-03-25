---
title: Continuous integration
layout: default
---

# Continuous integration (CI)

| Name                                                                                  | Short description                                                                                                                                   | 🚦  |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [GitHub Actions](https://docs.github.com/en/actions)                                  | Continuous integration and continuous delivery platform (integrated with GitHub).                                                                   | 🟢  |
| [AppVeyor](https://www.appveyor.com/docs/)                                            | Continuous integration and continuous delivery platform.                                                                                            | 🟠  |
| [Bamboo](https://confluence.atlassian.com/bamboo/bamboo-documentation-289276551.html) | Atlassian continuous integration and continuous delivery platform.                                                                                  | 🟠  |
| [Travis CI](https://docs.travis-ci.com/)                                              | Continuous integration and continuous delivery platform.                                                                                            | 🟠  |
| [pre-commmit.ci](https://pre-commit.ci/)                                              | A bot that adds a pre-commit job to your GitHub Actions CI, and can automatically fix most trivial linting failures. Free for open-source projects. | 🟢  |

<details>
<summary> 🟢 explanation</summary>
We have many projects using GitHub CI and, it has good integration with GitHub itself, and is free for public repositories (with limited free monthly minutes for private repositories).
</details>

# Coverage monitoring

These services report and track test code coverage over time.
They render the code with highlighting to show which lines are not executed by tests.
See [testing](testing) for our recommendations on packages to generate code coverage during tests.

| Name                                     | Short description                                                                                                                                                                                                                                                                      | 🚦  |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [Codecov](https://docs.codecov.com/docs) | Hosted service to report code coverage metrics. Occasionally slow to update after a report is updated, can be configured to add extra CI checks. This service is probably more widely used and is [free for both open-source and private projects](https://about.codecov.io/pricing/). | 🟢  |
| [Coveralls](https://docs.coveralls.io/)  | Hosted service to report code coverage metrics. Very similar to codecov and we don't strongly recommend one over the other. This service is only [free for open-source projects](https://coveralls.io/pricing).                                                                        | 🟢  |

<details>
<summary> 🟢 explanation</summary>
Both services are similar, so both 🟢.
</details>
