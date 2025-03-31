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
	from .last_modified_by import LastModifiedByRequest
	from .created_by import CreatedByRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCustomTaskExtensionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/customTaskExtensions/{customTaskExtension%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceCustomTaskExtension:
		"""
		Get customTaskExtension
		Read the properties and relationships of a customTaskExtension object.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-customtaskextension-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceCustomTaskExtension, error_mapping)

	async def patch(
		self,
		body: IdentityGovernanceCustomTaskExtension,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityGovernanceCustomTaskExtension:
		"""
		Update customTaskExtension
		Update the properties of a customTaskExtension object.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-customtaskextension-update?view=graph-rest-beta
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, IdentityGovernanceCustomTaskExtension, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete customTaskExtension
		Delete a customTaskExtension object. A custom task extension  can only be deleted if it is not referenced in any task objects in a lifecycle workflow.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-customtaskextension-delete?view=graph-rest-beta
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByCustomTaskExtensionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCustomTaskExtensionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCustomTaskExtensionIdRequest(self.request_adapter, self.path_parameters)

	def created_by(self,
		customTaskExtension_id: str,
	) -> CreatedByRequest:
		if customTaskExtension_id is None:
			raise TypeError("customTaskExtension_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["customTaskExtension%2Did"] =  customTaskExtension_id

		from .created_by import CreatedByRequest
		return CreatedByRequest(self.request_adapter, path_parameters)

	def last_modified_by(self,
		customTaskExtension_id: str,
	) -> LastModifiedByRequest:
		if customTaskExtension_id is None:
			raise TypeError("customTaskExtension_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["customTaskExtension%2Did"] =  customTaskExtension_id

		from .last_modified_by import LastModifiedByRequest
		return LastModifiedByRequest(self.request_adapter, path_parameters)

