# encrypt-trial
Django REST Framework project for uploading and encrypting files

## Setup
> pipenv install

> pipenv shell # install dependencies

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver

## Demo
Go to: http://127.0.0.1:8000/api/upload_file/ in your browser
![image](https://github.com/user-attachments/assets/acda59dd-1e96-4e1b-b99f-a5301e8e3b7c)

Click "Choose File" then pick a fiile to upload. After picking a file, click "POST" button.

After uploading a file you will see this return in the page.
![image](https://github.com/user-attachments/assets/8a6b33b9-215a-44ec-9d61-0442b4e5151d)

Create an admin account to view the data uploaded
> python manage.py createsuperuser

After creating an account go to the admin page then login. http://127.0.0.1:8000/admin/

Go to File Upload page http://127.0.0.1:8000/admin/file_upload/fileupload/
then click the file you uploaded
![image](https://github.com/user-attachments/assets/a925b8d2-584a-4887-ba92-1976bc7f09ae)
![image](https://github.com/user-attachments/assets/c25ce7e9-ca1c-4e39-882d-8577042a0568)

If you click on the file you can see the link and its content. As you can see the contents of it is encrypted
http://127.0.0.1:8000/media/sample.txt
![image](https://github.com/user-attachments/assets/535a83d0-bd90-4b47-bce3-6c34bddf97b8)


