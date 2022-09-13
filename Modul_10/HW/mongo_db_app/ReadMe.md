**Steps to launch app**

`cd HW/mongo_db_app/src`
1. Start Docker container with MongoDB

`docker run -d -p 27017:27017 --name mongo_app mongo`

2. Feed our AddressBook 'fake' contacts

`python feed_fake_data.py`

3. Run app

`cd ..`

`python main.py`