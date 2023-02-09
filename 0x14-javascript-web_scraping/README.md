0x14. JavaScript - Web scraping
===============================

Learning Objectives
-------------------

-   Why JavaScript programming is amazing
-   How to manipulate JSON data
-   How to use `request` and fetch API
-   How to read and write a file using `fs` module

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/node`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should be `semistandard` compliant. [Rules of Standard](https://alx-intranet.hbtn.io/rltoken/W9rASrTqkF-xXjcwomrMLw "Rules of Standard") + [semicolons on top](https://alx-intranet.hbtn.io/rltoken/GXh9DyGGivUB7pdq9Oqmzg "semicolons on top"). Also as reference: [AirBnB style](https://alx-intranet.hbtn.io/rltoken/NZR55f9vk1dZXj5q7UI5mQ "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   You are not allowed to use `var`

More Info
---------

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://alx-intranet.hbtn.io/rltoken/GXh9DyGGivUB7pdq9Oqmzg "Documentation")

```
$ sudo npm install semistandard --global

```

### Install `request` module and use it

[Documentation](https://alx-intranet.hbtn.io/rltoken/goymbxGy-cTc5ZdKBTUcTQ "Documentation")

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

```

**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it's a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Tasks
-----

### [0. Readme](./0-readme.js)
* Write a script that reads and prints the content of a file.
* Usage: `./0-readme.js <file path>`.

### [1. Write me](./1-writeme.js)
* Write a script that writes a string to a file.
* Usage: `./1-writeme.js <file path> <string to write>`.

### [2. Status code](./2-statuscode.js)
* Write a script that display the status code of a GET request.
* Usage: `./2-statuscode.js <URL to GET>`.
* Output: `code: <status code>`.

### [3. Star wars movie title](./3-starwars_title.js)
* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
* Usage: `./3-starwars_title.js <3-starwars_title.js>`.

### [4. Star wars Wedge Antilles](./4-starwars_count.js)
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
* Usage: `./4-starwars_count.js http://swapi.co/api/films/`.

### [5. Loripsum](./5-request_store.js)
* Write a script that gets the contents of a webpage and stores it in a file.
* Usage: `./5-request_store.js <URL to get> <file path to store content in>`.

### [6. How many completed?](./6-completed_tasks.js)
* Write a script that computes the number of tasks completed by user id.
* Usage: `./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`.

### [7. Who was playing in this movie?](./100-starwars_characters.js)
* Write a script that prints all characters of a Star Wars movie:
* Usage: `./100-starwars_characters.js <movie ID>`.

### [8. Right order](./101-starwars_characters.js)
* Write a script that prints all characters of a Star Wars movie:
* Usage: `./101-starwars_characters.js <movie ID>`.

---

## Author
* **Mugigayi Amili Hussein** - [Amili-usain](https://github.com/Amili-usain)
