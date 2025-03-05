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
	from .get_teams_licensing_details import GetTeamsLicensingDetailsRequest
	from .count import CountRequest
	from .by_license_details_id import ByLicenseDetailsIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.license_details_collection_response import LicenseDetailsCollectionResponse
from iograph_models.models.license_details import LicenseDetails


class LicenseDetailsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/licenseDetails", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LicenseDetailsCollectionResponse:
		"""
		List licenseDetails
		Retrieve a list of licenseDetails objects for enterprise users. This API returns details for licenses that are directly assigned and those transitively assigned through memberships in licensed groups.
		Find more info here: https://learn.microsoft.com/graph/api/user-list-licensedetails?view=graph-rest-1.0
		"""
		tags = ['me.licenseDetails']

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
		return await self.request_adapter.send_async(request_info, LicenseDetailsCollectionResponse, error_mapping)

	async def post(
		self,
		body: LicenseDetails,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LicenseDetails:
		"""
		Create new navigation property to licenseDetails for me
		
		"""
		tags = ['me.licenseDetails']

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
		return await self.request_adapter.send_async(request_info, LicenseDetails, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LicenseDetailsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LicenseDetailsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LicenseDetailsRequest(self.request_adapter, self.path_parameters)

	def by_license_details_id(self,
		licenseDetails_id: str,
	) -> ByLicenseDetailsIdRequest:
		if licenseDetails_id is None:
			raise TypeError("licenseDetails_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["licenseDetails%2Did"] =  licenseDetails_id

		from .by_license_details_id import ByLicenseDetailsIdRequest
		return ByLicenseDetailsIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def get_teams_licensing_details(self,
	) -> GetTeamsLicensingDetailsRequest:
		from .get_teams_licensing_details import GetTeamsLicensingDetailsRequest
		return GetTeamsLicensingDetailsRequest(self.request_adapter, self.path_parameters)

