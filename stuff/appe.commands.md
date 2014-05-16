# appengine Commands

## Upload and launch App
appcfg.py update <directory>

## Bulkuploader

## create bulkloader
    appcfg.py create_bulkloader_config --filename=bulkloader.yaml --url=http://<app_id>.appspot.com/_ah/remote_api

## local upload data
    appcfg.py upload_data --config_file=bulkloader.yaml --filename=<path_to_file> --kind=<kind> --url=http://localhost:<port>/_ah/remote_api

## local download data
    appcfg.py download_data --config_file=bulkloader.yaml --filename=<path_to_file> --kind=<kind> --url=http://localhost:<port>/_ah/remote_api

## remote Upload data
    appcfg.py upload_data --config_file=bulkloader.yaml --filename=<path_to_file> --kind=<kind> --url=http://<app_id>.appspot.com/_ah/remote_api

## remote Download data
    appcfg.py download_data --config_file=bulkloader.yaml --filename=<path_to_file> --kind=<kind> --url=http://<app_id>.appspot.com/_ah/remote_api