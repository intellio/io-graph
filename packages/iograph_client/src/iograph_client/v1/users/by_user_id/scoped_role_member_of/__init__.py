# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_scoped_role_membership_id import ByScopedRoleMembershipIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.scoped_role_membership import ScopedRoleMembership
from iograph_models.v1.scoped_role_membership_collection_response import ScopedRoleMembershipCollectionResponse


class ScopedRoleMemberOfRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/scopedRoleMemberOf", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ScopedRoleMembershipCollectionResponse:
		"""
		Get scopedRoleMemberOf from users
		
		"""
		tags = ['users.scopedRoleMembership']

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
		return await self.request_adapter.send_async(request_info, ScopedRoleMembershipCollectionResponse, error_mapping)

	async def post(
		self,
		body: ScopedRoleMembership,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ScopedRoleMembership:
		"""
		Create new navigation property to scopedRoleMemberOf for users
		
		"""
		tags = ['users.scopedRoleMembership']

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
		return await self.request_adapter.send_async(request_info, ScopedRoleMembership, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ScopedRoleMemberOfRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ScopedRoleMemberOfRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ScopedRoleMemberOfRequest(self.request_adapter, self.path_parameters)

	def by_scoped_role_membership_id(self,
		user_id: str,
		scopedRoleMembership_id: str,
	) -> ByScopedRoleMembershipIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if scopedRoleMembership_id is None:
			raise TypeError("scopedRoleMembership_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["scopedRoleMembership%2Did"] =  scopedRoleMembership_id

		from .by_scoped_role_membership_id import ByScopedRoleMembershipIdRequest
		return ByScopedRoleMembershipIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

