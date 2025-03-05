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
	from .by_user_source_id import ByUserSourceIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.security_user_source import SecurityUserSource
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_user_source_collection_response import SecurityUserSourceCollectionResponse


class UserSourcesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/custodians/{ediscoveryCustodian%2Did}/userSources", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityUserSourceCollectionResponse:
		"""
		List userSources
		Get a list of the userSource objects associated with an ediscoveryCustodian or ediscoveryHoldPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycustodian-list-usersources?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityUserSourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityUserSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityUserSource:
		"""
		Create custodian userSource
		Create a new userSource object associated with an eDiscovery custodian.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycustodian-post-usersources?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityUserSource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserSourcesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserSourcesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserSourcesRequest(self.request_adapter, self.path_parameters)

	def by_user_source_id(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
		userSource_id: str,
	) -> ByUserSourceIdRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")
		if userSource_id is None:
			raise TypeError("userSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id
		path_parameters["userSource%2Did"] =  userSource_id

		from .by_user_source_id import ByUserSourceIdRequest
		return ByUserSourceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		ediscoveryCase_id: str,
		ediscoveryCustodian_id: str,
	) -> CountRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryCustodian_id is None:
			raise TypeError("ediscoveryCustodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryCustodian%2Did"] =  ediscoveryCustodian_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

