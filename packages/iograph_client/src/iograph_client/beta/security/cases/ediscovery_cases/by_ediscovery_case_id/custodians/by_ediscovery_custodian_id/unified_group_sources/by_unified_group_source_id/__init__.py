# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .group import GroupRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_unified_group_source import SecurityUnifiedGroupSource
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUnifiedGroupSourceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/custodians/{ediscoveryCustodian%2Did}/unifiedGroupSources/{unifiedGroupSource%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityUnifiedGroupSource:
		"""
		Get unifiedGroupSources from security
		Data source entity for groups associated with the custodian.
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
		return await self.request_adapter.send_async(request_info, SecurityUnifiedGroupSource, error_mapping)

	async def patch(
		self,
		body: SecurityUnifiedGroupSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityUnifiedGroupSource:
		"""
		Update the navigation property unifiedGroupSources in security
		
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
		return await self.request_adapter.send_async(request_info, SecurityUnifiedGroupSource, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete unifiedGroupSource
		Delete a unifiedGroupSource object associated with an ediscoveryCustodian.
		Find more info here: https://learn.microsoft.com/graph/api/security-unifiedgroupsource-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByUnifiedGroupSourceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedGroupSourceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedGroupSourceIdRequest(self.request_adapter, self.path_parameters)

	def group(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
		unifiedGroupSource_id: str,
	) -> GroupRequest:
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

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

