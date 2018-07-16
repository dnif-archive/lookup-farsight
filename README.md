# FARSIGHT SECURITY DNSDB

https://www.farsightsecurity.com/solutions/dnsdb/

## Overview

Farsight DNSDB is a passive DNS historical database that provides a unique/fact-based,multifaceted view of the configuration of the global Internet infrastructure.
It stores both the passive DNS data available via Farsight Security’s SIE(Security Information Exchange) as well as the authoritative DNS data.
## REAL TIME UPDATES

Leaverging Farsight DNSDB with Polarity, threat investigators,responders and security analysts can now be presented with critical history about an IP address or domain name in real-time. It contains more than 100 DNS records and are continously updated in real time.
## DETAILED RESULTS
DNSDB users can access DNSDB via a Web UI or a RESTful API.The web search interface offers two lookup modes,”rrset” and”rdata”, which are selected using the radio buttons at the top of the search form.The "rrset" lookup queries DNSDB's RRset index, which supports "forward" lookups based on the owner name of an RRset.The "rdata" lookup queries DNSDB's Rdata index, which supports "inverse" lookups based on Rdata record values.

## Lookups integrated with Farsight

##### Note

`testingintegrations` is a DNIF event store that can be uploaded for testing.

### Retrieve “rrset” whose owner name is the URL given

- input : A URL for which Farsight DNSDB will retrieve “rrset”

```
_fetch $URL from farsightsample limit 1
>>_lookup farsight get_url_report $URL
```

###### Sample walkthrough screenshot of get_url_report

