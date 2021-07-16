# lazyrun

Lazyrun is a utility to run various useful tools in containers as if they were installed natively.

## Installation

To get lazyrun, for now just clone this repository:

```
git clone https://github.com/antmicro/lazyrun
```

Lazyrun uses [Podman](https://podman.io/) under the hood for rootless, deamonless containers.
Unfortunately the official [static build docs don't work](https://podman.io/getting-started/installation#static-build) - we should most likely suggest a fix.

But you can get Podman as a static binary e.g. [from its official CI](https://cirrus-ci.com/task/5125306349518848) or the [releases](https://github.com/antmicro/lazyrun/releases/download/0.1/podman).

Basically, lazyrun itself will tell you if you don't have Podman and how to
download it in that case.
Preferably, build a static binary from it as outlined below.

### Building a static binary

Run:

```
pip install pyinstaller staticx
```

Then execute:

```
./build.sh
```

And you should see a `lazyrun` binary in your current folder.
Put it somewhere in your PATH.

## Running lazyrun

Just do:

```
lazyrun
```

And follow the guidelines - you will need to:

```
source ./lazyrun/init
```

And you should now see the relevant dockerized binaries on your PATH.

## TODO

* [ ] create CI which produces static binaries
* [ ] turn sbt into a more sensible container (no weird paths)
* [X] describe building static binary and usage thereof
* [ ] investigate simpler path changing solution
