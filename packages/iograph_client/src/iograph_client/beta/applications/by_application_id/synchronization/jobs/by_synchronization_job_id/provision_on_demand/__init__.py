# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.provision_on_demand_post_request import Provision_on_demandPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.string_key_string_value_pair import StringKeyStringValuePair


class ProvisionOnDemandRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/jobs/{synchronizationJob%2Did}/provisionOnDemand", path_parameters)

	async def post(
		self,
		body: Provision_on_demandPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> StringKeyStringValuePair:
		"""
		Invoke action provisionOnDemand
		Select a user and provision the account on-demand. The rate limit for this API is 5 requests per 10 seconds. No user or group will be provisioned on-demand that would not have been provisioned through the regular provisioning cycles.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationjob-provisionondemand?view=graph-rest-beta
		"""
		tags = ['applications.synchronization']

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


	def with_url(self, raw_url: str) -> ProvisionOnDemandRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ProvisionOnDemandRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ProvisionOnDemandRequest(self.request_adapter, self.path_parameters)

