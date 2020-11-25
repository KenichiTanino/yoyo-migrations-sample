import Vue from 'vue'
import {
  extend,
  ValidationProvider,
  ValidationObserver,
  localize
} from 'vee-validate'
import ja from 'vee-validate/dist/locale/ja.json'
import { required } from 'vee-validate/dist/rules'

extend('required', required)
// see: https://teratail.com/questions/231233
const validate_ip = require('is-ip');
const validate_ip_cidr = require('is-cidr');

extend("ipaddr", {
        params: [],
      	validate: (value) => {
          if (validate_ip(value) || validate_ip_cidr(value) ) {
            return true;
          }
          return false;
        },
        message:
          "IPAddress must be valid"
        }
);

Vue.component('validation-provider', ValidationProvider)
Vue.component('validation-observer', ValidationObserver)

localize('ja', ja)