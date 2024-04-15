# AKM Documentation

The AKM documentation is realized with GitHub Pages. It is generated from
the markdown files in the ```/Documentation``` directory of this repository.
The static webpage is generated automatically after every PR merged to master
and deployed into a branch called `gh-pages`.


### Dependencies

The static page is generated with:

- [HUGO](https://gohugo.io/)
- [Learn Theme](https://themes.gohugo.io/hugo-theme-learn/)

Please follow the [documentation](https://gohugo.io/documentation/) for installation and further questions around the framework.

### Run the documentation server locally

Once hugo is installed please follow the following steps:

#### Check that HUGO is working:
```
hugo version
```
The following outcome is expected:

```
Hugo Static Site Generator v0.xx.xx ...
```

#### Clone the submodule containing the theme

Run the following git commands to init and fetch the submodules:

```
git submodule init
git submodule update
```

Reference: [Git Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

#### Test locally on your server:

Within the repository

```
hugo server -D -s ./documentation
```

Optional ```-D:``` include draft pages as well. Afterwards, you can access the
page under http://localhost:1313/Automotive_Knowledge_Model/

### Contribute

If you want to contribute, do the following:

1. **Change documentation in ```/documentation```**

1. **Test your changes locally, as described above**

1. **Create Pull Request for review**
