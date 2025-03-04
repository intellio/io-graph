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
	from .user_sources import UserSourcesRequest
	from .unified_group_sources import UnifiedGroupSourcesRequest
	from .site_sources import SiteSourcesRequest
	from .security_update_index import SecurityUpdateIndexRequest
	from .security_remove_hold import SecurityRemoveHoldRequest
	from .security_release import SecurityReleaseRequest
	from .security_apply_hold import SecurityApplyHoldRequest
	from .security_activate import SecurityActivateRequest
	from .last_index_operation import LastIndexOperationRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_ediscovery_custodian import SecurityEdiscoveryCustodian


class ByEdiscoveryCustodianIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/custodians/{ediscoveryCustodian%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryCustodian:
		"""
		Get ediscoveryCustodian
		Read the properties and relationships of an ediscoveryCustodian object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycustodian-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryCustodian, error_mapping)

	async def patch(
		self,
		body: SecurityEdiscoveryCustodian,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoveryCustodian:
		"""
		Update the navigation property custodians in security
		
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryCustodian, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property custodians for security
		
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



	def with_url(self, raw_url: str) -> ByEdiscoveryCustodianIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEdiscoveryCustodianIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEdiscoveryCustodianIdRequest(self.request_adapter, self.path_parameters)

	def last_index_operation(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> LastIndexOperationRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .last_index_operation import LastIndexOperationRequest
		return LastIndexOperationRequest(self.request_adapter, path_parameters)

	def security_activate(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> SecurityActivateRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .security_activate import SecurityActivateRequest
		return SecurityActivateRequest(self.request_adapter, path_parameters)

	def security_apply_hold(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> SecurityApplyHoldRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .security_apply_hold import SecurityApplyHoldRequest
		return SecurityApplyHoldRequest(self.request_adapter, path_parameters)

	def security_release(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> SecurityReleaseRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .security_release import SecurityReleaseRequest
		return SecurityReleaseRequest(self.request_adapter, path_parameters)

	def security_remove_hold(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> SecurityRemoveHoldRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .security_remove_hold import SecurityRemoveHoldRequest
		return SecurityRemoveHoldRequest(self.request_adapter, path_parameters)

	def security_update_index(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> SecurityUpdateIndexRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .security_update_index import SecurityUpdateIndexRequest
		return SecurityUpdateIndexRequest(self.request_adapter, path_parameters)

	def site_sources(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> SiteSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .site_sources import SiteSourcesRequest
		return SiteSourcesRequest(self.request_adapter, path_parameters)

	def unified_group_sources(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> UnifiedGroupSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .unified_group_sources import UnifiedGroupSourcesRequest
		return UnifiedGroupSourcesRequest(self.request_adapter, path_parameters)

	def user_sources(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> UserSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .user_sources import UserSourcesRequest
		return UserSourcesRequest(self.request_adapter, path_parameters)

