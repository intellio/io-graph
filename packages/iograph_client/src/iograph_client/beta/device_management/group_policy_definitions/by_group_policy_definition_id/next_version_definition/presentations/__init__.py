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
	from .count import CountRequest
	from .by_group_policy_presentation_id import ByGroupPolicyPresentationIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_policy_presentation_collection_response import GroupPolicyPresentationCollectionResponse
from iograph_models.beta.group_policy_presentation import GroupPolicyPresentation


class PresentationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyDefinitions/{groupPolicyDefinition%2Did}/nextVersionDefinition/presentations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyPresentationCollectionResponse:
		"""
		Get presentations from deviceManagement
		The group policy presentations associated with the definition.
		"""
		tags = ['deviceManagement.groupPolicyDefinition']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyPresentationCollectionResponse, error_mapping)

	async def post(
		self,
		body: GroupPolicyPresentation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyPresentation:
		"""
		Create new navigation property to presentations for deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyDefinition']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyPresentation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PresentationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PresentationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PresentationsRequest(self.request_adapter, self.path_parameters)

	def by_group_policy_presentation_id(self,
		groupPolicyDefinition_id: str,
		groupPolicyPresentation_id: str,
	) -> ByGroupPolicyPresentationIdRequest:
		if groupPolicyDefinition_id is None:
			raise TypeError("groupPolicyDefinition_id cannot be null.")
		if groupPolicyPresentation_id is None:
			raise TypeError("groupPolicyPresentation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyDefinition%2Did"] =  groupPolicyDefinition_id
		path_parameters["groupPolicyPresentation%2Did"] =  groupPolicyPresentation_id

		from .by_group_policy_presentation_id import ByGroupPolicyPresentationIdRequest
		return ByGroupPolicyPresentationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		groupPolicyDefinition_id: str,
	) -> CountRequest:
		if groupPolicyDefinition_id is None:
			raise TypeError("groupPolicyDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyDefinition%2Did"] =  groupPolicyDefinition_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

