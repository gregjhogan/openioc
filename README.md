# openioc
Control your car inputs (e.g. switches) and outputs (e.g. lights) with software over CAN

## Discovery
CAN bus protocols such as [UDS](https://en.wikipedia.org/wiki/Unified_Diagnostic_Services) and [KWP2000](https://en.wikipedia.org/wiki/Keyword_Protocol_2000) define services that perform ECU input/output tests (lights, blinkers, wipers, etc...). Automotive manufacturers often release software for repair shops that can perform these tests, which makes it possible to record the tests.  The repair shop software often does not reveal all possible tests, but even one test can reveal patterns you can expand on to search for additional input/output tests.

## Limitations
Sometimes it isn't as easy as plugging into the OBD-II port and replaying messages.  Vehicles often have multiple CAN buses, which are sometimes not easily accessible.  An ECU acting as a gateway between other ECUs may perform address translation or block your messages.  Additionally, sometimes specific diagnostic session modes are required which may or may not require a security access key exchange.
