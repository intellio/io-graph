# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_access_review_history_definition_id import ByAccessReviewHistoryDefinitionIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.access_review_history_definition import AccessReviewHistoryDefinition
from iograph_models.models.access_review_history_definition_collection_response import AccessReviewHistoryDefinitionCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class HistoryDefinitionsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/accessReviews/historyDefinitions"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewHistoryDefinitionCollectionResponse:
		"""
		List historyDefinitions
		Retrieve the accessReviewHistoryDefinition objects created in the last 30 days, including all nested properties.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewset-list-historydefinitions?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.accessReviewSet']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, AccessReviewHistoryDefinitionCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessReviewHistoryDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewHistoryDefinition:
		"""
		Create historyDefinitions
		Create a new accessReviewHistoryDefinition object.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewset-post-historydefinitions?view=graph-rest-1.0
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
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, AccessReviewHistoryDefinition, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_access_review_history_definition_id(self,
		accessReviewHistoryDefinition_id: str,
	) -> ByAccessReviewHistoryDefinitionIdRequest:
		if accessReviewHistoryDefinition_id is None:
			raise TypeError("accessReviewHistoryDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReviewHistoryDefinition%2Did"] =  accessReviewHistoryDefinition_id

		from .by_access_review_history_definition_id import ByAccessReviewHistoryDefinitionIdRequest
		return ByAccessReviewHistoryDefinitionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

