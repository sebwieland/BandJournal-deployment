import requests
from requests.auth import HTTPBasicAuth

# Grafana instance URL and credentials
grafana_url = 'http://localhost:3000'
username = 'admin'
password = 'password'

# Create a new datasource for Prometheus
datasource_url = f'{grafana_url}/api/datasources'
datasource_data = {
    'name': 'Prometheus',
    'type': 'prometheus',
    'url': 'http://host.docker.internal:9090',
    'access': 'proxy',
    'isDefault': True
}
response = requests.post(datasource_url, auth=HTTPBasicAuth(username, password), json=datasource_data)
print(response)
# Create a new dashboard with the desired metrics
# dashboard_url = f'{grafana_url}/api/dashboards/db'
# dashboard_data = {
#     'dashboard': {
#         'title': 'My Dashboard',
#         'rows': [
#             {
#                 'title': 'Row 1',
#                 'panels': [
#                     {
#                         'id': 1,
#                         'title': 'Panel 1',
#                         'type': 'graph',
#                         'span': 12,
#                         'targets': [
#                             {
#                                 'expr': 'metric_name',
#                                 'refId': 'A',
#                                 'datasource': 'Prometheus'
#                             }
#                         ]
#                     }
#                 ]
#             }
#         ]
#     },
#     'folderId': 0,
#     'overwrite': True
# }
# response = requests.post(dashboard_url, auth=HTTPBasicAuth(username, password), json=dashboard_data)

