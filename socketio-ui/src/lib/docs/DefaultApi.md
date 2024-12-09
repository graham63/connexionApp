# ConnexionApi.DefaultApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hello**](DefaultApi.md#hello) | **GET** /hello | Returns Hello World



## hello

> Hello200Response hello()

Returns Hello World

### Example

```javascript
import ConnexionApi from 'connexion_api';

let apiInstance = new ConnexionApi.DefaultApi();
apiInstance.hello().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Hello200Response**](Hello200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

