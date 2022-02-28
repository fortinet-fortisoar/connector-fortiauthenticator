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

### operation: Run Operation Command
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody>
<tr><td>Method<br></td><td>RPC Command to run<br></td>
</tr><tr><td>Custom Method<br></td><td>if the command is not in the list above (Method) you can use a custom one as a Custom method. To get the exact command syntax refer to this example on JunOS: [show route|display xml rpc] <br>
</td></tr><tr><td>Method Parameters<br></td><td>Method parameters in JSON. For example, if the action is get-interface-information the parameter(s) could be [{'interface-name':'ge-0/0/0'}]<br>
</td></tr></tbody></table>


#### Output
The output contains the following populated JSON schema: <JSON Output>

### operation: Run Configuration Command
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody>
<tr><td>Request Payload<br></td><td>HTTP/POST XML Payload as documented here https://www.juniper.net/documentation/us/en/software/junos/rest-api/rest-api.pdf<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>

### operation: Get Address Set
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Address Set<br></td><td>Name of the address set<br>
</td></tr><tr><td>Get Entries Count<br></td><td>If checked, returns only entries count instead of the entries data<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>


### operation: Add an Object to Global Address Set
#### Requirements

- This action will add object(s) (IP/FQDN/Wildcard) to an address set of the **global address book** so the address set (defined by the name you use in the Address Set parameter) can be used with any security policy from and to any zone.
- The action doesn't create the security policy, the users have to do it themselves and associate the Address-Set with any policy of their choosing.
- A maximum of 1024 address (IPv4) can be created. each IPv6 takes up a space of 4 IPv4s.
- You can use **Get Address Set** /count Action to check how many records are there already.

#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Address Set<br></td><td>Name of the address set<br>
</td></tr><tr><td>Object Types<br></td><td>Type of the object(s) to add, only one type is supported at a time. Wildcard format is: A.B.C.D/E.F.G.H<br>
</td></tr><tr><td>Object(s) To Add<br></td><td>IP address, an FQDN or a wildcard to add, for multiple entries use CSV format such as host1.domain.com,host2.domain.com if the type is dns-name<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>


### operation: Delete Object from Global Address Set
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Address set<br></td><td>Name of the address set<br>
</td></tr><tr><td>Object Types<br></td><td>Type of the object(s) to delete, only one type is supported at a time<br>
</td></tr><tr><td>Object(s) To Delete<br></td><td>IP address, an FQDN or a wildcard to delete, for multiple entries use CSV format such as host1.domain.com,host2.domain.com if the type is dns-name<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>


### operation: Get Prefix List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Prefix List<br></td><td>Name of the Prefix List<br>
</td></tr><tr><td>Get Entries Count<br></td><td>If checked, returns only entries count instead of the entries data<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>
85325
- The action only creates and populates prefix list, you will need to associate it with a firewall filter. For example if the prefix list you create is called **Bad-IPs** (defined by the prefix list parameter) you will need to add the below configuration to use the prefix list to block traffic from/to its addresses on ge-0/0/0.0.

```bash
set firewall family inet filter Blocked-Group term 1 from prefix-list Bad-IPs
set firewall family inet filter Blocked-Group term 1 then discard
set firewall family inet filter Blocked-Group term 99 then accept
set interfaces ge-0/0/0.0 family inet filter input Blocked-Group
set interfaces ge-0/0/0.0 family inet filter ouput Blocked-Group
```

#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Prefix List<br></td><td>Name of the Prefix List<br>
</td></tr><tr><td>Address(es) To Add<br></td><td>IPv4 or IPv6 Address or Addresses (in CSV) to add to the prefix list<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>


### operation: Delete Address(es) from a Prefix List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Prefix List<br></td><td>Name of the Prefix List<br>
</td></tr><tr><td>Address(es) To Delete<br></td><td>IPv4 or IPv6 Address or Addresses (in CSV) to delete from the prefix list<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema: <JSON Output>


## Included playbooks
The `Sample - juniper-junos - 1.0.0` playbook collection comes bundled with the Juniper JunOS connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Juniper JunOS connector.

