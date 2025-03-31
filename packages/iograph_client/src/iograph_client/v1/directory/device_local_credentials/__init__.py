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
	from .by_device_local_credential_info_id import ByDeviceLocalCredentialInfoIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.device_local_credential_info_collection_response import DeviceLocalCredentialInfoCollectionResponse
from iograph_models.v1.device_local_credential_info import DeviceLocalCredentialInfo
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceLocalCredentialsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/deviceLocalCredentials", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceLocalCredentialInfoCollectionResponse:
		"""
		List deviceLocalCredentialInfo
		Get a list of the deviceLocalCredentialInfo objects and their properties, excluding the credentials property. 
		Find more info here: https://learn.microsoft.com/graph/api/directory-list-devicelocalcredentials?view=graph-rest-1.0
		"""
		tags = ['directory.deviceLocalCredentialInfo']

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
		return await self.request_adapter.send_async(request_info, DeviceLocalCredentialInfoCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceLocalCredentialInfo,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceLocalCredentialInfo:
		"""
		Create new navigation property to deviceLocalCredentials for directory
		
		"""
		tags = ['directory.deviceLocalCredentialInfo']

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
		return await self.request_adapter.send_async(request_info, DeviceLocalCredentialInfo, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceLocalCredentialsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceLocalCredentialsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceLocalCredentialsRequest(self.request_adapter, self.path_parameters)

	def by_device_local_credential_info_id(self,
		deviceLocalCredentialInfo_id: str,
	) -> ByDeviceLocalCredentialInfoIdRequest:
		if deviceLocalCredentialInfo_id is None:
			raise TypeError("deviceLocalCredentialInfo_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceLocalCredentialInfo%2Did"] =  deviceLocalCredentialInfo_id

		from .by_device_local_credential_info_id import ByDeviceLocalCredentialInfoIdRequest
		return ByDeviceLocalCredentialInfoIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

