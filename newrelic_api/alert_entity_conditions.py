from .base import Resource
from newrelic_api.exceptions import NoEntityException


class AlertEntityConditions(Resource):
    """
    An interface for interacting with the NewRelic Alert Entity Conditions API.
    """
    def add(self, entity_id, entity_type, condition_id):
        """
        This API endpoint allows you to add an entity to a specified Alerts condition.
        Note: Admin User’s API Key is required. 
        Entity type options (Synthetics is not yet supported):
            BrowserApplication
            Application
            MobileApplication
            Server
            KeyTransaction
            Plugin

        {
          "condition": {
            "id": "integer",
            "type": "string",
            "name": "string",
            "enabled": "boolean",
            "entities": [
              "integer"
            ],
            "metric": "string",
            "runbook_url": "string",
            "terms": [
              {
                "duration": "string",
                "operator": "string",
                "priority": "string",
                "threshold": "string",
                "time_function": "string"
              }
            ],
            "user_defined": {
              "metric": "string",
              "value_function": "string"
            }
          }
        }

        """
        filters = [
            'entity_type={0}'.format(entity_type),
            'condition_id={0}'.format(condition_id)
        ]

        return self._put(
            url='{0}alerts_entity_conditions/{1}.json'.format(self.URL, entity_id),
            headers=self.headers,
            params=self.build_param_string(filters)
        )

    def remove(self, entity_id, entity_type, condition_id):
        filters = [
            'entity_type={0}'.format(entity_type),
            'condition_id={0}'.format(condition_id)
        ]

        return self._delete(
            url='{0}alerts_entity_conditions/{1}.json'.format(self.URL, entity_id),
            headers=self.headers,
            params=self.build_param_string(filters)
        )


###
### TO DO: Implement "list"
###
