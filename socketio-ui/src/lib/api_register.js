
// Auto-generated file: api_register.js
// Generated from ./openapi.yaml

import {DefaultApi, SiteApi} from '@/lib/src';

// API Classes
const defaultApi = new DefaultApi();
defaultApi.basePath = 'http://localhost:8080';
const siteApi = new SiteApi();

// Fixes error: "Refused to set unsafe header "User-Agent"
defaultApi.apiClient.defaultHeaders = {}

// Export functions
export const hello = defaultApi.hello.bind(defaultApi);
export const get_site_layout = siteApi.getSiteLayout.bind(siteApi);
