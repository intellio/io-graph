# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.access_review_history_instance import AccessReviewHistoryInstance
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class GenerateDownloadUriRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/historyDefinitions/{accessReviewHistoryDefinition%2Did}/instances/{accessReviewHistoryInstance%2Did}/generateDownloadUri", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewHistoryInstance:
		"""
		Invoke action generateDownloadUri
		Generates a URI for an accessReviewHistoryInstance object the status for which is done. Each URI can be used to retrieve the instance's review history data. Each URI is valid for 24 hours and can be retrieved by fetching the downloadUri property from the accessReviewHistoryInstance object.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewhistoryinstance-generatedownloaduri?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		return await self.request_adapter.send_async(request_info, AccessReviewHistoryInstance, error_mapping)


	def with_url(self, raw_url: str) -> GenerateDownloadUriRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GenerateDownloadUriRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GenerateDownloadUriRequest(self.request_adapter, self.path_parameters)

