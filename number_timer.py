from number import app
from timer import Timer
import matplotlib.pyplot as plt

repeat = 10000
no_ifthen_list = []
ifthen_list = []
op = "multiplication"

for counter in range(1, repeat):
    with Timer() as t:
        with app.app_context():
            resp = app.test_client().get('/4/2/?operation={}'.format(op))
    no_ifthen_list.append(t.secs*1000)
        
for counter in range(1,repeat):
    with Timer() as t:
        with app.app_context():
            resp = app.test_client().get('/ifthen/4/2/?operation={}'.format(op))
    ifthen_list.append(t.secs*1000)
        
plt.hist(no_ifthen_list, bins=200, histtype="stepfilled", normed=True, color="blue", label='No If-Then')
plt.hist(ifthen_list, bins=200, histtype="stepfilled", normed=True, color="red", alpha=0.5, label="If-Then")
plt.xlabel("Time (milisecs)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
