# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .security_update_index import SecurityUpdateIndexRequest
	from .security_remove_hold import SecurityRemoveHoldRequest
	from .security_release import SecurityReleaseRequest
	from .security_apply_hold import SecurityApplyHoldRequest
	from .last_index_operation import LastIndexOperationRequest
	from .data_source import DataSourceRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource


class ByEdiscoveryNoncustodialDataSourceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/noncustodialDataSources/{ediscoveryNoncustodialDataSource%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryNoncustodialDataSource:
		"""
		Get noncustodialDataSources from security
		Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryNoncustodialDataSource, error_mapping)

	async def patch(
		self,
		body: SecurityEdiscoveryNoncustodialDataSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoveryNoncustodialDataSource:
		"""
		Update the navigation property noncustodialDataSources in security
		
		"""
		tags = ['security.casesRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryNoncustodialDataSource, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property noncustodialDataSources for security
		
		"""
		tags = ['security.casesRoot']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByEdiscoveryNoncustodialDataSourceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEdiscoveryNoncustodialDataSourceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEdiscoveryNoncustodialDataSourceIdRequest(self.request_adapter, self.path_parameters)

	def data_source(self,
		ediscoveryCase_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> DataSourceRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .data_source import DataSourceRequest
		return DataSourceRequest(self.request_adapter, path_parameters)

	def last_index_operation(self,
		ediscoveryCase_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> LastIndexOperationRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .last_index_operation import LastIndexOperationRequest
		return LastIndexOperationRequest(self.request_adapter, path_parameters)

	def security_apply_hold(self,
		ediscoveryCase_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> SecurityApplyHoldRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .security_apply_hold import SecurityApplyHoldRequest
		return SecurityApplyHoldRequest(self.request_adapter, path_parameters)

	def security_release(self,
		ediscoveryCase_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> SecurityReleaseRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .security_release import SecurityReleaseRequest
		return SecurityReleaseRequest(self.request_adapter, path_parameters)

	def security_remove_hold(self,
		ediscoveryCase_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> SecurityRemoveHoldRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .security_remove_hold import SecurityRemoveHoldRequest
		return SecurityRemoveHoldRequest(self.request_adapter, path_parameters)

	def security_update_index(self,
		ediscoveryCase_id: str,
		ediscoveryNoncustodialDataSource_id: str,
	) -> SecurityUpdateIndexRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryNoncustodialDataSource_id is None:
			raise TypeError("ediscoveryNoncustodialDataSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryNoncustodialDataSource%2Did"] =  ediscoveryNoncustodialDataSource_id

		from .security_update_index import SecurityUpdateIndexRequest
		return SecurityUpdateIndexRequest(self.request_adapter, path_parameters)

