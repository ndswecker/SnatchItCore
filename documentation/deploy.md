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

1. Create a machine image of the production vm instance
1. Create instance
1. Update nginx
    ```
    sudo nano /etc/nginx/conf.d/app.conf
    sudo systemctl restart nginx
    sudo systemctl daemon-reload
    ```
1. Test that the browser is serving the app at the IP
1. Test updating the production clone:

    ```shell
    cd /srv/web/
    sudo git pull
    sudo git checkout dev
    sudo bash /srv/web/deploy/update.sh
    ```

1. Delete test machine image

### Apply all changes to production environment
1. Merge Dev into Main
    ```shell
    cd /srv/web/
    sudo git pull
    sudo git checkout main
    sudo bash /srv/web/deploy/update.sh
    ```

