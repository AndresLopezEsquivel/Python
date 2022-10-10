## To list the existing environments

To list the existing environments, use

```console
conda env list
```

## To create a new environment

To create a new environment, use

```console
conda create --name <env-name> <dependecies=version>
```

Check the following example:

```console
conda create --name py35 python=3.5 pandas
```

If version is not specified (as with pandas), then the latest will be used

## To activate an environment

To activate a certain evironment, run

```console
conda activate <env-name>
```

## To deactivate an environment

To deactivate the current environment, run

```console
conda deactivate
```

## To list the installed dependencies

To list **all** the installed dependencies (with their versions) in the current environment, run

```console
conda list
```

However, to filter the list of dependencies and get the one you are interested in, run

```console
conda list <dependency-name>
```

An example is

```console
conda list pandas
```

## To update a dependency

To update a dependency, run

```console
conda update <dependency-name>
```

For example

```console
conda update pandas
```

## To install a certain version of a dependency

To install a certain version of a dependency, run

```console
conda install <dependency-name=version>
```

For example

```console
conda install python=3.9 pandas=1.2
```

## To clone an old one

To clone an old one, run

```console
conda create --name <new_dependency_name> --copy --clone <old_dependency_name>
```

For example

```console
conda create --name py39 --copy --clone py35
```

## To remove a dependency

To remove a dependency, run:

```console
conda remove <dependency-name>
```

For example

```console
conda remove pandas
```

## To remove an environment

To remove a certain environment, run

```console
conda env remove --name <env-name>
```

For example

```console
conda env remove --name py39
```

Note: It is not possible to remove an active virtual environment. You need to deactivate it and then remove it.