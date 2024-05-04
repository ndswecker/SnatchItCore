## Test Deployment of Dev

### Verify that Dev is Deployable 

1. Merge all branches into Dev.
1. Squash Migrations
    1. Delete all new migrations
    2. make migrations 
        ```
        python .\app\manage.py makemigrations
        ```

1. Create a clean virtual machine:
    1. "New VM Instance" blue button
    1. allow http, https, load balancer
    1. create, allow for time
        1. ssh button into it
    - Inside VM, run the following commands:

    ```shell
    sudo apt update
    sudo apt upgrade -y
    sudo apt install git -y
    sudo git clone --branch dev https://github.com/ndswecker/SnatchItCore.git /srv/web
    sudo bash /srv/web/deploy/install.sh
    sudo /srv/web/venv/bin/python3 /srv/web/app/manage.py createsuperuser
    ```

1. Evaluate the Dev deployment.
1. Delete the Dev virtual machine.

### Verify Production is Updatable Locally

1. Delete the database.
1. Run the install script.
1. Run migrations:
    ```shell
    python .\app\manage.py migrate
    ```
1. Verify no errors.

### Verify Production is Updatable Remotely

1. Clone the production VM.
1. Test updating the production clone:

    ```shell
    sudo bash /srv/web/deploy/update.sh
    ```

1. SSH into the production VM.
1. Run the update script.
