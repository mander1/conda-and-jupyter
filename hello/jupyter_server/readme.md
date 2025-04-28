# configuring a jupyter sever using miniconda

# create
```sh
conda create -n serv python=3.10.0 ipykernal -y
```
# install
```sh
conda install -c conda-forge jupyterlab
```
# start
```sh
jupyter lab --no-browser --allow-root -ip 0.0.0.0
```
# install a package
```sh
conda install -c conda-forge jupyterlab-git
```