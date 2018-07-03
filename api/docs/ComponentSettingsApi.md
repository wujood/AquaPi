# swagger_client.ComponentSettingsApi

All URIs are relative to *http://aquapihome.ddns.net:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_component_settings**](ComponentSettingsApi.md#post_component_settings) | **POST** /ComponentSettings | Returns the current component settings
[**put_component_settings**](ComponentSettingsApi.md#put_component_settings) | **PUT** /ComponentSettings | Sets a new component settings


# **post_component_settings**
> list[ComponentSettings] post_component_settings(request)

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
api_instance = swagger_client.ComponentSettingsApi()
request = swagger_client.ParamComponentSettingsPost() # ParamComponentSettingsPost | Request object for this operation

try: 
    # Returns the current component settings
    api_response = api_instance.post_component_settings(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentSettingsApi->post_component_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ParamComponentSettingsPost**](ParamComponentSettingsPost.md)| Request object for this operation | 

### Return type

[**list[ComponentSettings]**](ComponentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.ComponentSettingsApi()
request = swagger_client.ComponentSettings() # ComponentSettings | Request object for this operation

try: 
    # Sets a new component settings
    api_instance.put_component_settings(request)
except ApiException as e:
    print("Exception when calling ComponentSettingsApi->put_component_settings: %s\n" % e)
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

