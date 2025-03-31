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
	from .security_remove_hold import SecurityRemoveHoldRequest
	from .security_apply_hold import SecurityApplyHoldRequest
	from .count import CountRequest
	from .by_ediscovery_custodian_id import ByEdiscoveryCustodianIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_ediscovery_custodian import SecurityEdiscoveryCustodian
from iograph_models.v1.security_ediscovery_custodian_collection_response import SecurityEdiscoveryCustodianCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class CustodiansRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/custodians", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryCustodianCollectionResponse:
		"""
		List ediscoveryCustodian
		Get a list of the custodian objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-list-custodians?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryCustodianCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityEdiscoveryCustodian,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoveryCustodian:
		"""
		Create custodians
		Create a new ediscoveryCustodian object.
After the custodian object is created, you will need to create the custodian's userSource to reference their mailbox and OneDrive for Business site.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-post-custodians?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryCustodian, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CustodiansRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CustodiansRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CustodiansRequest(self.request_adapter, self.path_parameters)

	def by_ediscovery_custodian_id(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> ByEdiscoveryCustodianIdRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .by_ediscovery_custodian_id import ByEdiscoveryCustodianIdRequest
		return ByEdiscoveryCustodianIdRequest(self.request_adapter, path_parameters)

	def count(self,
		ediscoveryCase_id: str,
	) -> CountRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def security_apply_hold(self,
		ediscoveryCase_id: str,
	) -> SecurityApplyHoldRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .security_apply_hold import SecurityApplyHoldRequest
		return SecurityApplyHoldRequest(self.request_adapter, path_parameters)

	def security_remove_hold(self,
		ediscoveryCase_id: str,
	) -> SecurityRemoveHoldRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id

		from .security_remove_hold import SecurityRemoveHoldRequest
		return SecurityRemoveHoldRequest(self.request_adapter, path_parameters)

