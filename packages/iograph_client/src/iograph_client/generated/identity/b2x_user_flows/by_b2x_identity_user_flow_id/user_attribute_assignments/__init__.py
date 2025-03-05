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
	from .set_order import SetOrderRequest
	from .get_order import GetOrderRequest
	from .count import CountRequest
	from .by_identity_user_flow_attribute_assignment_id import ByIdentityUserFlowAttributeAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
from iograph_models.models.identity_user_flow_attribute_assignment_collection_response import IdentityUserFlowAttributeAssignmentCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class UserAttributeAssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/userAttributeAssignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityUserFlowAttributeAssignmentCollectionResponse:
		"""
		List userAttributeAssignments
		Get the identityUserFlowAttributeAssignment resources from the userAttributeAssignments navigation property in a b2xIdentityUserFlow.
		Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-list-userattributeassignments?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, IdentityUserFlowAttributeAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: IdentityUserFlowAttributeAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityUserFlowAttributeAssignment:
		"""
		Create userAttributeAssignments
		Create a new identityUserFlowAttributeAssignment object in a b2xIdentityUserFlow.
		Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-post-userattributeassignments?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, IdentityUserFlowAttributeAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserAttributeAssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserAttributeAssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserAttributeAssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_identity_user_flow_attribute_assignment_id(self,
		b2xIdentityUserFlow_id: str,
		identityUserFlowAttributeAssignment_id: str,
	) -> ByIdentityUserFlowAttributeAssignmentIdRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")
		if identityUserFlowAttributeAssignment_id is None:
			raise TypeError("identityUserFlowAttributeAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id
		path_parameters["identityUserFlowAttributeAssignment%2Did"] =  identityUserFlowAttributeAssignment_id

		from .by_identity_user_flow_attribute_assignment_id import ByIdentityUserFlowAttributeAssignmentIdRequest
		return ByIdentityUserFlowAttributeAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		b2xIdentityUserFlow_id: str,
	) -> CountRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def get_order(self,
		b2xIdentityUserFlow_id: str,
	) -> GetOrderRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .get_order import GetOrderRequest
		return GetOrderRequest(self.request_adapter, path_parameters)

	def set_order(self,
		b2xIdentityUserFlow_id: str,
	) -> SetOrderRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .set_order import SetOrderRequest
		return SetOrderRequest(self.request_adapter, path_parameters)

