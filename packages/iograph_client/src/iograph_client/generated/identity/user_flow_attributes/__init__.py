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
	from .count import CountRequest
	from .by_identity_user_flow_attribute_id import ByIdentityUserFlowAttributeIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.identity_user_flow_attribute import IdentityUserFlowAttribute
from iograph_models.models.identity_user_flow_attribute_collection_response import IdentityUserFlowAttributeCollectionResponse


class UserFlowAttributesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/userFlowAttributes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityUserFlowAttributeCollectionResponse:
		"""
		List identityUserFlowAttributes
		Retrieve a list of identityUserFlowAttribute objects.
		Find more info here: https://learn.microsoft.com/graph/api/identityuserflowattribute-list?view=graph-rest-1.0
		"""
		tags = ['identity.identityUserFlowAttribute']

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
		return await self.request_adapter.send_async(request_info, IdentityUserFlowAttributeCollectionResponse, error_mapping)

	async def post(
		self,
		body: IdentityUserFlowAttribute,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityUserFlowAttribute:
		"""
		Create identityUserFlowAttribute
		Create a new custom identityUserFlowAttribute object.
		Find more info here: https://learn.microsoft.com/graph/api/identityuserflowattribute-post?view=graph-rest-1.0
		"""
		tags = ['identity.identityUserFlowAttribute']

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
		return await self.request_adapter.send_async(request_info, IdentityUserFlowAttribute, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserFlowAttributesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserFlowAttributesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserFlowAttributesRequest(self.request_adapter, self.path_parameters)

	def by_identity_user_flow_attribute_id(self,
		identityUserFlowAttribute_id: str,
	) -> ByIdentityUserFlowAttributeIdRequest:
		if identityUserFlowAttribute_id is None:
			raise TypeError("identityUserFlowAttribute_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["identityUserFlowAttribute%2Did"] =  identityUserFlowAttribute_id

		from .by_identity_user_flow_attribute_id import ByIdentityUserFlowAttributeIdRequest
		return ByIdentityUserFlowAttributeIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

