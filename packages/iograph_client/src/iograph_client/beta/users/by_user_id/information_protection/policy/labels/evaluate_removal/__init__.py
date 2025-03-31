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
from iograph_models.beta.evaluate_removal_post_request import Evaluate_removalPostRequest
from iograph_models.beta.evaluate_removal_post_response import Evaluate_removalPostResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class EvaluateRemovalRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/informationProtection/policy/labels/evaluateRemoval", path_parameters)

	async def post(
		self,
		body: Evaluate_removalPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Evaluate_removalPostResponse:
		"""
		Invoke action evaluateRemoval
		Indicate to the consuming application what actions it should take to remove the label information. Given contentInfo as an input, which includes existing content metadata key/value pairs, the API returns an informationProtectionAction that contains some combination of one of more of the following: 
		Find more info here: https://learn.microsoft.com/graph/api/informationprotectionlabel-evaluateremoval?view=graph-rest-beta
		"""
		tags = ['users.informationProtection']

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
		return await self.request_adapter.send_async(request_info, Evaluate_removalPostResponse, error_mapping)


	def with_url(self, raw_url: str) -> EvaluateRemovalRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EvaluateRemovalRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EvaluateRemovalRequest(self.request_adapter, self.path_parameters)

