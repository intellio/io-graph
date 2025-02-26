# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_site_protection_unit_id import BySiteProtectionUnitIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.site_protection_unit_collection_response import SiteProtectionUnitCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SiteProtectionUnitsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/solutions/backupRestore/sharePointProtectionPolicies/{sharePointProtectionPolicy%2Did}/siteProtectionUnits"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SiteProtectionUnitCollectionResponse:
		"""
		List siteProtectionUnits
		Get a list of the siteProtectionUnit objects that are associated with a sharePointProtectionPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-list-siteprotectionunits?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SiteProtectionUnitCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def by_site_protection_unit_id(self,
		sharePointProtectionPolicy_id: str,
		siteProtectionUnit_id: str,
	) -> BySiteProtectionUnitIdRequest:
		if sharePointProtectionPolicy_id is None:
			raise TypeError("sharePointProtectionPolicy_id cannot be null.")
		if siteProtectionUnit_id is None:
			raise TypeError("siteProtectionUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharePointProtectionPolicy%2Did"] =  sharePointProtectionPolicy_id
		path_parameters["siteProtectionUnit%2Did"] =  siteProtectionUnit_id

		from .by_site_protection_unit_id import BySiteProtectionUnitIdRequest
		return BySiteProtectionUnitIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

