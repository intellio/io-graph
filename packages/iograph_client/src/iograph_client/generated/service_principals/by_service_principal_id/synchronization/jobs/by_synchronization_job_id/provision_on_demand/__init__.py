# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.provision_on_demand_post_request import Provision_on_demandPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.string_key_string_value_pair import StringKeyStringValuePair


class ProvisionOnDemandRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization/jobs/{synchronizationJob%2Did}/provisionOnDemand"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Provision_on_demandPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> StringKeyStringValuePair:
		"""
		Invoke action provisionOnDemand
		Select a user and provision the account on-demand. The rate limit for this API is 5 requests per 10 seconds.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationjob-provisionondemand?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.synchronization']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, StringKeyStringValuePair, error_mapping)


