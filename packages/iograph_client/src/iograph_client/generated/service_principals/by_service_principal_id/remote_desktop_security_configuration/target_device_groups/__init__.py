# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_target_device_group_id import ByTargetDeviceGroupIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.target_device_group_collection_response import TargetDeviceGroupCollectionResponse
from iograph_models.models.target_device_group import TargetDeviceGroup
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class TargetDeviceGroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/remoteDesktopSecurityConfiguration/targetDeviceGroups", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TargetDeviceGroupCollectionResponse:
		"""
		List targetDeviceGroups
		Get a list of the targetDeviceGroup objects and their properties on the remoteDesktopSecurityConfiguration resource on the servicePrincipal. Any user authenticating using the Microsoft Entra ID Remote Desktop Services (RDS) authentication protocol to a Microsoft Entra joined or Microsoft Entra hybrid joined device that belongs to the targetDeviceGroup will get SSO.
		Find more info here: https://learn.microsoft.com/graph/api/remotedesktopsecurityconfiguration-list-targetdevicegroups?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.remoteDesktopSecurityConfiguration']

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
		return await self.request_adapter.send_async(request_info, TargetDeviceGroupCollectionResponse, error_mapping)

	async def post(
		self,
		body: TargetDeviceGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TargetDeviceGroup:
		"""
		Create targetDeviceGroup
		Create a new targetDeviceGroup object for the remoteDesktopSecurityConfiguration object on the servicePrincipal. You can configure a maximum of 10 target device groups for the remoteDesktopSecurityConfiguraiton object on the servicePrincipal.
		Find more info here: https://learn.microsoft.com/graph/api/remotedesktopsecurityconfiguration-post-targetdevicegroups?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.remoteDesktopSecurityConfiguration']

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
		return await self.request_adapter.send_async(request_info, TargetDeviceGroup, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TargetDeviceGroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TargetDeviceGroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TargetDeviceGroupsRequest(self.request_adapter, self.path_parameters)

	def by_target_device_group_id(self,
		servicePrincipal_id: str,
		targetDeviceGroup_id: str,
	) -> ByTargetDeviceGroupIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if targetDeviceGroup_id is None:
			raise TypeError("targetDeviceGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["targetDeviceGroup%2Did"] =  targetDeviceGroup_id

		from .by_target_device_group_id import ByTargetDeviceGroupIdRequest
		return ByTargetDeviceGroupIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

