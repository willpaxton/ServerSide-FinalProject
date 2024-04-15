FROM grafana/grafana

# https://medium.com/swlh/easy-grafana-and-docker-compose-setup-d0f6f9fcec13

# Disable Login form or not
# ENV GF_AUTH_DISABLE_LOGIN_FORM "true"
# Allow anonymous authentication or not
ENV GF_AUTH_ANONYMOUS_ENABLED="true"
# Role of anonymous user
ENV GF_AUTH_ANONYMOUS_ORG_ROLE="Admin"
# Install plugins here our in your own config file
ENV GF_INSTALL_PLUGINS="marcusolsson-json-datasource"

ENV GF_AUTH_BASIC_ENABLED=false

ENV GF_AUTH_PROXY_HEADER_NAME=X-WEBAUTH-USER

# Add provisioning
ADD ./provisioning /etc/grafana/provisioning
# Add configuration file
ADD ./grafana.ini /etc/grafana/grafana.ini
# Add dashboard json files
ADD ./dashboards /etc/grafana/dashboards

# should I add a run to create a volume???