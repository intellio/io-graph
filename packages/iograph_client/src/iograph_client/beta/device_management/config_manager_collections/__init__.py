# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_policy_summary_with_policyid import GetPolicySummaryWithPolicyIdRequest
	from .count import CountRequest
	from .by_config_manager_collection_id import ByConfigManagerCollectionIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.config_manager_collection import ConfigManagerCollection
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.config_manager_collection_collection_response import ConfigManagerCollectionCollectionResponse


class ConfigManagerCollectionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/configManagerCollections", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ConfigManagerCollectionCollectionResponse:
		"""
		Get configManagerCollections from deviceManagement
		A list of ConfigManagerCollection
		"""
		tags = ['deviceManagement.configManagerCollection']

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
		return await self.request_adapter.send_async(request_info, ConfigManagerCollectionCollectionResponse, error_mapping)

	async def post(
		self,
		body: ConfigManagerCollection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ConfigManagerCollection:
		"""
		Create new navigation property to configManagerCollections for deviceManagement
		
		"""
		tags = ['deviceManagement.configManagerCollection']

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
		return await self.request_adapter.send_async(request_info, ConfigManagerCollection, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ConfigManagerCollectionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ConfigManagerCollectionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ConfigManagerCollectionsRequest(self.request_adapter, self.path_parameters)

	def by_config_manager_collection_id(self,
		configManagerCollection_id: str,
	) -> ByConfigManagerCollectionIdRequest:
		if configManagerCollection_id is None:
			raise TypeError("configManagerCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["configManagerCollection%2Did"] =  configManagerCollection_id

		from .by_config_manager_collection_id import ByConfigManagerCollectionIdRequest
		return ByConfigManagerCollectionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def get_policy_summary_with_policyid(self,
		policyId: str,
	) -> GetPolicySummaryWithPolicyIdRequest:
		if policyId is None:
			raise TypeError("policyId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["policyId"] =  policyId

		from .get_policy_summary_with_policyid import GetPolicySummaryWithPolicyIdRequest
		return GetPolicySummaryWithPolicyIdRequest(self.request_adapter, path_parameters)

