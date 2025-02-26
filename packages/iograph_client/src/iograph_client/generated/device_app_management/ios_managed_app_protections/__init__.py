# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_ios_managed_app_protection_id import ByIosManagedAppProtectionIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.ios_managed_app_protection_collection_response import IosManagedAppProtectionCollectionResponse
from iograph_models.models.ios_managed_app_protection import IosManagedAppProtection


class IosManagedAppProtectionsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/iosManagedAppProtections"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IosManagedAppProtectionCollectionResponse:
		"""
		List iosManagedAppProtections
		List properties and relationships of the iosManagedAppProtection objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-iosmanagedappprotection-list?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.iosManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, IosManagedAppProtectionCollectionResponse, error_mapping)

	async def post(
		self,
		body: IosManagedAppProtection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IosManagedAppProtection:
		"""
		Create iosManagedAppProtection
		Create a new iosManagedAppProtection object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-iosmanagedappprotection-create?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.iosManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, IosManagedAppProtection, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_ios_managed_app_protection_id(self,
		iosManagedAppProtection_id: str,
	) -> ByIosManagedAppProtectionIdRequest:
		if iosManagedAppProtection_id is None:
			raise TypeError("iosManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosManagedAppProtection%2Did"] =  iosManagedAppProtection_id

		from .by_ios_managed_app_protection_id import ByIosManagedAppProtectionIdRequest
		return ByIosManagedAppProtectionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

