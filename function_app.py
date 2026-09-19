import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(
        route="http_trigger_Aula_1",
        methods=["GET"]
)
def http_trigger_Aula_1(req: func.HttpRequest) -> func.HttpResponse:
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
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.timer_trigger(
    schedule = "0 * * * * *",
    arg_name = "myTimer",
    run_on_startup = False,              
    use_monitor=False

) 
def timer_trigger_2(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


# Adicionar outro timer_trigger igual o anterior que deverar se conectado ao def http_trigger_Aula_1
@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def timer_trigger_3(myTimer: func.TimerRequest) -> None:

    url = "http://localhost:7071/api/http_trigger_Aula_1?name=Robertha"

    try:
        resposta = requests.get(url, timeout=10)

        logging.info(f"Resposta da HTTP Function: {resposta.text}")

    except requests.RequestException as erro:
        logging.error(f"Erro ao chamar a HTTP Function: {erro}")