# lazyrun

Lazyrun is a utility to run various useful tools in containers as if they were installed natively.

## Installation

To get lazyrun, for now just clone this repository:

```
git clone https://github.com/antmicro/lazyrun
```

Lazyrun uses [Podman](https://podman.io/) under the hood for rootless, deamonless containers. Docker can also be used as a replacement.
See [the official Podman docs](https://podman.io/getting-started/installation) for installation instructions.

Basically, lazyrun itself will tell you if you don't have Podman and how to get it in that case.

TODO: our own fully static container tech.

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
Static binaries are also built on every commit [GitHub Actions](https://github.com/antmicro/lazyrun/actions).

## Running lazyrun

Just do:

```
lazyrun
```

And follow the guidelines - you will need to:

```
source ./lazyrun/init
```

And you should now see the relevant containerized binaries on your PATH.
