# ipybudget

 <p align="center">
  <img width="256" src="misc/header.png">
</p>

This project aims to provide a library for creating budgets with [Jupyter Lab](https://jupyter.org/).


## How ipybudget works

All calculation is hidden away from the user in the library. By using Jupyter Notebooks the user can now define the budget as a Python data structure. By implementing the different IPython formatting methods, this data will be correctly displayed as a table in the Markdown, HTML and LaTeX output. Between the definitions there is space for additional informations.


## Motivation

I frequently have to create budgets for Art/Movie projects. This normally means to fiddle around with more or less crappy spreadsheet files. This approach is not fundamentally wrong but comes in with major drawbacks:

- _Missing calculation transparency._ Spreadsheet softwares try to somewhat hide the formulas from your view. While this is fine for the most part, you have no central way of changing some calculations. Instead you have to alter _all_ affected cells and just hope, you haven't missed some parts...
- _Collaboration._ Yes, there is plenty Cloud Spreadsheet stuff out there and they work more or less fine. But at least somebody from your team will eventually download the file and then re-uploading a version edited in a Office Suite from the late 90s and very likely disfigure the whole thing beyond recognition. Also there is a certain group of persons which apparently like to randomly alter formulas and or the format.
- _Formatting._ For me this is the single biggest issue with spreadsheet applications. Almost all of my budgets will be submitted as a part of an application for financial support for projects. Therefore a decent appearance is crucial. I've tried multiple times to accomplish this with different softwares and I always failed and just copied all the numbers in some word processing − or more likely in a markdown file and used [pandoc](https://pandoc.org/).
- _Additional content/remarks._ Almost always you will have to add some comprehensive remarks for some of the budget entries which simply wont fit into a spreadsheet file. Thus you'll alway have a separate text file containing the appendix around. To keep both files in sync can be quit hard and annoying.


## Currency

ipybudget uses [Money Package](https://pypi.org/project/money/) throughout the library and uses Euro as the default format. This can be altered by calling the `set_currency` class-method on Entry. Specify the currency by using the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) three-lettered code:

```python
from ipybudget import Entry

Entry.set_currency("USD")
```
