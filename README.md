# magento-abandoned-carts
Look for abandoned carts (quotes that did not become orders) and send email to shop owner for each abandoned cart. Uses sendgrid and sendgrid APIs to send email. Works with magento 1.9.*, however, uses direct SQL on database as API does not offer quotes. 


## Configuration - get code, set up virtual environment, install dependencies
Navigate to a folder where the folder with the code should be located.

`git clone https://github.com/martinskeem/magento-abandoned-carts.git`

create virtual environment

```bash
cd magento-abandoned-carts
virtualenv . -p /usr/bin/python3`
```

activate the virtual environment

`source bin/activate`

install dependencies

`pip install -r requirements.txt`

create log folder

`mkdir log`


## Configuration - secrets.py
In order for the synchronization scripts to work, various configuration variables need to be set in a file named `secrets.py`. Add the file to the root of the project folder and use below template:

```python
mysql_magento_database= ""
mysql_magento_host = ""
mysql_magento_user = ""
mysql_magento_password = ""

mysql_magentosync_database= ""
mysql_magentosync_host = ""
mysql_magentosync_user = ""
mysql_magentosync_password = ""

sendgrid_api_key = ""
```


## Configuration - crontab
The script Synchronizes changes done last day by default (this can be changed in `sync.py` with the `delta_load_days parameter`). If the job is scheduled to more than once per day (e.g. every 30 minutes), this is sufficient. Later, this may be updated to handle delta load more elegantly by maintaining state of already synchronized entities. Example crontab schedule that synchronizes data every 30 minutes:

```bash
/30 * * * * /var/python/magento-abandoned-carts/bin/python /var/python/magento-abandoned-carts/sync.py
```


## Configuration - logging
Emits logging to console and flat file in subfolder `/log`. This can be configured in `logging.conf`.