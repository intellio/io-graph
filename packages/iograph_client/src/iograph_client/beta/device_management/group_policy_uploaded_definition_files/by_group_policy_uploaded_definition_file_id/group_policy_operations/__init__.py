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
	from .count import CountRequest
	from .by_group_policy_operation_id import ByGroupPolicyOperationIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.group_policy_operation import GroupPolicyOperation
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_policy_operation_collection_response import GroupPolicyOperationCollectionResponse


class GroupPolicyOperationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyUploadedDefinitionFiles/{groupPolicyUploadedDefinitionFile%2Did}/groupPolicyOperations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyOperationCollectionResponse:
		"""
		Get groupPolicyOperations from deviceManagement
		The list of operations on the uploaded ADMX file.
		"""
		tags = ['deviceManagement.groupPolicyUploadedDefinitionFile']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyOperationCollectionResponse, error_mapping)

	async def post(
		self,
		body: GroupPolicyOperation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyOperation:
		"""
		Create new navigation property to groupPolicyOperations for deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyUploadedDefinitionFile']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyOperation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> GroupPolicyOperationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GroupPolicyOperationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GroupPolicyOperationsRequest(self.request_adapter, self.path_parameters)

	def by_group_policy_operation_id(self,
		groupPolicyUploadedDefinitionFile_id: str,
		groupPolicyOperation_id: str,
	) -> ByGroupPolicyOperationIdRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")
		if groupPolicyOperation_id is None:
			raise TypeError("groupPolicyOperation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id
		path_parameters["groupPolicyOperation%2Did"] =  groupPolicyOperation_id

		from .by_group_policy_operation_id import ByGroupPolicyOperationIdRequest
		return ByGroupPolicyOperationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		groupPolicyUploadedDefinitionFile_id: str,
	) -> CountRequest:
		if groupPolicyUploadedDefinitionFile_id is None:
			raise TypeError("groupPolicyUploadedDefinitionFile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyUploadedDefinitionFile%2Did"] =  groupPolicyUploadedDefinitionFile_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

