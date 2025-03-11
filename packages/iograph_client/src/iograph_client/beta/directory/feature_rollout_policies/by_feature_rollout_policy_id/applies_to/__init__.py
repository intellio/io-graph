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
	from .ref import RefRequest
	from .count import CountRequest
	from .by_directory_object_id import ByDirectoryObjectIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.directory_object import DirectoryObject
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.directory_object_collection_response import DirectoryObjectCollectionResponse


class AppliesToRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/featureRolloutPolicies/{featureRolloutPolicy%2Did}/appliesTo", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObjectCollectionResponse:
		"""
		Get appliesTo from directory
		Nullable. Specifies a list of directoryObject resources that feature is enabled for.
		"""
		tags = ['directory.featureRolloutPolicy']

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

	async def post(
		self,
		body: DirectoryObject,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectoryObject:
		"""
		Create new navigation property to appliesTo for directory
		
		"""
		tags = ['directory.featureRolloutPolicy']

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
		return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AppliesToRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AppliesToRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AppliesToRequest(self.request_adapter, self.path_parameters)

	@property
	def by_directory_object_id(self,
	) -> ByDirectoryObjectIdRequest:
		from .by_directory_object_id import ByDirectoryObjectIdRequest
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		featureRolloutPolicy_id: str,
	) -> CountRequest:
		if featureRolloutPolicy_id is None:
			raise TypeError("featureRolloutPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["featureRolloutPolicy%2Did"] =  featureRolloutPolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		featureRolloutPolicy_id: str,
	) -> RefRequest:
		if featureRolloutPolicy_id is None:
			raise TypeError("featureRolloutPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["featureRolloutPolicy%2Did"] =  featureRolloutPolicy_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

