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
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_evaluate_classification_results_post_response import Security_evaluate_classification_resultsPostResponse
from iograph_models.beta.security_evaluate_classification_results_post_request import Security_evaluate_classification_resultsPostRequest


class SecurityEvaluateClassificationResultsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/security/informationProtection/sensitivityLabels/microsoft.graph.security.evaluateClassificationResults", path_parameters)

	async def post(
		self,
		body: Security_evaluate_classification_resultsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Security_evaluate_classification_resultsPostResponse:
		"""
		Invoke action evaluateClassificationResults
		Use the classification results to compute the sensitivity label that should be applied and return the set of actions that must be taken to correctly label the information. This API is useful when a label should be set automatically based on classification of the file contents, rather than labeled directly by a user or service.  To evaluate based on classification results, provide the contentInfo, which includes existing content metadata key-value pairs, and classification results. The API returns an informationProtectionAction that contains one of more of the following:
		Find more info here: https://learn.microsoft.com/graph/api/security-sensitivitylabel-evaluateclassificationresults?view=graph-rest-beta
		"""
		tags = ['users.security']

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
		return await self.request_adapter.send_async(request_info, Security_evaluate_classification_resultsPostResponse, error_mapping)


	def with_url(self, raw_url: str) -> SecurityEvaluateClassificationResultsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SecurityEvaluateClassificationResultsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SecurityEvaluateClassificationResultsRequest(self.request_adapter, self.path_parameters)

