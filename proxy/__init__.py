import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(f"This HTTP triggered function executed successfully.", headers={'content-type':'application/json', 'Set-Cookie':'cross-site-cookie=bar; SameSite=None; Secure; HttpOnly', 'Access-Control-Allow-Origin':'https://ambitious-plant-090f10f1e.1.azurestaticapps.net', 'Access-Control-Allow-Credentials':'true'}, status_code=200)
    
