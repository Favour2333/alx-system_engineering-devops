Issue Summary

Duration of the outage: From 2:00 PM to 5:00 PM EST on May 10th, 2023.

Impact: The e-commerce website was down for all users during the outage period. Users were unable to access the website, place orders or make payments. The website received a high volume of complaints via email and social media. The outage affected 100% of users who attempted to access the website during the period.

Root cause: The outage was caused by a configuration error in the website's load balancer.

Timeline

2:00 PM EST: The website became unresponsive and returned error messages when users attempted to access it. The issue was detected by monitoring alerts.
2:05 PM EST: Engineers investigated the issue and determined that the website was down due to a high volume of traffic overwhelming the load balancer.
2:15 PM EST: Engineers scaled up the number of backend servers to handle the increased traffic, but the issue persisted.
2:30 PM EST: Further investigation revealed that the load balancer was misconfigured, causing it to route traffic incorrectly.
3:00 PM EST: The misconfiguration was corrected, and the load balancer was restarted.
3:30 PM EST: Engineers verified that the website was functioning correctly and that traffic was being routed properly.
5:00 PM EST: The website was fully restored, and users were able to access it without any issues.
Root Cause and Resolution

The root cause of the outage was a misconfiguration in the load balancer, which caused traffic to be routed incorrectly. Specifically, the load balancer was set up to send traffic to only one of the backend servers, instead of distributing the traffic evenly across all the servers. This caused that server to become overloaded and unable to handle the volume of traffic.

To resolve the issue, engineers corrected the configuration of the load balancer, ensuring that traffic was distributed evenly across all the backend servers. Additionally, the load balancer was restarted to ensure that the corrected configuration was applied.

Corrective and Preventative Measures

To prevent a similar issue from occurring in the future, the following measures will be implemented:

Regular load balancer configuration audits to identify and correct any misconfigurations that may arise.
Automated load balancer testing to verify that traffic is being distributed correctly across all backend servers.
Implementation of an automatic failover mechanism to switch traffic to a backup load balancer in the event of a failure.
This concludes the postmortem report for the e-commerce website outage on May 10th, 2023.
