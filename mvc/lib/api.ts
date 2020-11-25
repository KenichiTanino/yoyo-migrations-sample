import { AddrView, AddrsType } from "./addr";

export class ApiClient {

    async get_addrs(axios: any): Promise<AddrsType> {
        let api_url = axios.defaults.baseURL + '/api/v1/addrs';
        return await axios.$get(api_url);
    }

    async post(axios: any, method: string, params: any): Promise<AddrsType> {
        let api_url = axios.defaults.baseURL + '/api/v1/addrs/' + method;
        return await axios.$post(api_url, params);
    }
}

export default ApiClient;