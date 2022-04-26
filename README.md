## About the connector

FortiAuthenticator is a centralized user Identity Management solution to transparently identify network users and enforce identity-driven access policy in a Fortinet fabric. It supports FortiToken Two-factor authentication, Certificate and Wireless Guest management and Single Sign On capability.

### Version information

Connector Version: 1.0.0

Tested on FortiAuthenticator: 6.2.0

Authored By: Fortinet SE

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-juniper-junos`

## Prerequisites to configuring the connector
- You must have the URL of FortiAuthenticator server to which you will connect and perform automated operations and username/password credentials to access that appliance.
- The FortiSOAR&trade; server should have outbound connectivity to port 3443 (or the configured port) on the FortiAuthentictor Appliance.

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Juniper JunOS</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody>
<tr><td>Device URL<br></td><td>Management IP address or URL of the FortiAuthenticator appliance<br>
<tr><td>Username<br></td><td>FortiAuthenticator Username<br>
<tr><td>API Key<br></td><td>API Key<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Schema<br></td><td>Retrieves a report for all the endpoint actions within FortiAuthenticator<br></td><td>get_schema<br/>Information<br></td></tr>
<tr><td>Get Local Users<br></td><td>This endpoint represents local user resource, namely a user account. This resource can be found in the FortiAuthenticator GUI under Authentication > Local Users..<br></td><td>get_users<br/>Configuration<br></td></tr>
<tr><td>Get Specific Local User<br></td><td>Get Local Use by ID<br></td><td>get_local_user<br/>Configuration<br></td></tr>
<tr><td>Create Local User<br></td><td>This endpoint represents local user resource, namely a user account. This resource can be found in the FortiAuthenticator GUI under Authentication > Local Users.<br></td><td>create_local_user<br/>Configuration<br></td></tr>
<tr><td>Update Local User Status<br></td><td>Activate/Deactivates local user.<br></td><td>update_user_status<br/>Configuration<br></td></tr>
<tr><td>Get Specific Ladap User<br></td><td>Get Local Use by filter paramaters<br></td><td>get_ladap_user<br/>Configuration<br></td></tr>
<tr><td>Update LDAP User<br></td><td>Deactivates LDAP user.<br></td><td>update_ladapuser_status<br/>Configuration<br></td></tr>
<tr><td>Update Radius User<br></td><td>Active/Deactive Radius user.<br></td><td>update_radiususer_status<br/>Configuration<br></td></tr>
<tr><td>User Lockout Policy Info<br></td><td>This endpoint is used to query and edit user account lockout policy settings including the maximum number of failed login attempts, specify the lockout period, and enable inactive user lockouts.<td>get_userlockout_policy<br/>Configuration<br></td></tr>
<tr><td>Get Specific Radius User<br></td><td>Get Radius Use by filter paramaters<br></td><td>get_radius_user<br/>Configuration<br></td></tr>
</tbody></table>

### operation: Get Schema
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody>
<tr><td>Request Schema<br></td><td>Retrieves a report for all the endpoint actions within FortiAuthenticator<br></td>
</td></tr></tbody></table>


#### Output
The output contains the following populated JSON schema: <JSON Output>
```
  {
        "auth": {
          "list_endpoint": "",
          "schema": ""
        },
        "emergencytoken": {
          "list_endpoint": "",
          "schema": ""
        },
        "fabric": {
          "list_endpoint": "",
          "schema": ""
        },
        "fgtgroupfilter": {
          "list_endpoint": "",
          "schema": ""
        },
        "fortiguardmessages": {
          "list_endpoint": "",
          "schema": ""
        },
        "fortitokenmobilelicenses": {
          "list_endpoint": "",
          "schema": ""
        },
        "fortitokenmobileprovisioning": {
          "list_endpoint": "",
          "schema": ""
        },
        "fortitokens": {
          "list_endpoint": "",
          "schema": ""
        },
        "ftpservers": {
          "list_endpoint": "",
          "schema": ""
        },
        "iamaccounts": {
          "list_endpoint": "",
          "schema": ""
        },
        "iamusers": {
          "list_endpoint": "",
          "schema": ""
        },
        "ldapusers": {
          "list_endpoint": "",
          "schema": ""
        },
        "licensing": {
          "list_endpoint": "",
          "schema": ""
        },
        "localapiadmin": {
          "list_endpoint": "",
          "schema": ""
        },
        "localgroup-memberships": {
          "list_endpoint": "",
          "schema": ""
        },
        "localusers": {
          "list_endpoint": "",
          "schema": ""
        },
        "logsettings": {
          "list_endpoint": "",
          "schema": ""
        },
        "macdevices": {
          "list_endpoint": "",
          "schema": ""
        },
        "macgroup-memberships": {
          "list_endpoint": "",
          "schema": ""
        },
        "macgroups": {
          "list_endpoint": "",
          "schema": ""
        },
        "oauth": {
          "list_endpoint": "",
          "schema": ""
        },
        "offlinehotpupdate": {
          "list_endpoint": "",
          "schema": ""
        },
        "offlineotp": {
          "list_endpoint": "",
          "schema": ""
        },
        "passwordpolicies": {
          "list_endpoint": "",
          "schema": ""
        },
        "pushauth": {
          "list_endpoint": "",
          "schema": ""
        },
        "pushauthresp": {
          "list_endpoint": "",
          "schema": ""
        },
        "pushpoll": {
          "list_endpoint": "",
          "schema": ""
        },
        "radiusclients": {
          "list_endpoint": "",
          "schema": ""
        },
        "radiuspolicies": {
          "list_endpoint": "",
          "schema": ""
        },
        "radiuspolicyclient": {
          "list_endpoint": "",
          "schema": ""
        },
        "radiususers": {
          "list_endpoint": "",
          "schema": ""
        },
        "realmauth": {
          "list_endpoint": "",
          "schema": ""
        },
        "recovery": {
          "list_endpoint": "",
          "schema": ""
        },
        "scepreqs": {
          "list_endpoint": "",
          "schema": ""
        },
        "scheduledbackupsettings": {
          "list_endpoint": "",
          "schema": ""
        },
        "smtpservers": {
          "list_endpoint": "",
          "schema": ""
        },
        "ssoauth": {
          "list_endpoint": "",
          "schema": ""
        },
        "ssogroup": {
          "list_endpoint": "",
          "schema": ""
        },
        "syslogservers": {
          "list_endpoint": "",
          "schema": ""
        },
        "system": {
          "list_endpoint": "",
          "schema": ""
        },
        "systeminfo": {
          "list_endpoint": "",
          "schema": ""
        },
        "tacplusclients": {
          "list_endpoint": "",
          "schema": ""
        },
        "tacpluspolicies": {
          "list_endpoint": "",
          "schema": ""
        },
        "tacpluspolicyclient": {
          "list_endpoint": "",
          "schema": ""
        },
        "transfertoken": {
          "list_endpoint": "",
          "schema": ""
        },
        "usercerts": {
          "list_endpoint": "",
          "schema": ""
        },
        "userfortitokenpolicy": {
          "list_endpoint": "",
          "schema": ""
        },
        "usergroups": {
          "list_endpoint": "",
          "schema": ""
        },
        "userlockoutpolicy": {
          "list_endpoint": "",
          "schema": ""
        }
      }
