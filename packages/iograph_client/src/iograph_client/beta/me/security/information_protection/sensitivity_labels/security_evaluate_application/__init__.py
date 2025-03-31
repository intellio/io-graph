# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_evaluate_application_post_response import Security_evaluate_applicationPostResponse
from iograph_models.beta.security_evaluate_application_post_request import Security_evaluate_applicationPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SecurityEvaluateApplicationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/security/informationProtection/sensitivityLabels/microsoft.graph.security.evaluateApplication", path_parameters)

	async def post(
		self,
		body: Security_evaluate_applicationPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Security_evaluate_applicationPostResponse:
		"""
		Invoke action evaluateApplication
		Compute the sensitivity label that should be applied and return the set of actions that must be taken to correctly label the information. This API is useful when a label should be set manually or explicitly by a user or service, rather than automatically based on file contents. Given contentInfo, which includes existing content metadata key-value pairs, and labelingOptions as an input, the API returns an informationProtectionAction object that contains one of more of the following: 
		Find more info here: https://learn.microsoft.com/graph/api/security-sensitivitylabel-evaluateapplication?view=graph-rest-beta
		"""
		tags = ['me.security']

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
		return await self.request_adapter.send_async(request_info, Security_evaluate_applicationPostResponse, error_mapping)


	def with_url(self, raw_url: str) -> SecurityEvaluateApplicationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SecurityEvaluateApplicationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SecurityEvaluateApplicationRequest(self.request_adapter, self.path_parameters)

