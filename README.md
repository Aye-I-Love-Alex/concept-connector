
## Setting up the Development Environment
Its recommended that you install all python dependencies in a virtual environment and then clone inside that environment.

### Virtualenv Insturctions
1. ```pip install virtualenv```
2. ```virtualenv 5914```
3. ```cd 5914```
4. ```git clone concept-connector``` (using SSH or HTTPS)
5.  ```cd concept-conector```
6.  ```pip install -r requirements.txt```

## Running ElasticSearch:
If running for first time:
1. Download ElasticSearch [here](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/getting-started.html#run-elasticsearch) and Docker [here](https://www.docker.com/products/docker-desktop/)
2. Follow self-managed commands to initially run ElasticSearch for Docker [here](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/getting-started.html#run-elasticsearch)
3. Run command to build mapping for ElasticSearch (found commented out in `populateElastic.py`)
4. Add a folder named "graph" in the same directory as the other program files, such as comparator.py and Connection.py. This is where the graphs will be stored after running.

If ElasticSearch has been run in the past:
1. Open Docker Desktop and run container for ElasticSearch

## Running the Parser
### Requirements
* ElasticSearch and Docker installed and functional
* BeautifulSoup python library installed
### Steps
1. Download the simple wikipedia datadump [here](https://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-pages-articles-multistream.xml.bz2)
2. Unzip the compressed datadump with a software like 7zip or winrar, will be 1 GB uncompressed
3. Place the file in the home directory(\concept-connector)
4. Run the following terminal command in the home directory(\concept-connector) % py WikiReader.py

_Estimated runtime is under 5 minutes_

## Running the Frontend
### Requirements
* ElasticSearch and Docker installed and functional
* All python packages from requirements.txt installed in a virtual environment i.e. venv.

```flask --app comparator run```

