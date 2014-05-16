Uploading data to your app's datastore
--------------------------------------

Before you can upload data, you need to make the following configuration updates (see AppEngine documentation for [Uploading and Downloading Data](https://developers.google.com/appengine/docs/python/tools/uploadingdata) for a more detailed explanation).

1. Enable remote_api for your app by adding the following lines to your app.yaml file and deploying:

        builtins:
        - remote_api: on

    _Note: You can deploy to a 'stage' version of your app and use your stage URL in the commands outlined in the following steps_

2. Generate a bulkloader.yaml file in your local environment by running the following in Terminal from your project root:

        appcfg.py create_bulkloader_config --filename=bulkloader.yaml --url=http://[your_app_id].appspot.com/_ah/remote_api

3. Update the connector and key names in your bulkloader.yaml file

4. Run the following command in Terminal from the root of your project to upload your data:

        appcfg.py upload_data --config_file=bulkloader.yaml --filename=[path to CSV file] --kind=[datastore entity name] --url=http://[your_app_id].appspot.com/_ah/remote_api --has_header