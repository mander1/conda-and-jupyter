# install miniconda
conda and jupyter venv setup

https://www.anaconda.com/docs/getting-started/miniconda/main

```sh
mkdir -p ~/minconda3
Invoke-WebRequest -Uri https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -OutFile miniconda.exe
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
Remove-Item -Path ".\miniconda.exe"
```
# setup

```sh
& "C:\Users\$env:username\miniconda3\Scripts\conda" init powershell
& "C:\Users\$env:username\miniconda3\Scripts\activate"
```

# create a new environment

```sh
conda create --name hello python=3.10.0 -y
```

# activate the env

```sh
conda acivate hello
```

# deactivate env

```sh
conda deactivate
```

# get info about env

```sh
conda info
```

# remove env

```sh
conda remove -n hello --all -y
```