# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_privilege_management_elevation_request_id import ByPrivilegeManagementElevationRequestIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.privilege_management_elevation_request_collection_response import PrivilegeManagementElevationRequestCollectionResponse
from iograph_models.beta.privilege_management_elevation_request import PrivilegeManagementElevationRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ElevationRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/elevationRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegeManagementElevationRequestCollectionResponse:
		"""
		Get elevationRequests from deviceManagement
		List of elevation requests
		"""
		tags = ['deviceManagement.privilegeManagementElevationRequest']

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
		return await self.request_adapter.send_async(request_info, PrivilegeManagementElevationRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrivilegeManagementElevationRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegeManagementElevationRequest:
		"""
		Create new navigation property to elevationRequests for deviceManagement
		
		"""
		tags = ['deviceManagement.privilegeManagementElevationRequest']

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
		return await self.request_adapter.send_async(request_info, PrivilegeManagementElevationRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ElevationRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ElevationRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ElevationRequestsRequest(self.request_adapter, self.path_parameters)

	def by_privilege_management_elevation_request_id(self,
		privilegeManagementElevationRequest_id: str,
	) -> ByPrivilegeManagementElevationRequestIdRequest:
		if privilegeManagementElevationRequest_id is None:
			raise TypeError("privilegeManagementElevationRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegeManagementElevationRequest%2Did"] =  privilegeManagementElevationRequest_id

		from .by_privilege_management_elevation_request_id import ByPrivilegeManagementElevationRequestIdRequest
		return ByPrivilegeManagementElevationRequestIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

