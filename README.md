## python-azure-appInsights-Integration
<br />
OpenCensus is a set of open source libraries to allow collection of distributed tracing, metrics and logging telemetry. Through the use of Azure Monitor exporters, you will be able to send this collected telemetry to Application insights. This article walks you through the process of setting up OpenCensus and Azure Monitor Exporters for Python to send your monitoring data to Azure Monitor.
<br />
### Install the OpenCensus Azure Monitor exporters

azure-functions <br />
opencensus-extension-azure-functions <br />
opencensus-ext-requests <br />
<br />
  ```sh
  pip install -r requirements.txt
  ```
Although entering values is helpful for demonstration purposes, ultimately we want to emit the log data to Azure Monitor. Pass your connection string directly into the exporter. Or, you can specify it in an environment variable, APPLICATIONINSIGHTS_CONNECTION_STRING.

### Function App Configuration
<br />
Step 1: Enable Application Insight on Function App <br />
![image](https://user-images.githubusercontent.com/38012945/149370476-7edf757c-165a-4c63-bbce-1bf50bb0ed5b.png)
<br />
Step 2: Ensure the Instrument key and connection string is added to Function app's setting <br />
![image](https://user-images.githubusercontent.com/38012945/149370696-c9495ac5-523e-4360-9346-7151f9fe4114.png)

