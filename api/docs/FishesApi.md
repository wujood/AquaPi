# swagger_client.FishesApi

All URIs are relative to *http://aquapihome.ddns.net:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_fishes**](FishesApi.md#post_fishes) | **POST** /Fishes | Returns the fishes that are inside the aquarium
[**put_fishes**](FishesApi.md#put_fishes) | **PUT** /Fishes | Sets the fishes that are in the aquarium


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
api_instance = swagger_client.FishesApi()
request = swagger_client.ParamFishes() # ParamFishes | Request object for this operation

try: 
    # Returns the fishes that are inside the aquarium
    api_response = api_instance.post_fishes(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FishesApi->post_fishes: %s\n" % e)
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
api_instance = swagger_client.FishesApi()
request = swagger_client.Fishes() # Fishes | Request object for this operation

try: 
    # Sets the fishes that are in the aquarium
    api_response = api_instance.put_fishes(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FishesApi->put_fishes: %s\n" % e)
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

