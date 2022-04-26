""" Copyright start
  Copyright (C) 2008 - 2020 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import validators, requests, json
import base64
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('FortiAuthenticator')

error_msgs = {
    400: 'Bad/Invalid Request',
    401: 'Unauthorized: Invalid credentials',
    403: 'Access Denied',
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable'
}


class FortiAuthenticator(object):
    def __init__(self, config):
        self.server_url = config.get('server', '')
        if not self.server_url.startswith('https://'):
            self.server_url = 'https://' + self.server_url
        if not self.server_url.endswith('/'):
            self.server_url += '/'
        self.username = config.get('username')
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')

    def make_api_call(self, endpoint=None, method='GET', data=None, params=None):
        try:
            url = self.server_url + endpoint
            b64_credential = base64.b64encode((self.username + ":" + self.api_key).encode('utf-8')).decode()
            headers = {'Authorization': "Basic " + b64_credential, 'Content-Type': 'application/json'}
            response = requests.request(method, url, params=params, data=data, headers=headers, verify=self.verify_ssl)
            if response.ok:
                return response.json()
            else:
                logger.error(response.text)
                raise ConnectorError({'status_code': response.status_code, 'message': response.reason})
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.exception(str(err))
            raise ConnectorError(str(err))


def _check_health(config):
    fa = FortiAuthenticator(config)
    try:
        response = fa.make_api_call(endpoint='/api/v1/')
        if response:
            logger.info('connector available')
            return True
    except Exception as e:
        raise ConnectorError('{0}'.format(e))


def get_params(params):
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    return params


def get_schema(config, params):
    fa = FortiAuthenticator(config)
    return fa.make_api_call(endpoint='/api/v1/')


def get_users(config, params):
    fa = FortiAuthenticator(config)
    return fa.make_api_call(endpoint='/api/v1/localusers/')


def get_local_user(config, params):
    fa = FortiAuthenticator(config)
    params = get_params(params)
    mode = params.get('output_mode', '')
    if mode == 'ID':
        return fa.make_api_call(endpoint='/api/v1/localusers/' + str(params.get('id')) + '/')
    else:
        return fa.make_api_call(endpoint='/api/v1/localusers/', params=params)


def create_local_user(config, params):
    fa = FortiAuthenticator(config)
    params = get_params(params)
    return fa.make_api_call(endpoint='/api/v1/localusers/', data=json.dumps(params), method='POST')


def update_user_status(config, params):
    fa = FortiAuthenticator(config)
    id = str(params.get('userid'))
    active = params.get('active')
    return fa.make_api_call(endpoint='/api/v1/localusers/' + id + '/', data=json.dumps({'active': active}),
                            method='PATCH')


def get_ladap_user(config, params):
    fa = FortiAuthenticator(config)
    params = get_params(params)
    mode = params.get('output_mode', '')
    if mode == 'ID':
        return fa.make_api_call(endpoint='/api/v1/ldapusers/' + str(params.get('id')) + '/')
    else:
        return fa.make_api_call(endpoint='/api/v1/ldapusers/', params=params)


def update_ladapuser_status(config, params):
    fa = FortiAuthenticator(config)
    id = str(params.get('userid'))
    active = params.get('active')
    return fa.make_api_call(endpoint='/api/v1/ldapusers/' + id + '/', data=json.dumps({'active': active}),
                            method='PATCH')


def get_radius_user(config, params):
    fa = FortiAuthenticator(config)
    params = get_params(params)
    mode = params.get('output_mode', '')
    if mode == 'ID':
        return fa.make_api_call(endpoint='/api/v1/localusers/' + str(params.get('id')) + '/')
    else:
        return fa.make_api_call(endpoint='/api/v1/localusers/', params=params)


def update_radiususer_status(config, params):
    fa = FortiAuthenticator(config)
    id = str(params.get('userid'))
    active = params.get('active')
    return fa.make_api_call(endpoint='/api/v1/radiususers/' + id + '/', data=json.dumps({'active': active}),
                            method='PATCH')


def get_userlockout_policy(config, params):
    fa = FortiAuthenticator(config)
    return fa.make_api_call(endpoint='/api/v1/userlockoutpolicy/')


operations = {
    'get_schema': get_schema,
    'get_users': get_users,
    'get_local_user': get_local_user,
    'create_local_user': create_local_user,
    'update_user_status': update_user_status,
    'get_ladap_user': get_ladap_user,
    'update_ladapuser_status': update_ladapuser_status,
    'get_radius_user': get_radius_user,
    'update_radiususer_status': update_radiususer_status,
    'get_userlockout_policy': get_userlockout_policy
}
