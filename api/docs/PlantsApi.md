# swagger_client.PlantsApi

All URIs are relative to *http://aquapihome.ddns.net:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_plants**](PlantsApi.md#post_plants) | **POST** /Plants | Returns the plants in the soil
[**put_plants**](PlantsApi.md#put_plants) | **PUT** /Plants | Sets the number of plants


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
api_instance = swagger_client.PlantsApi()
request = swagger_client.ParamPlants() # ParamPlants | Request object for this operation

try: 
    # Returns the plants in the soil
    api_response = api_instance.post_plants(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlantsApi->post_plants: %s\n" % e)
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
api_instance = swagger_client.PlantsApi()
request = swagger_client.Plants() # Plants | Request object for this operation

try: 
    # Sets the number of plants
    api_instance.put_plants(request)
except ApiException as e:
    print("Exception when calling PlantsApi->put_plants: %s\n" % e)
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

