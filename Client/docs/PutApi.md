# swagger_client.PutApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_component_settings**](PutApi.md#put_component_settings) | **PUT** /ComponentSettings | Sets a new component settings


# **put_component_settings**
> put_component_settings(request)

Sets a new component settings

Sets a new component settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PutApi()
request = swagger_client.ComponentSettings() # ComponentSettings | Request object for this operation

try:
    # Sets a new component settings
    api_instance.put_component_settings(request)
except ApiException as e:
    print("Exception when calling PutApi->put_component_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ComponentSettings**](ComponentSettings.md)| Request object for this operation | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

