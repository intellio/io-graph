# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_ediscovery_noncustodial_data_source_id import ByEdiscoveryNoncustodialDataSourceIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.security_ediscovery_noncustodial_data_source_collection_response import SecurityEdiscoveryNoncustodialDataSourceCollectionResponse


class NoncustodialSourcesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/searches/{ediscoverySearch%2Did}/noncustodialSources", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryNoncustodialDataSourceCollectionResponse:
		"""
		Get noncustodialSources from security
		noncustodialDataSource sources that are included in the eDiscovery search
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryNoncustodialDataSourceCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> NoncustodialSourcesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NoncustodialSourcesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NoncustodialSourcesRequest(self.request_adapter, self.path_parameters)

	def by_ediscovery_noncustodial_data_source_id(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> ByEdiscoveryNoncustodialDataSourceIdRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .by_ediscovery_noncustodial_data_source_id import ByEdiscoveryNoncustodialDataSourceIdRequest
		return ByEdiscoveryNoncustodialDataSourceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> CountRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

