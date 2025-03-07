# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.filter_by_current_user_with_on_get_response import Filter_by_current_user_with_onGetResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class FilterByCurrentUserWithOnRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignmentApprovals/filterByCurrentUser(on='{on}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Filter_by_current_user_with_onGetResponse:
		"""
		Invoke function filterByCurrentUser
		In Microsoft Entra entitlement management, return a collection of access package assignment approvals. The objects returned are those that are in scope for approval by the calling user. In PIM for groups, return a collection of assignment approvals. The objects returned are those that are in scope for approval by the calling user.
		Find more info here: https://learn.microsoft.com/graph/api/approval-filterbycurrentuser?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, Filter_by_current_user_with_onGetResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> FilterByCurrentUserWithOnRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FilterByCurrentUserWithOnRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FilterByCurrentUserWithOnRequest(self.request_adapter, self.path_parameters)

