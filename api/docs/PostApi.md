# swagger_client.PostApi

All URIs are relative to *http://aquapihome.ddns.net:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_component_settings**](PostApi.md#post_component_settings) | **POST** /ComponentSettings | Returns the current component settings
[**post_fishes**](PostApi.md#post_fishes) | **POST** /Fishes | Returns the fishes that are inside the aquarium
[**post_messages**](PostApi.md#post_messages) | **POST** /Messages | Returns the current PushConfigurations
[**post_plants**](PostApi.md#post_plants) | **POST** /Plants | Returns the plants in the soil
[**post_push_configuration**](PostApi.md#post_push_configuration) | **POST** /PushConfiguration | Returns the current PushConfigurations


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
api_instance = swagger_client.PostApi()
request = swagger_client.ParamComponentSettingsPost() # ParamComponentSettingsPost | Request object for this operation

try: 
    # Returns the current component settings
    api_response = api_instance.post_component_settings(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->post_component_settings: %s\n" % e)
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

# **post_fishes**
> list[Fishes] post_fishes(request)

Returns the fishes that are inside the aquarium

Returns the fishes that are inside the aquarium by name and quantity

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()
request = swagger_client.ParamFishes() # ParamFishes | Request object for this operation

try: 
    # Returns the fishes that are inside the aquarium
    api_response = api_instance.post_fishes(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->post_fishes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ParamFishes**](ParamFishes.md)| Request object for this operation | 

### Return type

[**list[Fishes]**](Fishes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.PostApi()
request = swagger_client.ParamPushConfiguration() # ParamPushConfiguration | The piid that you are interested in

try: 
    # Returns the current PushConfigurations
    api_response = api_instance.post_messages(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->post_messages: %s\n" % e)
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

# **post_plants**
> list[Plants] post_plants(request)

Returns the plants in the soil

Returns the plants in the soil

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()
request = swagger_client.ParamPlants() # ParamPlants | Request object for this operation

try: 
    # Returns the plants in the soil
    api_response = api_instance.post_plants(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->post_plants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ParamPlants**](ParamPlants.md)| Request object for this operation | 

### Return type

[**list[Plants]**](Plants.md)

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
api_instance = swagger_client.PostApi()
request = swagger_client.ParamPushConfiguration() # ParamPushConfiguration | Request object for this operation

try: 
    # Returns the current PushConfigurations
    api_response = api_instance.post_push_configuration(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->post_push_configuration: %s\n" % e)
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

