# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_unified_group_source_id import ByUnifiedGroupSourceIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.security_unified_group_source_collection_response import SecurityUnifiedGroupSourceCollectionResponse
from iograph_models.models.security_unified_group_source import SecurityUnifiedGroupSource
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class UnifiedGroupSourcesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/custodians/{ediscoveryCustodian%2Did}/unifiedGroupSources"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityUnifiedGroupSourceCollectionResponse:
		"""
		List unifiedGroupSources
		Get a list of the unifiedGroupSource objects associated with an ediscoveryCustodian.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycustodian-list-unifiedgroupsources?view=graph-rest-1.0
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityUnifiedGroupSourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityUnifiedGroupSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityUnifiedGroupSource:
		"""
		Create custodian unifiedGroupSource
		Create a new unifiedGroupSource object associated with an eDiscovery custodian.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycustodian-post-unifiedgroupsources?view=graph-rest-1.0
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityUnifiedGroupSource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_unified_group_source_id(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
		unifiedGroupSource_id: str,
	) -> ByUnifiedGroupSourceIdRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")
		if unifiedGroupSource_id is None:
			raise TypeError("unifiedGroupSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id
		path_parameters["unifiedGroupSource%2Did"] =  unifiedGroupSource_id

		from .by_unified_group_source_id import ByUnifiedGroupSourceIdRequest
		return ByUnifiedGroupSourceIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

