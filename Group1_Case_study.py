from multiprocessing.dummy import Manager
from ncclient import manager
import requests
import xml.dom.minidom

m= manager.connect(
	host = "192.168.56.4",
	port = 830,
	username = "cisco",
	password = "cisco123!",
	hostkey_verify = False
)

netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>Group1</hostname>
    </native>
</config>
"""

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                    <description>Case study loopback1</description>
                        <ip>
                            <address>
                                <primary>
                                    <address>10.1.1.1</address>
                                    <mask>255.255.255.0</mask>
                                </primary>
                            </address>
                        </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>2</name>
                    <description>case study loopback2</description>
                        <ip>
                            <address>
                                <primary>
                                    <address>10.2.2.2</address>
                                    <mask>255.255.255.0</mask>
                                </primary>
                            </address>
                        </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_ospf = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
            <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">  
                <id>1</id>
                <router-id>1.1.1.1</router-id>
                <network>
                    <ip>10.1.1.5</ip>
                    <mask>0.0.0.0</mask>
                    <area>0</area>
                </network>
                <network>
                    <ip>192.168.56.4</ip>
                    <mask>0.0.0.0</mask>
                    <area>0</area>
                </network>
            </ospf>
        </router>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_ospf)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


netconf_ipv6 = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
                <description>Interface G1</description>
                    <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                        <address>
                            <ip>2001:db8:0000::1</ip>
                            <prefix-length>64</prefix-length>
                        </address>
                    </ipv6>
        </interface>
    </interfaces>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

a = manager.connect(
	host = "192.168.56.3",
	port = 830,
	username = "cisco",
	password = "cisco123!",
	hostkey_verify = False
)
netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>Arvin</hostname>
    </native>
</config>
"""

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                    <description>Case study loopback1</description>
                        <ip>
                            <address>
                                <primary>
                                    <address>10.3.3.3</address>
                                    <mask>255.255.255.0</mask>
                                </primary>
                            </address>
                        </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = a.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>2</name>
                    <description>case study loopback2</description>
                        <ip>
                            <address>
                                <primary>
                                    <address>10.4.4.4</address>
                                    <mask>255.255.255.0</mask>
                                </primary>
                            </address>
                        </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = a.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_ospf = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
            <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">  
                <id>2</id>
                <router-id>2.2.2.2</router-id>
                <network>
                    <ip>10.2.2.5</ip>
                    <mask>0.0.0.0</mask>
                    <area>0</area>
                </network>
                <network>
                    <ip>192.168.56.3</ip>
                    <mask>0.0.0.0</mask>
                    <area>0</area>
                </network>
            </ospf>
        </router>
    </native>
</config>
"""
netconf_reply = a.edit_config(target="running", config = netconf_ospf)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_ipv6 = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
                <description>Interface G1</description>
                    <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                        <address>
                            <ip>2001:db8:0000::2</ip>
                            <prefix-length>64</prefix-length>
                        </address>
                    </ipv6>
        </interface>
    </interfaces>
</config>
"""
netconf_reply = a.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



access_token = 'MGI2OTRmMDEtMWVhMS00NmY2LWExZDMtOGViNDFmYjg3NDMzOTNkNzM1ZTktYmE5_P0A1_d31bbd0b-8840-4794-8b3b-ed77b0194b3b'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vN2NhYjVlZjAtN2UwNy0xMWVkLThkZGUtZjk1YTc4MmY4OWU0'
message = 'Main router of group 1(csrvk1v) is acknowledge by router through ospf succesfully'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