```
### operation: Get Specific Local User
#### Description

- Get Local User by ID.

#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Input for user search<br></td><td>Search can be made using - ID or Username or Email<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>
```
  {
        "active": "",
        "address": "",
        "change_password": "",
        "city": "",
        "country": "",
        "custom1": "",
        "custom2": "",
        "custom3": "",
        "email": "",
        "expires_at": "",
        "fido": "",
        "first_name": "",
        "ftk_only": "",
        "ftm_act_method": "",
        "id": "",
        "last_name": "",
        "mail_host": "",
        "mail_routing_address": "",
        "mobile_number": "",
        "phone_number": "",
        "reason": "",
        "recovery_by_question": "",
        "resource_uri": "",
        "state": "",
        "token_auth": "",
        "token_fas": "",
        "token_serial": "",
        "token_type": "",
        "user_groups": [],
        "username": ""
      }
```


### operation: Get Users
This endpoint represents local user resource, namely a user account. This resource can be found in the FortiAuthenticator GUI under Authentication > Local Users..",
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Get Users<br></td><td>No parameters needed<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>
```
  {
            "active": "",
            "address": "",
            "change_password": "",
            "city": "",
            "country": "",
            "custom1": "",
            "custom2": "",
            "custom3": "",
            "email": "",
            "expires_at": "",
            "fido": "",
            "first_name": "",
            "ftk_only": "",
            "ftm_act_method": "",
            "id": "",
            "last_name": "",
            "mail_host": "",
            "mail_routing_address": "",
            "mobile_number": "",
            "phone_number": "",
            "reason": "",
            "recovery_by_question": "",
            "resource_uri": "",
            "state": "",
            "token_auth": "",
            "token_fas": "",
            "token_serial": "",
            "token_type": "",
            "user_groups": [],
            "username": ""
          }
  ```


### operation: Create Local User
This endpoint represents local user resource, namely a user account. This resource can be found in the FortiAuthenticator GUI under Authentication > Local Users."
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Input<br></td><td>Username<br><tr><td>Input<br></td><td>Password<br><tr><td>Input<br></td><td>Email<br><tr><td>Input<br></td><td>First Name<br><tr><td>Input<br></td><td>Last Name<br><tr><td>Input<br></td><td>Account Status (Yes/No) checkbox.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

```
  {
        "active": "",
        "address": "",
        "change_password": "",
        "city": "",
        "country": "",
        "custom1": "",
        "custom2": "",
        "custom3": "",
        "email": "",
        "expires_at": "",
        "fido": "",
        "first_name": "",
        "ftk_only": "",
        "ftm_act_method": "",
        "id": "",
        "last_name": "",
        "mail_host": "",
        "mail_routing_address": "",
        "mobile_number": "",
        "phone_number": "",
        "reason": "",
        "recovery_answer": "",
        "recovery_by_question": "",
        "recovery_question": "",
        "resource_uri": "",
        "state": "",
        "token_auth": "",
        "token_fas": "",
        "token_serial": "",
        "token_type": "",
        "user_groups": [],
        "username": ""
      }
