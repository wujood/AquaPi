# swagger_client.PostApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_component_settings**](PostApi.md#post_component_settings) | **POST** /ComponentSettings | Returns the current component settings


# **post_component_settings**
> ComponentSettings post_component_settings()

Returns the current component settings

Returns the current component settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()

try:
    # Returns the current component settings
    api_response = api_instance.post_component_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->post_component_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComponentSettings**](ComponentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

