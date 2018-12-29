# Catalog-Web-App
this project is a required project in udacity nanodegree. It is about making website with database and users containing creating json.

## Requirements
in order to run this project you need:
1. [Vagrant](https://www.vagrantup.com/downloads.html) .
2. [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
3. [Vagrant](https://github.com/udacity/fullstack-nanodegree-vm )  provided by udacity.
 
### Database content  
it contain 3 tables:

##### brand table include:
 
| Column        | Type          |
| ------------- |:-------------:|
| id            | integer       |
| name          | text          |
| user_id       | integer       |
 
##### user: 
 
| Column        | Type          |
| ------------- |:-------------:|
| name          | text          |
| email         | text          |
| picture       | text          |
| id            | intege        |
 
##### mackeup_item: 

| Column        | Type          |
| ------------- |:-------------:|
| name          | text          |
| discription   | text          |
| price         | text          |
| type          | text          |
| user_id       | integer       |  
| brand_id      | integer       | 
 
## run
to run the code you first have to open vagrant file as provided by Udacity. Then move this progect folder inside the vagrant folder then  open git bash from there and type 
`vagrant up ` then `vagrant ssh` 
then ` cd /vagrant` , ` cd catalog ` 
then 
 ```bash
   python project.py
```
   then go to http://localhost:5000


 
