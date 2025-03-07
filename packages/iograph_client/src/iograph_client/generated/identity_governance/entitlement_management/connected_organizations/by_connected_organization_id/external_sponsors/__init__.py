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
	from .ref import RefRequest
	from .count import CountRequest
	from .by_directory_object_id import ByDirectoryObjectIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.directory_object_collection_response import DirectoryObjectCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ExternalSponsorsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/connectedOrganizations/{connectedOrganization%2Did}/externalSponsors", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObjectCollectionResponse:
		"""
		Get externalSponsors from identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, DirectoryObjectCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ExternalSponsorsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ExternalSponsorsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ExternalSponsorsRequest(self.request_adapter, self.path_parameters)

	@property
	def by_directory_object_id(self,
	) -> ByDirectoryObjectIdRequest:
		from .by_directory_object_id import ByDirectoryObjectIdRequest
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		connectedOrganization_id: str,
	) -> CountRequest:
		if connectedOrganization_id is None:
			raise TypeError("connectedOrganization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["connectedOrganization%2Did"] =  connectedOrganization_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		connectedOrganization_id: str,
	) -> RefRequest:
		if connectedOrganization_id is None:
			raise TypeError("connectedOrganization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["connectedOrganization%2Did"] =  connectedOrganization_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

