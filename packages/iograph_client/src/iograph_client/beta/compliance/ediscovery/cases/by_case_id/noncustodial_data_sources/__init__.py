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
	from .ediscovery_remove_hold import EdiscoveryRemoveHoldRequest
	from .ediscovery_apply_hold import EdiscoveryApplyHoldRequest
	from .count import CountRequest
	from .by_noncustodial_data_source_id import ByNoncustodialDataSourceIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
from iograph_models.beta.ediscovery_noncustodial_data_source_collection_response import EdiscoveryNoncustodialDataSourceCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class NoncustodialDataSourcesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/noncustodialDataSources", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryNoncustodialDataSourceCollectionResponse:
		"""
		List noncustodialDataSources
		Get a list of the noncustodialDataSource objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-noncustodialdatasource-list?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryNoncustodialDataSourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: EdiscoveryNoncustodialDataSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryNoncustodialDataSource:
		"""
		Create noncustodialDataSource
		Create a new noncustodialDataSource object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-noncustodialdatasource-post?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryNoncustodialDataSource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> NoncustodialDataSourcesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NoncustodialDataSourcesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NoncustodialDataSourcesRequest(self.request_adapter, self.path_parameters)

	def by_noncustodial_data_source_id(self,
		case_id: str,
		noncustodialDataSource_id: str,
	) -> ByNoncustodialDataSourceIdRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if noncustodialDataSource_id is None:
			raise TypeError("noncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["noncustodialDataSource%2Did"] =  noncustodialDataSource_id

		from .by_noncustodial_data_source_id import ByNoncustodialDataSourceIdRequest
		return ByNoncustodialDataSourceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		case_id: str,
	) -> CountRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ediscovery_apply_hold(self,
		case_id: str,
	) -> EdiscoveryApplyHoldRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .ediscovery_apply_hold import EdiscoveryApplyHoldRequest
		return EdiscoveryApplyHoldRequest(self.request_adapter, path_parameters)

	def ediscovery_remove_hold(self,
		case_id: str,
	) -> EdiscoveryRemoveHoldRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .ediscovery_remove_hold import EdiscoveryRemoveHoldRequest
		return EdiscoveryRemoveHoldRequest(self.request_adapter, path_parameters)

