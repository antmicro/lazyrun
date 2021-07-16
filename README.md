# lazyrun

Lazyrun is a utility to run various useful tools in containers as if they were installed natively.

## Installation

To get lazyrun, for now just clone this repository:

```
git clone https://github.com/antmicro/lazyrun
```

Lazyrun uses [Podman](https://podman.io/) under the hood for rootless, deamonless containers.
Unfortunately the official [static build docs don't work](https://podman.io/getting-started/installation#static-build) - we should most likely suggest a fix.

But you can get Podman as a static binary e.g. [from its official CI](https://cirrus-ci.com/task/5125306349518848) or the releases, so you can do for example:

```
cd lazyrun
mkdir -p .lazyrun && cd .lazyrun
wget https://github.com/antmicro/lazyrun/releases/download/0.1/podman
chmod +x podman
```

## Running lazyrun

Just do:

```
lazyrun
```

And follow the guidelines - if you have podman, you will need to:

```
source ./lazyrun/init
```

And you should now see the relevant binaries on your PATH.

## TODO

* [ ] turn sbt into a more sensible container (no weird paths)
* [ ] dsceribe building static binary and usage thereof
* [ ] investigate simpler path changing solution
