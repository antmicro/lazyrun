# lazyrun

Lazyrun is a utility to run various useful tools in containers as if they were
installed natively.

## Installation

Lazyrun uses [Podman](https://podman.io/) under the hood for rootless, deamonless containers.
Unfortunately the official [static build docs don't work](https://podman.io/getting-started/installation#static-build) - we should most likely suggest a fix.

But you can get Podman as a static binary e.g. [from its official CI](https://cirrus-ci.com/task/5125306349518848).

You also need to add the `apps/` directory to your path.

## TODO

* [X] sbt PoC
* [ ] turn sbt into a more sensible container (no weird paths)
* [X] move from scripts to config
* [ ] include static podman in releases
* [ ] ability to turn apps on or off
* [ ] overlays over default list - or list of lists
