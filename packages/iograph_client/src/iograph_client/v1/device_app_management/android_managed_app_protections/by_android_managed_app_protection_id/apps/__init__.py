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
	from .by_managed_mobile_app_id import ByManagedMobileAppIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.managed_mobile_app_collection_response import ManagedMobileAppCollectionResponse
from iograph_models.v1.managed_mobile_app import ManagedMobileApp


class AppsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/androidManagedAppProtections/{androidManagedAppProtection%2Did}/apps", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedMobileAppCollectionResponse:
		"""
		Get apps from deviceAppManagement
		List of apps to which the policy is deployed.
		"""
		tags = ['deviceAppManagement.androidManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, ManagedMobileAppCollectionResponse, error_mapping)

	async def post(
		self,
		body: ManagedMobileApp,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedMobileApp:
		"""
		Create new navigation property to apps for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.androidManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, ManagedMobileApp, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AppsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AppsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AppsRequest(self.request_adapter, self.path_parameters)

	def by_managed_mobile_app_id(self,
		androidManagedAppProtection_id: str,
		managedMobileApp_id: str,
	) -> ByManagedMobileAppIdRequest:
		if androidManagedAppProtection_id is None:
			raise TypeError("androidManagedAppProtection_id cannot be null.")
		if managedMobileApp_id is None:
			raise TypeError("managedMobileApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["androidManagedAppProtection%2Did"] =  androidManagedAppProtection_id
		path_parameters["managedMobileApp%2Did"] =  managedMobileApp_id

		from .by_managed_mobile_app_id import ByManagedMobileAppIdRequest
		return ByManagedMobileAppIdRequest(self.request_adapter, path_parameters)

	def count(self,
		androidManagedAppProtection_id: str,
	) -> CountRequest:
		if androidManagedAppProtection_id is None:
			raise TypeError("androidManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["androidManagedAppProtection%2Did"] =  androidManagedAppProtection_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

