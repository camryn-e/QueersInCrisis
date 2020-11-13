# QueersInCrisis

Team: (Our names go here, probably)

## About

This repository contains the product build for the Crisis Resources Page
[challenge](https://www.notion.so/Crisis-Resources-Page-d47e22f151394101a45ce4e0608ccd4f)
at the 2020 oSTEM Hackathon.
Our product builds an interactive map of crisis resources from
a CSV file.

You can access our presentation on [Google Slides](https://bit.ly/2020-oSTEM-Hack-QIC).

## Dependencies

This code uses Python 3 and relies on the `plotly`, `pandas`, and `csv` dependencies.
The `csv` module is in base python.

`plotly` and `pandas` can be installed using either `conda` or `pip`.
```
conda install -c plotly plotly
conda install pandas
```

```
pip install plotly
pip install pandas
```
## `map2html.py`

`map2html.py` generates an example plotly figure and renders a standalone
HTML page.

## `crisis.py`

`crisis.py` has functions that result in several tabular data approaches:
  1. Generating an interactive HTML [DataTable](https://datatables.net/) from a CSV
  2. Generating an interative HTML DataTable from a public Google Sheet
  3. Generating an interative HTML DataTable from a public Google Sheet and replacing cell text with Font Awesome icons

## `docs/from-current.html`

This file contains the HTML for a working oSTEM test page.
Any additions or modifications to the original crisis page's HTML are marked
in comment blocks following this format:
```
<!-- EML: <Description of what is being done> -->
<!-- EML: End <any parting words> -->
```

## Site Rendering

The test site is rendered on
[GitHub pages](https://camryn-e.github.io/QueersInCrisis/index.html).

The base website code was built using the source from the current
[oSTEM Crisis Hotlines](https://ostem.org/page/crisis-hotlines).

The original contrast errors flagged by the [WAVE](https://wave.webaim.org/)
extension were fixed in a `<style>` block based on the values in the referenced
`WhiteSkyBlue`[stylesheet](https://globalassets.azureedge.net/templates/Portal-B4/Impression/S4-WhiteSkyBlue.min.css?_=637401814753747732).
The biggest adjustments were resetting colors from `#019FCB` to `#0000F5`.
The adjusted elements were only those on the crisis page, so there are likely
more elements to fix from the underlying Bootstrap for the entire oSTEM site.

The `navbar` links were modified from relative links to absolute links for the
demo.

The iFrames can be tested with new HTML sources locally by replacing the GitHub paths to the local `file:///` path.

In addition to adding iFrames for the map and DataTables solutions, a published version of the public Google Sheet
was also embedded.

## Additional Information on Web Accessibility

Each of the individual pages that the iFrames were rendered from were tested using WAVE.
The Plotly map is an accessibility nightmare, and as an iFrame, a Mac computer's VoiceOver will
skip over it entirely.
The DataTables solutions are all accessible, but the FontAwesome variant will not allow searching by icons.

- [Color Oracle - Color Blindness Simulator](https://colororacle.org/)
- [Who Can Use -- color guidelines](https://whocanuse.com/)
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [WAVE Browser Extension (works on local test site)](https://wave.webaim.org/extension/)
- [Web AIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