```

### operation: Update Local User Status
Update Local User Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>CheckBox<br></td><td>Activate/Deactivates local user<br>
</td></tr><tr><td>Input<br></td><td>Local User ID input for active/deactive status<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
```
{
        "active": "",
        "address": "",
        "change_password": "",
        "city": "",
        "country": "",
        "custom1": "",
        "custom2": "",
        "custom3": "",
        "email": "",
        "expires_at": "",
        "fido": "",
        "first_name": "",
        "ftk_only": "",
        "ftm_act_method": "",
        "id": "",
        "last_name": "",
        "mail_host": "",
        "mail_routing_address": "",
        "mobile_number": "",
        "phone_number": "",
        "reason": "",
        "recovery_by_question": "",
        "resource_uri": "",
        "state": "",
        "token_auth": "",
        "token_fas": "",
        "token_serial": "",
        "token_type": "",
        "user_groups": [],
        "username": ""
      }
  ```


### operation: Get Specific Ladap User
Get Local Use by filter paramaters
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Prefix List<br></td><td>Name of the Prefix List<br>
</td></tr><tr><td>Address(es) To Delete<br></td><td>IPv4 or IPv6 Address or Addresses (in CSV) to delete from the prefix list<br>
</td></tr></tbody></table>

#### Output
```
{
        "active": "",
        "address": "",
        "change_password": "",
        "city": "",
        "country": "",
        "custom1": "",
        "custom2": "",
        "custom3": "",
        "email": "",
        "expires_at": "",
        "fido": "",
        "first_name": "",
        "ftk_only": "",
        "ftm_act_method": "",
        "id": "",
        "last_name": "",
        "mail_host": "",
        "mail_routing_address": "",
        "mobile_number": "",
        "phone_number": "",
        "reason": "",
        "recovery_by_question": "",
        "resource_uri": "",
        "state": "",
        "token_auth": "",
        "token_fas": "",
        "token_serial": "",
        "token_type": "",
        "user_groups": [],
        "username": ""
      }
  ```
  
### operation: Update LDAP User
Activate/Deactivates LDAP user
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Prefix List<br></td><td>Name of the Prefix List<br>
</td></tr><tr><td>Address(es) To Delete<br></td><td>IPv4 or IPv6 Address or Addresses (in CSV) to delete from the prefix list<br>
</td></tr></tbody></table>

#### Output
```
{
        "active": "",
        "address": "",
        "change_password": "",
        "city": "",
        "country": "",
        "custom1": "",
        "custom2": "",
        "custom3": "",
        "email": "",
        "expires_at": "",
        "fido": "",
        "first_name": "",
        "ftk_only": "",
        "ftm_act_method": "",
        "id": "",
        "last_name": "",
        "mail_host": "",
        "mail_routing_address": "",
        "mobile_number": "",
        "phone_number": "",
        "reason": "",
        "recovery_by_question": "",
        "resource_uri": "",
        "state": "",
        "token_auth": "",
        "token_fas": "",
        "token_serial": "",
        "token_type": "",
        "user_groups": [],
        "username": ""
      }
  ```
  
### operation: Get Specific Radius User
Get Radius Use by filter paramaters - username or ID or email
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>User ID<br></td><td>User ID for query<br>
</td></tr><tr><td>Username<br></td><td>Username of the user<br></td></tr><tr><td>Email<br></td><td>Email address of the user to query<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
```
{
        "meta": {
          "limit": "",
          "next": "",
          "offset": "",
          "previous": "",
          "total_count": ""
        },
        "objects": [
          {
            "active": "",
            "dn": "",
            "email": "",
            "fido": "",
            "first_name": "",
            "ftm_act_method": "",
            "id": "",
            "last_name": "",
            "mobile_number": "",
            "reason": "",
            "recovery_by_question": "",
            "resource_uri": "",
            "server_address": "",
            "server_name": "",
            "token_auth": "",
            "token_serial": "",
            "token_type": "",
            "username": ""
          }
        ]
      }
  ```
  
### operation: Update Radius User
Active/Deactive Radius user
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Input<br></td><td>UserID to active/deactive user. Use the checkbox option.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
```
  {
        "active": "",
        "address": "",
        "change_password": "",
        "city": "",
        "country": "",
        "custom1": "",
        "custom2": "",
        "custom3": "",
        "email": "",
        "expires_at": "",
        "fido": "",
        "first_name": "",
        "ftk_only": "",
        "ftm_act_method": "",
        "id": "",
        "last_name": "",
        "mail_host": "",
        "mail_routing_address": "",
        "mobile_number": "",
        "phone_number": "",
        "reason": "",
        "recovery_by_question": "",
        "resource_uri": "",
        "state": "",
        "token_auth": "",
        "token_fas": "",
        "token_serial": "",
        "token_type": "",
        "user_groups": [],
        "username": ""
      }
  ```

### operation: User Lockout Policy Info
This endpoint is used to query and edit user account lockout policy settings including the maximum number of failed login attempts, specify the lockout period, and enable inactive user lockouts.

#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Paramters<br></td><td>No Parameters required<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: 
```
  {
        "failed_login_lockout": "",
        "failed_login_lockout_max_attempts": "",
        "failed_login_lockout_period": "",
        "failed_login_lockout_permanent": "",
        "inactivity_lockout": "",
        "inactivity_lockout_period": ""
      }
  ```


## Included playbooks
The `Sample - FortiAuthenticator - 1.0.0` playbook collection comes bundled with the FortiAuthenticator connector. These playbooks contain steps using which you can perform all supported actions.

