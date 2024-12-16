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


import ApiClient from './ApiClient';
import GetSiteLayout from './models/GetSiteLayout';
import Hello from './models/Hello';
import DefaultApi from './apis/DefaultApi';
import SiteApi from './apis/SiteApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ConnexionApi = require('index'); // See note below*.
* var xxxSvc = new ConnexionApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ConnexionApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new ConnexionApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ConnexionApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The GetSiteLayout model constructor.
     * @property {module:models/GetSiteLayout}
     */
    GetSiteLayout,

    /**
     * The Hello model constructor.
     * @property {module:models/Hello}
     */
    Hello,

    /**
    * The DefaultApi service constructor.
    * @property {module:apis/DefaultApi}
    */
    DefaultApi,

    /**
    * The SiteApi service constructor.
    * @property {module:apis/SiteApi}
    */
    SiteApi
};