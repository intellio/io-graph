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
	from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
	from .count import CountRequest
	from .by_user_consent_request_id import ByUserConsentRequestIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.user_consent_request_collection_response import UserConsentRequestCollectionResponse
from iograph_models.v1.user_consent_request import UserConsentRequest


class UserConsentRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/appConsent/appConsentRequests/{appConsentRequest%2Did}/userConsentRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserConsentRequestCollectionResponse:
		"""
		List userConsentRequests
		Retrieve a collection of userConsentRequest objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/appconsentrequest-list-userconsentrequests?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.appConsentApprovalRoute']

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
		return await self.request_adapter.send_async(request_info, UserConsentRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserConsentRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserConsentRequest:
		"""
		Create new navigation property to userConsentRequests for identityGovernance
		
		"""
		tags = ['identityGovernance.appConsentApprovalRoute']

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
		return await self.request_adapter.send_async(request_info, UserConsentRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserConsentRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserConsentRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserConsentRequestsRequest(self.request_adapter, self.path_parameters)

	def by_user_consent_request_id(self,
		appConsentRequest_id: str,
		userConsentRequest_id: str,
	) -> ByUserConsentRequestIdRequest:
		if appConsentRequest_id is None:
			raise TypeError("appConsentRequest_id cannot be null.")
		if userConsentRequest_id is None:
			raise TypeError("userConsentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appConsentRequest%2Did"] =  appConsentRequest_id
		path_parameters["userConsentRequest%2Did"] =  userConsentRequest_id

		from .by_user_consent_request_id import ByUserConsentRequestIdRequest
		return ByUserConsentRequestIdRequest(self.request_adapter, path_parameters)

	def count(self,
		appConsentRequest_id: str,
	) -> CountRequest:
		if appConsentRequest_id is None:
			raise TypeError("appConsentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appConsentRequest%2Did"] =  appConsentRequest_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def filter_by_current_user_with_on(self,
		appConsentRequest_id: str,
		on: str,
	) -> FilterByCurrentUserWithOnRequest:
		if appConsentRequest_id is None:
			raise TypeError("appConsentRequest_id cannot be null.")
		if on is None:
			raise TypeError("on cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appConsentRequest%2Did"] =  appConsentRequest_id
		path_parameters["on"] =  on

		from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
		return FilterByCurrentUserWithOnRequest(self.request_adapter, path_parameters)