![get_url_report](https://user-images.githubusercontent.com/40236269/42689961-2b2dedce-86c0-11e8-9947-5cdff596d7a0.jpg)


The lookup call returns output in the following structure for available data

|Field|Description|
|-|-|
|$FSCount|The number of times the RRset was observed via passive DNS replication.|
|$FSFirstseen|A UTC timestamp with seconds granularity indicating the first time an RRset was seen in the given bailiwick via passive DNS replication.|
|$FSLastseen|A UTC timestamp with seconds granularity indicating the last time an RRset was seen in the given bailiwick via passive DNS replication.|
|$FSRRname|The owner name of the RRset in DNS presentation format.|
|$FSBailiwick|The "bailiwick" of an RRset in DNSDB observed via passive DNS replication is the closest enclosing zone delegated to a nameserver which served the RRset.|
|$FSRdata|An array of one or more Rdata values. The Rdata values are converted to the standard presentation format based on the rrtype value. If the encoder lacks a type-specific presentation format for the RRset's rrtype, then the RFC 3597 generic Rdata encoding will be used.|
|$FSRRtype|The resource record type of the RRset, either using the standard DNS type mnemonic, or an RFC 3597 generic type, i.e. the string TYPE immediately followed by the decimal RRtype number.|

### Retrieve resource records whose “rdata” is the IPv4 address

- input :A IPv4 address for which Farsight DNSDB will provide all the resource records.

```
_fetch $SrcIP from farsightsample limit 1
>>_lookup farsight get_ipv4_report $SrcIP
```

###### Sample walkthrough screenshot of get_ipv4_report

![get_ipv4_report](https://user-images.githubusercontent.com/40236269/42689986-3f0922a0-86c0-11e8-8d03-0e86c5cd2ed4.jpg)


The lookup call returns output in the following structure for available data

|Field|Description|
|-|-|
|$FSCount|The number of times the resource record was observed via passive DNS replication.|
|$FSFirstseen|UNIX epoch timestamps with second granularity indicating the first time resource record was observed via passive DNS replication.|
|$FSLastseen|UNIX epoch timestamps with second granularity indicating last times  resource record was observed via passive DNS replication.|
|$FSZonefirstseen|UNIX epoch timestamps with second granularity indicating  first time  resource record was observed via zone file import.|
|$FSZonelastseen|UNIX epoch timestamps with second granularity indicating  last time resource record was observed via zone file import.|
|$FSRRname|The owner name of the resource record in DNS presentation format.|
|$FSRRtype|The resource record type of the resource record, either using the standard DNS type mnemonic, or an RFC 3597 generic type, i.e. the string TYPE immediately followed by the decimal RRtype number|
|$FSRdata|The record data value. The Rdata value is converted to the standard presentation format based on the rrtype value. If the encoder lacks a type-specific presentation format for the resource record's type, then the RFC 3597 generic Rdata encoding will be used.|

### Retrieve resource records whose “rdata” is the IPv6 addres

- input : A IPv6 address for which Farsight DNSDB will provide all the resource records.

```
_fetch $Ipv6 from farsightsample limit 1
>>_lookup farsight get_ipv6_report $Ipv6
```

###### Sample walkthrough screenshot of get_ipv6_report

![get_ipv6_report](https://user-images.githubusercontent.com/40236269/42690009-50fd5616-86c0-11e8-8e5b-348296bf0434.jpg)

The lookup call returns output in the following structure for available data

|Field|Description|
|-|-|
|$FSCount|The number of times the resource record was observed via passive DNS replication.|
|$FSFirstseen|UNIX epoch timestamps with second granularity indicating the first time resource record was observed via passive DNS replication.|
|$FSLastseen|UNIX epoch timestamps with second granularity indicating last times  resource record was observed via passive DNS replication.|
|$FSRRname|The owner name of the resource record in DNS presentation format.|
|$FSRRtype|The resource record type of the resource record, either using the standard DNS type mnemonic, or an RFC 3597 generic type, i.e. the string TYPE immediately followed by the decimal RRtype number|
|$FSRdata|The record data value. The Rdata value is converted to the standard presentation format based on the rrtype value. If the encoder lacks a type-specific presentation format for the resource record's type, then the RFC 3597 generic Rdata encoding will be used.|

### Retrieve resource records whose “rdata” is the nameserver

- input :A Nameserver for which Farsight DNSDB will provide all the resource records.

```
_fetch $Nameserver from farsightsample limit 1
>>_lookup farsight get_nameserver_report $Nameserver
```

###### Sample walkthrough screenshot of get_nameserver_report

![get_nameserver_report](https://user-images.githubusercontent.com/40236269/42690022-6276d12e-86c0-11e8-9426-72a0a2f30591.jpg)


The lookup call returns output in the following structure for available data

|Field|Description|
|-|-|
|$FSCount|The number of times the resource record was observed via passive DNS replication.|
|$FSZonefirstseen|UNIX epoch timestamps with second granularity indicating  first time  resource record was observed via zone file import.|
|$FSZonelastseen|UNIX epoch timestamps with second granularity indicating  last time resource record was observed via zone file import.|
|$FSRRname|The owner name of the resource record in DNS presentation format.|
|$FSRRtype|The resource record type of the resource record, either using the standard DNS type mnemonic, or an RFC 3597 generic type, i.e. the string TYPE immediately followed by the decimal RRtype number|
|$FSRdata|The record data value. The Rdata value is converted to the standard presentation format based on the rrtype value. If the encoder lacks a type-specific presentation format for the resource record's type, then the RFC 3597 generic Rdata encoding will be used.|

### Retrieve resource records with mailexchange server

- input :A Mailexchange server  for which Farsight DNSDB will provide all the resource records.

```
_fetch $Mailexchange from farsightsample limit 1
>>_lookup farsight get_mailexchange_report $Mailexchange
```

###### Sample walkthrough screenshot of get_mailexchange_report

![get_mailexchange_report](https://user-images.githubusercontent.com/40236269/42690039-78886a72-86c0-11e8-9ff3-bc66d1d701eb.jpg)


The lookup call returns output in the following structure for available data

|Field|Description|
|-|-|
|$FSCount|The number of times the resource record was observed via passive DNS replication.|
|$FSFirstseen|UNIX epoch timestamps with second granularity indicating the first time resource record was observed via passive DNS replication.|
|$FSLastseen|UNIX epoch timestamps with second granularity indicating last times  resource record was observed via passive DNS replication.|
|$FSRRname|The owner name of the resource record in DNS presentation format.|
|$FSRRtype|The resource record type of the resource record, either using the standard DNS type mnemonic, or an RFC 3597 generic type, i.e. the string TYPE immediately followed by the decimal RRtype number|
|$FSRdata|The record data value. The Rdata value is converted to the standard presentation format based on the rrtype value. If the encoder lacks a type-specific presentation format for the resource record's type, then the RFC 3597 generic Rdata encoding will be used.|

## Using the Farsight API and DNIF
The Farsight API is found on github at

https://github.com/dnif/lookup-farsight

### Getting started with Farsight API and DNIF

1. ###### Login to your Data Store, Correlator, and A10 containers.  
   [ACCESS DNIF CONTAINER VIA SSH](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. ###### Move to the `/dnif/<Deployment-key>/lookup_plugins` folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/lookup_plugins/
```
3. ###### Clone using the following command
```  
git clone https://github.com/dnif/lookup-farsight.git farsight
```
4. ###### Move to the `/dnif/<Deployment-key>/lookup_plugins/farsight/` folder path and open dnifconfig.yml configuration file     

Replace the tag: <Add_your_api_key_here> with your Farsight api key
```
lookup_plugin:
  FS_API_KEY: <Add_your_api_key_here>
```
