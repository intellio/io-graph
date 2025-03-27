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
	from .import_apple_device_identity_list import ImportAppleDeviceIdentityListRequest
	from .count import CountRequest
	from .by_imported_apple_device_identity_id import ByImportedAppleDeviceIdentityIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.imported_apple_device_identity_collection_response import ImportedAppleDeviceIdentityCollectionResponse
from iograph_models.beta.imported_apple_device_identity import ImportedAppleDeviceIdentity
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ImportedAppleDeviceIdentitiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}/importedAppleDeviceIdentities", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ImportedAppleDeviceIdentityCollectionResponse:
		"""
		Get importedAppleDeviceIdentities from deviceManagement
		The imported Apple device identities.
		"""
		tags = ['deviceManagement.depOnboardingSetting']

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
		return await self.request_adapter.send_async(request_info, ImportedAppleDeviceIdentityCollectionResponse, error_mapping)

	async def post(
		self,
		body: ImportedAppleDeviceIdentity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ImportedAppleDeviceIdentity:
		"""
		Create new navigation property to importedAppleDeviceIdentities for deviceManagement
		
		"""
		tags = ['deviceManagement.depOnboardingSetting']

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
		return await self.request_adapter.send_async(request_info, ImportedAppleDeviceIdentity, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ImportedAppleDeviceIdentitiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ImportedAppleDeviceIdentitiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ImportedAppleDeviceIdentitiesRequest(self.request_adapter, self.path_parameters)

	def by_imported_apple_device_identity_id(self,
		depOnboardingSetting_id: str,
		importedAppleDeviceIdentity_id: str,
	) -> ByImportedAppleDeviceIdentityIdRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")
		if importedAppleDeviceIdentity_id is None:
			raise TypeError("importedAppleDeviceIdentity_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id
		path_parameters["importedAppleDeviceIdentity%2Did"] =  importedAppleDeviceIdentity_id

		from .by_imported_apple_device_identity_id import ByImportedAppleDeviceIdentityIdRequest
		return ByImportedAppleDeviceIdentityIdRequest(self.request_adapter, path_parameters)

	def count(self,
		depOnboardingSetting_id: str,
	) -> CountRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def import_apple_device_identity_list(self,
		depOnboardingSetting_id: str,
	) -> ImportAppleDeviceIdentityListRequest:
		if depOnboardingSetting_id is None:
			raise TypeError("depOnboardingSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["depOnboardingSetting%2Did"] =  depOnboardingSetting_id

		from .import_apple_device_identity_list import ImportAppleDeviceIdentityListRequest
		return ImportAppleDeviceIdentityListRequest(self.request_adapter, path_parameters)

