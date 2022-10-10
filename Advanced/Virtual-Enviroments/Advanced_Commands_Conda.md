## Install a certain dependency using a channel

To install a dependency through a channel, run

```console
conda install --channel <chanel-name> <dependency-name>
```

For example

```console
conda install --channel conda-forge boltons
```

## To list revisions

You can track the activity in your virtual environment. To do it, run

```console
conda list revision
```

## To return to a previous number of revision

To return to a previous number of revision, run

```console
conda install --revision <number-of-revision>
```

## To export the dependencies of a virtual environment

To export the installed dependencies, run

```console
conda env export
```

You can also run

```console
conda env export --from-history
```

```console
conda env export --no-builds
```

To create a file containing the installed dependencies, run

```console
conda env export --from-history --file file_name.yml
```

## To create an environment from a specified file

```console
conda env create --file file_name.yml
```