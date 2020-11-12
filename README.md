# QueersInCrisis

Team: (Our names go here, probably)

## About

This repository contains the product build for the Crisis Resources Page
challenge at the 2020 oSTEM Hackathon.
Our product builds an interactive map of crisis resources from
a CSV file.

## Dependencies

This code uses Python 3 and relies on the `plotly` dependency.

```
conda install -c plotly plotly
```

## Site Rendering

The test site is rendered on GitHub pages.

The base website code was built using the source from the current
[oSTEM Crisis Hotlines](https://ostem.org/page/crisis-hotlines).

The original contrast errors flagged by the [WAVE](https://wave.webaim.org/)
extension were fixed in a `<style>` block based on the values in the referenced
`WhiteSkyBlue`[stylesheet](https://globalassets.azureedge.net/templates/Portal-B4/Impression/S4-WhiteSkyBlue.min.css?_=637401814753747732).

The `navbar` links were modified from relative links to absolute links for the
demo.

`plotly2html.py` takes the rendered plotly figure and renders a standalone
HTML division.
This division is embedded into a responsive section via an iframe.

## Additional Information on Web Accessibility

- [Color Oracle - Color Blindness Simulator](https://colororacle.org/)
- [Who Can Use -- color guidelines](https://whocanuse.com/)
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [WAVE Browser Extension (works on local test site)](https://wave.webaim.org/extension/)
- [Web AIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
