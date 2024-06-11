# NYTSL 2024 Spring Workshop

This workshop uses the development version of arklet-frick ([https://github.com/frickdahl/arklet-frick][1]).

To install this repository, download the code ZIP or clone the repository. `cd` to the repository using your computer's command line. Make sure you have Python 3.9 or greater and Docker installed on your computer. 

Use `docker-compose up` to automatically launch the Postgres database, the arklet-minter component, and the arklet-resolver component. By default, the minter runs on 127.0.0.1:8001 and the resolver runs on 127.0.0.1:8000.

To properly set up the application, create the first user with admin privileges from the command line. 

`make dev-cmd`

…launches a bash shell in the minter container.

`./manage.py createsuperuser`

…creates the superuser.

### Docker

If you don't have Docker, you can download the latest Docker desktop client at [https://www.docker.com/products/docker-desktop/][2]

### Python 

If you're having issues with your Python installation, it's best to create a new virtual environment and use Python 3.11. A simple guide on how to do this is here: [https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/][3]

### Data

This workshop focuses on modeling and linking related resources. I recommend selecting a handful of resources and an ontology. Sample data can be found in `ui/data/`. 

To prepare for the workshop, duplicate `ui/data/entity.csv` and fill in the corresponding fields for each resource.

From an ontology, select a few entity classes and a few entity properties.

For instance, the sample data uses [https://www.cidoc-crm.org/html/cidoc\_crm\_v7.1.3.html#E78][4] as an entity class and [https://www.cidoc-crm.org/html/cidoc\_crm\_v7.1.3.html#P92][5] as a property.

I recommend copying the classes and properties you plan to use into a Word document or text file for reference during the workshop.

### Code

The static site generator is maintained as a Google Colab notebook at this link: [https://colab.research.google.com/drive/1bT5MpcDFoYSUYSDrOZVDL8smoTvrM9rV?usp=sharing][6]

To use the code, you'll need to copy it to your local Drive. You can also download the notebook to use locally. 

(Access to the notebook will open on the morning of the workshop.)

### License

This code is licensed with the MIT open-source license.

[1]:	https://github.com/frickdahl/arklet-frick
[2]:	https://www.docker.com/products/docker-desktop/
[3]:	https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
[4]:	https://www.cidoc-crm.org/html/cidoc_crm_v7.1.3.html#E78
[5]:	https://www.cidoc-crm.org/html/cidoc_crm_v7.1.3.html#P92
[6]:	https://colab.research.google.com/drive/1bT5MpcDFoYSUYSDrOZVDL8smoTvrM9rV?usp=sharing
