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
	from .by_ios_vpp_app_assigned_license_id import ByIosVppAppAssignedLicenseIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.ios_vpp_app_assigned_license import IosVppAppAssignedLicense
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.ios_vpp_app_assigned_license_collection_response import IosVppAppAssignedLicenseCollectionResponse


class AssignedLicensesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.iosVppApp/assignedLicenses", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IosVppAppAssignedLicenseCollectionResponse:
		"""
		Get assignedLicenses from deviceAppManagement
		The licenses assigned to this app.
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, IosVppAppAssignedLicenseCollectionResponse, error_mapping)

	async def post(
		self,
		body: IosVppAppAssignedLicense,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IosVppAppAssignedLicense:
		"""
		Create new navigation property to assignedLicenses for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, IosVppAppAssignedLicense, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignedLicensesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignedLicensesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignedLicensesRequest(self.request_adapter, self.path_parameters)

	def by_ios_vpp_app_assigned_license_id(self,
		mobileApp_id: str,
		iosVppAppAssignedLicense_id: str,
	) -> ByIosVppAppAssignedLicenseIdRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")
		if iosVppAppAssignedLicense_id is None:
			raise TypeError("iosVppAppAssignedLicense_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id
		path_parameters["iosVppAppAssignedLicense%2Did"] =  iosVppAppAssignedLicense_id

		from .by_ios_vpp_app_assigned_license_id import ByIosVppAppAssignedLicenseIdRequest
		return ByIosVppAppAssignedLicenseIdRequest(self.request_adapter, path_parameters)

	def count(self,
		mobileApp_id: str,
	) -> CountRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

