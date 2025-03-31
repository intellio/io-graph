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
	from .by_drive_protection_unit_id import ByDriveProtectionUnitIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.drive_protection_unit_collection_response import DriveProtectionUnitCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DriveProtectionUnitsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessProtectionPolicies/{oneDriveForBusinessProtectionPolicy%2Did}/driveProtectionUnits", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveProtectionUnitCollectionResponse:
		"""
		List driveProtectionUnits
		Get a list of the driveProtectionUnit objects that are associated with a oneDriveForBusinessProtectionPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-list-driveprotectionunits?view=graph-rest-beta
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, DriveProtectionUnitCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> DriveProtectionUnitsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DriveProtectionUnitsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DriveProtectionUnitsRequest(self.request_adapter, self.path_parameters)

	def by_drive_protection_unit_id(self,
		oneDriveForBusinessProtectionPolicy_id: str,
		driveProtectionUnit_id: str,
	) -> ByDriveProtectionUnitIdRequest:
		if oneDriveForBusinessProtectionPolicy_id is None:
			raise TypeError("oneDriveForBusinessProtectionPolicy_id cannot be null.")
		if driveProtectionUnit_id is None:
			raise TypeError("driveProtectionUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessProtectionPolicy%2Did"] =  oneDriveForBusinessProtectionPolicy_id
		path_parameters["driveProtectionUnit%2Did"] =  driveProtectionUnit_id

		from .by_drive_protection_unit_id import ByDriveProtectionUnitIdRequest
		return ByDriveProtectionUnitIdRequest(self.request_adapter, path_parameters)

	def count(self,
		oneDriveForBusinessProtectionPolicy_id: str,
	) -> CountRequest:
		if oneDriveForBusinessProtectionPolicy_id is None:
			raise TypeError("oneDriveForBusinessProtectionPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessProtectionPolicy%2Did"] =  oneDriveForBusinessProtectionPolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

