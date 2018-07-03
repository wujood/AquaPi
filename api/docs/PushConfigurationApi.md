# swagger_client.PushConfigurationApi

All URIs are relative to *http://aquapihome.ddns.net:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_messages**](PushConfigurationApi.md#post_messages) | **POST** /Messages | Returns the current PushConfigurations
[**post_push_configuration**](PushConfigurationApi.md#post_push_configuration) | **POST** /PushConfiguration | Returns the current PushConfigurations
[**put_push_configuration**](PushConfigurationApi.md#put_push_configuration) | **PUT** /PushConfiguration | Sets new PushConfigurations


# **post_messages**
> Messages post_messages(request)

Returns the current PushConfigurations

Returns the current PushConfiguration

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PushConfigurationApi()
request = swagger_client.ParamPushConfiguration() # ParamPushConfiguration | The piid that you are interested in

try: 
    # Returns the current PushConfigurations
    api_response = api_instance.post_messages(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushConfigurationApi->post_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ParamPushConfiguration**](ParamPushConfiguration.md)| The piid that you are interested in | 

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_push_configuration**
> PushConfiguration post_push_configuration(request)

Returns the current PushConfigurations

Returns the current PushConfiguration

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PushConfigurationApi()
request = swagger_client.ParamPushConfiguration() # ParamPushConfiguration | Request object for this operation

try: 
    # Returns the current PushConfigurations
    api_response = api_instance.post_push_configuration(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushConfigurationApi->post_push_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ParamPushConfiguration**](ParamPushConfiguration.md)| Request object for this operation | 

### Return type

[**PushConfiguration**](PushConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_push_configuration**
> PushConfiguration put_push_configuration(request)

Sets new PushConfigurations

Sets new PushConfigurations

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PushConfigurationApi()
request = swagger_client.PushConfiguration() # PushConfiguration | Request object for this operation

try: 
    # Sets new PushConfigurations
    api_response = api_instance.put_push_configuration(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushConfigurationApi->put_push_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PushConfiguration**](PushConfiguration.md)| Request object for this operation | 

### Return type

[**PushConfiguration**](PushConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

