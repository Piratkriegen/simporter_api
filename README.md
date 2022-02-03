# Data analysis
- Document here the project: simporter_api
- Description: API developed as a test to junior data engineer position
- Data Source: Providaded by the company
- Type of work: An API to conect a database to a web-service that plots graphs
  as as time-series.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for simporter_api in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/simporter_api`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "simporter_api"
git remote add origin git@github.com:{group}/simporter_api.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
simporter_api-run
```

# Install

Go to `https://github.com/{group}/simporter_api` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/simporter_api.git
cd simporter_api
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
simporter_api-run
```
