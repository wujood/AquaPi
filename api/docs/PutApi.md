# swagger_client.PutApi

All URIs are relative to *http://aquapihome.ddns.net:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_component_settings**](PutApi.md#put_component_settings) | **PUT** /ComponentSettings | Sets a new component settings
[**put_fishes**](PutApi.md#put_fishes) | **PUT** /Fishes | Sets the fishes that are in the aquarium
[**put_plants**](PutApi.md#put_plants) | **PUT** /Plants | Sets the number of plants
[**put_push_configuration**](PutApi.md#put_push_configuration) | **PUT** /PushConfiguration | Sets new PushConfigurations


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

# **put_fishes**
> Fishes put_fishes(request)

Sets the fishes that are in the aquarium

Sets the fishes that are in the aquarium

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PutApi()
request = swagger_client.Fishes() # Fishes | Request object for this operation

try: 
    # Sets the fishes that are in the aquarium
    api_response = api_instance.put_fishes(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PutApi->put_fishes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Fishes**](Fishes.md)| Request object for this operation | 

### Return type

[**Fishes**](Fishes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_plants**
> put_plants(request)

Sets the number of plants

Sets the number of plants

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PutApi()
request = swagger_client.Plants() # Plants | Request object for this operation

try: 
    # Sets the number of plants
    api_instance.put_plants(request)
except ApiException as e:
    print("Exception when calling PutApi->put_plants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Plants**](Plants.md)| Request object for this operation | 

### Return type

void (empty response body)

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
api_instance = swagger_client.PutApi()
request = swagger_client.PushConfiguration() # PushConfiguration | Request object for this operation

try: 
    # Sets new PushConfigurations
    api_response = api_instance.put_push_configuration(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PutApi->put_push_configuration: %s\n" % e)
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

