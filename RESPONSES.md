Question 3
* Since the aim of the project is to produce a complete up-to-date picture of a musical work, where a conflicting information is provided about same work, the most up-to-date version of this information should be selected over the previous. In which case the "PUT" method will be called to update the information appropriately

* For the sake of clean coding, readability of code, and other coding best practices, I'll suggest an additonal endpoint be created to handle the creation of the SingleView

* If the SingleView has 20 million musical works, the response time will definite be impacted negatively. The API reponse time will decrease greatly. Below are some ways to improve the API performance in such a situation:
1. employ a more performant Relational Database Management System like AWS AuroraDB that provide lower latency.
2. employ request queueing by using RabbitMQ and introduce asychronous request processing with Celery
3. for information search optimization, Elasticsearch should provide a lot of advantages
4. using redis or memcached from in-memormy management should take some load of the database system

NOTE:
* The Django Management Command for digesting CSV can be ran with the command below
- sudo docker exec -it bmat_bo_api python manage.py csv_digest "<file path>"
* Any files to be digested should be first copied into the file directory in the root of this project, a bind mount has been created to update the twin-directory appropriately

