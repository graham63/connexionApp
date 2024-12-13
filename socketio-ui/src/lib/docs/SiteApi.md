# ConnexionApi.SiteApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSiteLayout**](SiteApi.md#getSiteLayout) | **GET** /site/layout | Get info



## getSiteLayout

> GetSiteLayout getSiteLayout()

Get info

### Example

```javascript
import ConnexionApi from 'connexion_api';

let apiInstance = new ConnexionApi.SiteApi();
apiInstance.getSiteLayout().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSiteLayout**](GetSiteLayout.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

