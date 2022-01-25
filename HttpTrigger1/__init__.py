import logging

import azure.functions as func
from opencensus.extension.azure.functions import OpenCensusExtension
from opencensus.trace import config_integration

config_integration.trace_integrations(['requests'])

OpenCensusExtension.configure()

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.", headers={'content-type':'text/html', 'Set-Cookie':'cross-site-cookie=bar; SameSite=None; Secure; HttpOnly', 'Access-Control-Allow-Origin':'https://yellow-moss-018637f10.1.azurestaticapps.net', 'Access-Control-Allow-Credentials':'true'}, status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
