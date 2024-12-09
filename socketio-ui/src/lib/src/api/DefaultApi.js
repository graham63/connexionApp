/**
 * Connexion API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Hello200Response from '../model/Hello200Response';

/**
* Default service.
* @module api/DefaultApi
* @version 1.0.0
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }



    /**
     * Returns Hello World
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing data of type {@link module:model/Hello200Response} and HTTP response
     */
    helloWithHttpInfo() {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Hello200Response;
      return this.apiClient.callApi(
        '/hello', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null
      );
    }

    /**
     * Returns Hello World
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with data of type {@link module:model/Hello200Response}
     */
    hello() {
      return this.helloWithHttpInfo()
        .then(function(response_and_data) {
          return response_and_data.data;
        });
    }


}
