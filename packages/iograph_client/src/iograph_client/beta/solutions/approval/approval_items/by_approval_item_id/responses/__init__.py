# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_approval_item_response_id import ByApprovalItemResponseIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.approval_item_response_collection_response import ApprovalItemResponseCollectionResponse
from iograph_models.beta.approval_item_response import ApprovalItemResponse


class ResponsesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/approval/approvalItems/{approvalItem%2Did}/responses", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ApprovalItemResponseCollectionResponse:
		"""
		List responses
		Get a list of approvalItemResponse objects.
		Find more info here: https://learn.microsoft.com/graph/api/approvalitem-list-responses?view=graph-rest-beta
		"""
		tags = ['solutions.approvalSolution']

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
		return await self.request_adapter.send_async(request_info, ApprovalItemResponseCollectionResponse, error_mapping)

	async def post(
		self,
		body: ApprovalItemResponse,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ApprovalItemResponse:
		"""
		Create approvalItemResponse
		Create a new approvalItemResponse object.
		Find more info here: https://learn.microsoft.com/graph/api/approvalitem-post-responses?view=graph-rest-beta
		"""
		tags = ['solutions.approvalSolution']

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
		return await self.request_adapter.send_async(request_info, ApprovalItemResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ResponsesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ResponsesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ResponsesRequest(self.request_adapter, self.path_parameters)

	def by_approval_item_response_id(self,
		approvalItem_id: str,
		approvalItemResponse_id: str,
	) -> ByApprovalItemResponseIdRequest:
		if approvalItem_id is None:
			raise TypeError("approvalItem_id cannot be null.")
		if approvalItemResponse_id is None:
			raise TypeError("approvalItemResponse_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["approvalItem%2Did"] =  approvalItem_id
		path_parameters["approvalItemResponse%2Did"] =  approvalItemResponse_id

		from .by_approval_item_response_id import ByApprovalItemResponseIdRequest
		return ByApprovalItemResponseIdRequest(self.request_adapter, path_parameters)

	def count(self,
		approvalItem_id: str,
	) -> CountRequest:
		if approvalItem_id is None:
			raise TypeError("approvalItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["approvalItem%2Did"] =  approvalItem_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

