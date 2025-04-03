# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .validate_properties import ValidatePropertiesRequest
	from .get_user_owned_objects import GetUserOwnedObjectsRequest
	from .get_by_ids import GetByIdsRequest
	from .evaluate_dynamic_membership import EvaluateDynamicMembershipRequest
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_group_id import ByGroupIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_collection_response import GroupCollectionResponse
from iograph_models.beta.group import Group


class GroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupCollectionResponse:
		"""
		List groups
		List all the groups available in an organization, excluding dynamic distribution groups. To retrieve dynamic distribution groups, use the Exchange admin center. This operation returns by default only a subset of the more commonly used properties for each group. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the group and specify the properties in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and are not returned in the $select query.
		Find more info here: https://learn.microsoft.com/graph/api/group-list?view=graph-rest-beta
		"""
		tags = ['groups.group']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		return await self.request_adapter.send_async(request_info, GroupCollectionResponse, error_mapping)

	async def post(
		self,
		body: Group,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Group:
		"""
		Create group
		Create a new group as specified in the request body. You can create one of the following groups: This operation returns by default only a subset of the properties for each group. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option. Note: To create a team, first create a group then add a team to it, see create team.
		Find more info here: https://learn.microsoft.com/graph/api/group-post-groups?view=graph-rest-beta
		"""
		tags = ['groups.group']

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
		return await self.request_adapter.send_async(request_info, Group, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> GroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GroupsRequest(self.request_adapter, self.path_parameters)

	def by_group_id(self,
		group_id: str,
	) -> ByGroupIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .by_group_id import ByGroupIdRequest
		return ByGroupIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_dynamic_membership(self,
	) -> EvaluateDynamicMembershipRequest:
		from .evaluate_dynamic_membership import EvaluateDynamicMembershipRequest
		return EvaluateDynamicMembershipRequest(self.request_adapter, self.path_parameters)

	@property
	def get_by_ids(self,
	) -> GetByIdsRequest:
		from .get_by_ids import GetByIdsRequest
		return GetByIdsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_user_owned_objects(self,
	) -> GetUserOwnedObjectsRequest:
		from .get_user_owned_objects import GetUserOwnedObjectsRequest
		return GetUserOwnedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_properties(self,
	) -> ValidatePropertiesRequest:
		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, self.path_parameters)

