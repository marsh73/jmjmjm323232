#Bulkuploader

##create bulkloader
	appcfg.py create_bulkloader_config --filename=bulkloader.yaml --url=http://jmjmjm323232.appspot.com/_ah/remote_api

## local upload
	appcfg.py upload_data --config_file=bulkloader.yaml --filename=stuff/sample-data-store.csv --kind=Trainer --url=http://localhost:8080/_ah/remote_api

## local download
	appcfg.py download_data --config_file=bulkloader.yaml --filename=trainers.csv --kind=Trainer --url=http://localhost:8080/_ah/remote_api

## remote Upload
	appcfg.py upload_data --config_file=bulkloader.yaml --filename=trainers.csv --kind=Trainer --url=http://jmjmjm323232.appspot.com/_ah/remote_api
