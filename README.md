# SoundSource
SoundSource is a web application for storing and searching through audio mixes.
_______________

<img width="1156" alt="Screenshot 2021-06-16 at 16 38 20" src="https://user-images.githubusercontent.com/78811642/122252555-59795300-cec3-11eb-9832-22dd26b95dea.png">

______________________

Hosts can add/edit/delete mixes as well as add/edit/delete sources (DJs).
________________________

<img width="1023" alt="Screenshot 2021-06-16 at 16 40 23" src="https://user-images.githubusercontent.com/78811642/122252875-95acb380-cec3-11eb-8e6d-07f768cd966c.png">

________________________

Users can search mixes by genre or source and save mixes to their MySource index.
________________________

<img width="1154" alt="Screenshot 2021-06-16 at 16 39 34" src="https://user-images.githubusercontent.com/78811642/122253018-b5dc7280-cec3-11eb-8471-87437a2db536.png">

___________________________
SETUP
------

Clone down this repository

Install dependencies:

     pip3 install flask
     pip3 install psycopg2
     pip3 install psycopg2-binary
    
Create a sound_source database on your local machine:

     createdb sound_source
    
cd into /project1/db and run the sql file:

     psql -d sound_source -f sound_source.sql
    
Run the console.py file to populate the app with mixes or simply run flask to start with a blank slate.

     python3 console.py
     flask run
___________________________________________________

Project Brief:
-----

Hosts should be able to:

- add a new mix and create a new source (DJ).
 
- edit and delete mixes and sources.
 
Users should be able to:

- view a list of all mixes
 
- view a list of all sources.
 
- view all mixes from a selected source. 
 
- view all mixes in a selected genre.
 
- view a single mix with a description, tracklist and audio link.


### Completed Extensions:

- Users are able to add and delete mixes from their personal MySource index.

- Genres are added only when unique.

- Genres have an associated color theme, which carries through the app.


### Possible Additional Extensions:

- Access to add/edit/delete mixes and sources should be limited to the host.

- Some mixes may have more than one source (many to many).

- Users can request a new mix either by source or by genre, and pay for the mix.

- Users could be able to rate mixes. 

- There could be a button that picks a random mix for the user.
______________________________________

Inspired By::
Mixcloud
