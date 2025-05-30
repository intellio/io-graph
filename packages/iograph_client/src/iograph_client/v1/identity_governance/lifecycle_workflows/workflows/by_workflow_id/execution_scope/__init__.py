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
	from .by_user_processing_result_id import ByUserProcessingResultIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.identity_governance_user_processing_result_collection_response import IdentityGovernanceUserProcessingResultCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ExecutionScopeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/executionScope", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceUserProcessingResultCollectionResponse:
		"""
		Get executionScope from identityGovernance
		The unique identifier of the Microsoft Entra identity that last modified the workflow object.
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceUserProcessingResultCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ExecutionScopeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ExecutionScopeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ExecutionScopeRequest(self.request_adapter, self.path_parameters)

	def by_user_processing_result_id(self,
		workflow_id: str,
		userProcessingResult_id: str,
	) -> ByUserProcessingResultIdRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if userProcessingResult_id is None:
			raise TypeError("userProcessingResult_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["userProcessingResult%2Did"] =  userProcessingResult_id

		from .by_user_processing_result_id import ByUserProcessingResultIdRequest
		return ByUserProcessingResultIdRequest(self.request_adapter, path_parameters)

	def count(self,
		workflow_id: str,
	) -> CountRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

