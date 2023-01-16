0x10. Python - Network #0
=========================

Learning Objectives
-------------------

-   What a URL is
-   What HTTP is
-   How to read a URL
-   The scheme for a HTTP URL
-   What a domain name is
-   What a sub-domain is
-   How to define a port number in a URL
-   What a query string is
-   What an HTTP request is
-   What an HTTP response is
-   What HTTP headers are
-   What the HTTP message body is
-   What an HTTP request method is
-   What an HTTP response status code is
-   What an HTTP Cookie is
-   How to make a request with cURL
-   What happens when you type google.com in your browser (Application level)

## Tasks :page_with_curl:

* **0. cURL body size**
  * [0-body_size.sh](./0-body_size.sh): Bash script that sends a `GET` request to
  a given URL and displays the size of the response body in bytes.

* **1. cURL to the end**
  * [1-body.sh](./1-body.sh): Bash script that sends a `GET` request to a given
  URL and displays the response body for a `200` status code response.

* **2. cURL Method**
  * [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to
  a given URL and displays the response body.

* **3. cURL only methods**
  * [3-methods.sh](./3-methods.sh): Bash script that displays all HTTP methods
  the server of a given URL will accept.

* **4. cURL headers**
  * [4-header.sh](./4-header.sh): Bash script that sends a `GET` request to a
  given URL with a header variable `X-School-User-Id=98` and displays
  the response body.

* **5. cURL POST parameters**
  * [5-post_params.sh](./5-post_params.sh): Bash script that sends a `POST`
  request to a given URL with the variables `email=test@gmail.com` and
  `subject=I will always be here for PLD` and displays the response body.

* **6. Find a peak**
  * [6-peak.py](./6-peak.py): [Technical interview preparation] - Python
  program that finds a peak in a list of unsorted integers.
  * [6-peak.txt](./6-peak.txt): Text file containing the complexity of the
  algorithm.

* **7. Only status code**
  * [100-status_code.sh](./100-status_code.sh): Bash script that sends a `GET`
  request to a given URL without using pipes, redirections, `;`, or `&&` and
  displays the status code of the response.

* **8. cURL a JSON file**
  * [101-post_json.sh](./101-post_json.sh): Bash script that sends a JSON `POST`
  request with the contents of a provided file to a given URL, and displays the
  response body.

* **9. Catch me if you can!**
  * [102-catch_me.sh](./102-catch_me.sh): Bash script that sends a request to
  `0.0.0.0:5000/catch_me` that causes the server to respond with a message
  containing `You got me!` in the repsonse body.
