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
	from .tags import TagsRequest
	from .settings import SettingsRequest
	from .searches import SearchesRequest
	from .review_sets import ReviewSetsRequest
	from .operations import OperationsRequest
	from .noncustodial_data_sources import NoncustodialDataSourcesRequest
	from .security_reopen import SecurityReopenRequest
	from .security_close import SecurityCloseRequest
	from .legal_holds import LegalHoldsRequest
	from .custodians import CustodiansRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_ediscovery_case import SecurityEdiscoveryCase


class ByEdiscoveryCaseIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryCase:
		"""
		Get ediscoveryCase
		Read the properties and relationships of an ediscoveryCase object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-get?view=graph-rest-beta
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
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-update?view=graph-rest-beta
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
		Find more info here: https://learn.microsoft.com/graph/api/security-casesroot-delete-ediscoverycases?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByEdiscoveryCaseIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEdiscoveryCaseIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEdiscoveryCaseIdRequest(self.request_adapter, self.path_parameters)

	def custodians(self,
		ediscoveryCase_id: str,
	) -> CustodiansRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .custodians import CustodiansRequest
		return CustodiansRequest(self.request_adapter, path_parameters)

	def legal_holds(self,
		ediscoveryCase_id: str,
	) -> LegalHoldsRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .legal_holds import LegalHoldsRequest
		return LegalHoldsRequest(self.request_adapter, path_parameters)

	def security_close(self,
		ediscoveryCase_id: str,
	) -> SecurityCloseRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .security_close import SecurityCloseRequest
		return SecurityCloseRequest(self.request_adapter, path_parameters)

	def security_reopen(self,
		ediscoveryCase_id: str,
	) -> SecurityReopenRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .security_reopen import SecurityReopenRequest
		return SecurityReopenRequest(self.request_adapter, path_parameters)

	def noncustodial_data_sources(self,
		ediscoveryCase_id: str,
	) -> NoncustodialDataSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .noncustodial_data_sources import NoncustodialDataSourcesRequest
		return NoncustodialDataSourcesRequest(self.request_adapter, path_parameters)

	def operations(self,
		ediscoveryCase_id: str,
	) -> OperationsRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def review_sets(self,
		ediscoveryCase_id: str,
	) -> ReviewSetsRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .review_sets import ReviewSetsRequest
		return ReviewSetsRequest(self.request_adapter, path_parameters)

	def searches(self,
		ediscoveryCase_id: str,
	) -> SearchesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .searches import SearchesRequest
		return SearchesRequest(self.request_adapter, path_parameters)

	def settings(self,
		ediscoveryCase_id: str,
	) -> SettingsRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

	def tags(self,
		ediscoveryCase_id: str,
	) -> TagsRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, path_parameters)

