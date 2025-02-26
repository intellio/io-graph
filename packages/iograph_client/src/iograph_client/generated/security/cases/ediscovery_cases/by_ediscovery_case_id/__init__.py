# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tags import TagsRequest
	from .settings import SettingsRequest
	from .searches import SearchesRequest
	from .review_sets import ReviewSetsRequest
	from .operations import OperationsRequest
	from .noncustodial_data_sources import NoncustodialDataSourcesRequest
	from .security_reopen import SecurityReopenRequest
	from .security_close import SecurityCloseRequest
	from .custodians import CustodiansRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_ediscovery_case import SecurityEdiscoveryCase


class ByEdiscoveryCaseIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryCase:
		"""
		Get ediscoveryCase
		Read the properties and relationships of an ediscoveryCase object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryCase, error_mapping)

	async def patch(
		self,
		body: SecurityEdiscoveryCase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoveryCase:
		"""
		Update ediscoveryCase
		Update the properties of an ediscoveryCase object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryCase, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete ediscoveryCase
		Delete an ediscoveryCase object.
		Find more info here: https://learn.microsoft.com/graph/api/security-casesroot-delete-ediscoverycases?view=graph-rest-1.0
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



	@property
	def custodians(self,
	) -> CustodiansRequest:
		from .custodians import CustodiansRequest
		return CustodiansRequest(self.request_adapter, self.path_parameters)

	@property
	def security_close(self,
	) -> SecurityCloseRequest:
		from .security_close import SecurityCloseRequest
		return SecurityCloseRequest(self.request_adapter, self.path_parameters)

	@property
	def security_reopen(self,
	) -> SecurityReopenRequest:
		from .security_reopen import SecurityReopenRequest
		return SecurityReopenRequest(self.request_adapter, self.path_parameters)

	@property
	def noncustodial_data_sources(self,
	) -> NoncustodialDataSourcesRequest:
		from .noncustodial_data_sources import NoncustodialDataSourcesRequest
		return NoncustodialDataSourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def review_sets(self,
	) -> ReviewSetsRequest:
		from .review_sets import ReviewSetsRequest
		return ReviewSetsRequest(self.request_adapter, self.path_parameters)

	@property
	def searches(self,
	) -> SearchesRequest:
		from .searches import SearchesRequest
		return SearchesRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self,
	) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def tags(self,
	) -> TagsRequest:
		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, self.path_parameters)

