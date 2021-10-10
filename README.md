# PEnIS
Groceries recording and visits controling information system (in Czech: Potraviny Evidující a Nocležný Informační Systém) 
is a system that allows control over finances and visits to flats and houses that are typically inhabited by students or other non-family related people 
for which reason is necessary to have control over these aspects of living together.
Primary target is for Czech users. English localisation will be added later.

---

![App preview](https://i.imgur.com/Q68hyVk.png)

---

## Technologies
![Python](https://img.shields.io/badge/Python-3.8-informational?style=for-the-badge&logo=Python&logoColor=white&color=092e20)
![Django](https://img.shields.io/badge/Backend-Django-informational?style=for-the-badge&logo=Django&logoColor=white&color=092e20)
![Vue](https://img.shields.io/badge/Frontend-Vue.js-informational?style=for-the-badge&logo=Vue.js&logoColor=white&color=42b883)
![Vuetify](https://img.shields.io/badge/Components-Vuetify-informational?style=for-the-badge&logo=Vuetify&logoColor=white&color=0099e5)
![MySql](https://img.shields.io/badge/Database-MySql-informational?style=for-the-badge&logo=MySQL&logoColor=white&color=00758F)
![API](https://img.shields.io/badge/Api-DRF-informational?style=for-the-badge&logo=Python&logoColor=white&color=092e20)
![Authentication](https://img.shields.io/badge/Authentication-JWT-informational?style=for-the-badge&logo=JSON+Web+Tokens&logoColor=white&color=be0027)

---

## Features

Desctiption | Status
--- | ---
Creating request with the specified date or even time of a visit | Done ✔
Process of accepting the visit request | Done ✔
Info table and calendar with all visits | Done ✔
Cash due | Done ✔
Specified users and houses | Soon ❌
JWT authentication | Soon ❌
Cash due statistics | Soon ❌
Filtering for big data in tables | Soon ❌
English localisation | Soon ❌

---

## Usage



### Prerequisites
- python 3.8
- node.js (access to npm commands)


### Setup
1. Clone repository
2. Create venv with python 3.8
3. Install requirements 
4. Create .env file in root folder (user .env.example)
5. in src/backend run `python manage.py migrate`
6. in src/frontend run `npm i`


### Run
- in src/frontend `npm run serve`
- in src/backend `python manage.py run server`
- open on backend port (default is 8000)

---

## License 
