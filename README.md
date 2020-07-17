# Randori-API
Endpoints accessible using API tokens

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.2.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.randori.com/contact/](https://www.randori.com/contact/)

## Requirements.

Python 2.7 or 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/RandoriDev/randori-api-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/RandoriDev/randori-api-sdk.git`)

Then import the package:
```python
import randori_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import randori_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import randori_api
from randori_api.rest import ApiException
from pprint import pprint

configuration = randori_api.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://alpha.randori.io
configuration.host = "https://alpha.randori.io"
# Create an instance of the API class
api_instance = randori_api.RandoriApi(randori_api.ApiClient(configuration))
offset = 56 # int | offset into avilable records after filtering (optional)
limit = 56 # int | maximum number of records to return (optional)
sort = ['sort_example'] # list[str] | fields in the object to sort by, in order of precedence, minus indicates descending (optional)
q = 'q_example' # str | base64 encoded jquery querybuilder complex search field (optional)
reversed_nulls = True # bool | if true, sorts nulls as if smaller than any nonnull value for all sort parameters. otherwise (default) treats as if larger (optional)

try:
    api_response = api_instance.get_all_detections_for_target(offset=offset, limit=limit, sort=sort, q=q, reversed_nulls=reversed_nulls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RandoriApi->get_all_detections_for_target: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://alpha.randori.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RandoriApi* | [**get_all_detections_for_target**](docs/RandoriApi.md#get_all_detections_for_target) | **GET** /recon/api/v1/all-detections-for-target | 
*RandoriApi* | [**get_hostname**](docs/RandoriApi.md#get_hostname) | **GET** /recon/api/v1/hostname | 
*RandoriApi* | [**get_hostnames_for_ip**](docs/RandoriApi.md#get_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip | 
*RandoriApi* | [**get_ip**](docs/RandoriApi.md#get_ip) | **GET** /recon/api/v1/ip | 
*RandoriApi* | [**get_ips_for_hostname**](docs/RandoriApi.md#get_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname | 
*RandoriApi* | [**get_ips_for_network**](docs/RandoriApi.md#get_ips_for_network) | **GET** /recon/api/v1/ips-for-network | 
*RandoriApi* | [**get_ips_for_service**](docs/RandoriApi.md#get_ips_for_service) | **GET** /recon/api/v1/ips-for-service | 
*RandoriApi* | [**get_network**](docs/RandoriApi.md#get_network) | **GET** /recon/api/v1/network | 
*RandoriApi* | [**get_ports_for_ip**](docs/RandoriApi.md#get_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip | 
*RandoriApi* | [**get_service**](docs/RandoriApi.md#get_service) | **GET** /recon/api/v1/service | 
*RandoriApi* | [**get_single_detection_for_target**](docs/RandoriApi.md#get_single_detection_for_target) | **GET** /recon/api/v1/single-detection-for-target | 
*RandoriApi* | [**get_single_hostname**](docs/RandoriApi.md#get_single_hostname) | **GET** /recon/api/v1/hostname/{id} | 
*RandoriApi* | [**get_single_hostnames_for_ip**](docs/RandoriApi.md#get_single_hostnames_for_ip) | **GET** /recon/api/v1/hostnames-for-ip/{id} | 
*RandoriApi* | [**get_single_ip**](docs/RandoriApi.md#get_single_ip) | **GET** /recon/api/v1/ip/{id} | 
*RandoriApi* | [**get_single_ips_for_hostname**](docs/RandoriApi.md#get_single_ips_for_hostname) | **GET** /recon/api/v1/ips-for-hostname/{id} | 
*RandoriApi* | [**get_single_ips_for_network**](docs/RandoriApi.md#get_single_ips_for_network) | **GET** /recon/api/v1/ips-for-network/{id} | 
*RandoriApi* | [**get_single_ips_for_service**](docs/RandoriApi.md#get_single_ips_for_service) | **GET** /recon/api/v1/ips-for-service/{id} | 
*RandoriApi* | [**get_single_network**](docs/RandoriApi.md#get_single_network) | **GET** /recon/api/v1/network/{id} | 
*RandoriApi* | [**get_single_ports_for_ip**](docs/RandoriApi.md#get_single_ports_for_ip) | **GET** /recon/api/v1/ports-for-ip/{id} | 
*RandoriApi* | [**get_single_service**](docs/RandoriApi.md#get_single_service) | **GET** /recon/api/v1/service/{id} | 
*RandoriApi* | [**get_single_target**](docs/RandoriApi.md#get_single_target) | **GET** /recon/api/v1/target/{id} | 
*RandoriApi* | [**get_statistics**](docs/RandoriApi.md#get_statistics) | **GET** /recon/api/v1/statistics | 
*RandoriApi* | [**get_target**](docs/RandoriApi.md#get_target) | **GET** /recon/api/v1/target | 


## Documentation For Models

 - [AllDetectionsForTarget](docs/AllDetectionsForTarget.md)
 - [AllDetectionsForTargetGetOutput](docs/AllDetectionsForTargetGetOutput.md)
 - [ErrorSchema](docs/ErrorSchema.md)
 - [Hostname](docs/Hostname.md)
 - [HostnameGetOutput](docs/HostnameGetOutput.md)
 - [HostnameSingleOutput](docs/HostnameSingleOutput.md)
 - [HostnamesForIp](docs/HostnamesForIp.md)
 - [HostnamesForIpGetOutput](docs/HostnamesForIpGetOutput.md)
 - [HostnamesForIpSingleOutput](docs/HostnamesForIpSingleOutput.md)
 - [Ip](docs/Ip.md)
 - [IpGetOutput](docs/IpGetOutput.md)
 - [IpSingleOutput](docs/IpSingleOutput.md)
 - [IpsForHostname](docs/IpsForHostname.md)
 - [IpsForHostnameGetOutput](docs/IpsForHostnameGetOutput.md)
 - [IpsForHostnameSingleOutput](docs/IpsForHostnameSingleOutput.md)
 - [IpsForNetwork](docs/IpsForNetwork.md)
 - [IpsForNetworkGetOutput](docs/IpsForNetworkGetOutput.md)
 - [IpsForNetworkSingleOutput](docs/IpsForNetworkSingleOutput.md)
 - [IpsForService](docs/IpsForService.md)
 - [IpsForServiceGetOutput](docs/IpsForServiceGetOutput.md)
 - [IpsForServiceSingleOutput](docs/IpsForServiceSingleOutput.md)
 - [Network](docs/Network.md)
 - [NetworkGetOutput](docs/NetworkGetOutput.md)
 - [NetworkSingleOutput](docs/NetworkSingleOutput.md)
 - [PortsForIp](docs/PortsForIp.md)
 - [PortsForIpGetOutput](docs/PortsForIpGetOutput.md)
 - [PortsForIpSingleOutput](docs/PortsForIpSingleOutput.md)
 - [Service](docs/Service.md)
 - [ServiceGetOutput](docs/ServiceGetOutput.md)
 - [ServiceSingleOutput](docs/ServiceSingleOutput.md)
 - [SingleDetectionForTarget](docs/SingleDetectionForTarget.md)
 - [SingleDetectionForTargetGetOutput](docs/SingleDetectionForTargetGetOutput.md)
 - [Statistics](docs/Statistics.md)
 - [StatisticsGetOutput](docs/StatisticsGetOutput.md)
 - [Target](docs/Target.md)
 - [TargetGetOutput](docs/TargetGetOutput.md)
 - [TargetSingleOutput](docs/TargetSingleOutput.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

support@randori.com


