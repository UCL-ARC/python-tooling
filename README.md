# python-tooling
This repository documents common tooling we use in our Python projects in the [Advanced Research Computing center](https://www.ucl.ac.uk/arc/) (ARC) at [UCL](https://www.ucl.ac.uk).
It is designed as a static GitHub pages site.

## Contributing
The website and source pages are publicly available, but contributions are restricted to members and associate members of ARC.

Pages all live in the `pages` sub-directory, and are written in markdown.

To contribute:
1. Create a new branch.
2. Modify an existing page, or create a new one.
3. Open a pull request with changes.
4. Someone who did not contribute to the PR should review it.
5. If approved, the reviewer should merge the PR.
6. If changes requested, the PR author should address the comments, then ask for review again.

### Building locally
1. [Install jekyll](https://jekyllrb.com/docs/installation/)]
2. Run `bundle install` from the root of this repository to install dependencies
3. Run `bundle exec jekyll serve` from the root directory of this repository. This should fire up a local web server and tell you its address. By default the server will automatically refresh the HTML pages if any changes are made to the markdown sources.

See the [jekyll docs](https://jekyllrb.com/docs/) for more info.
