from fasthtml.common import *
from starlette.background import BackgroundTask
import time
import httpx
# need to push

app, rt = fast_app()

db = database(':memory:')

class TStamp: requestTime: int; responseTime: int

tstamps = db.create(TStamp, pk='requestTime')

def TaskSubmit(requestTime:int):
    client = httpx.Client()
    response = client.post(f'http://127.0.0.1:5001/?ts={requestTime}')
    tstamps.insert(**response.json())

@rt
def Submit():
    requestTime = int(time.time())
    task = BackgroundTask(TaskSubmit, requestTime=requestTime)
    return P(f'request submitted at: {requestTime}'), task

@rt
def ShowTStamps(): return Ul(map(Li, tstamps()))

@rt
def index():
    return Titled('Background Task Dashboard',
                  P(Button('Press to call slow service',
                           hx_post=Submit, hx_target='#res')),
                           H2('Responses From Tasks'),
                           P('', id='res'),
                           Div(Ul(map(Li, tstamps())),
                               hx_get=ShowTStamps, hx_trigger='every 5s')
                           )

serve()