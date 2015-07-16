from number import app

repeat = 100
op = "multiplication"
@profile
def no_ifthen_function():
    for counter in range(1, repeat):
        resp = app.test_client().get('/4/2/?operation={}'.format(op))

@profile
def ifthen_function():
    for counter in range(1,repeat):
        resp = app.test_client().get('/ifthen/4/2/?operation={}'.format(op))
        
no_ifthen_function()
ifthen_function()

# in a terminal:
# pip install -U memory_profiler
# pip install psutil
# python -m memory_profiler number_memory.py
