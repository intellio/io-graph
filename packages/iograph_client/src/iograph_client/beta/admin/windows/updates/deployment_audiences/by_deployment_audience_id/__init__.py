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
	from .windows_updates_update_audience_by_id import WindowsUpdatesUpdateAudienceByIdRequest
	from .windows_updates_update_audience import WindowsUpdatesUpdateAudienceRequest
	from .members import MembersRequest
	from .exclusions import ExclusionsRequest
	from .applicable_content import ApplicableContentRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.windows_updates_deployment_audience import WindowsUpdatesDeploymentAudience


class ByDeploymentAudienceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/deploymentAudiences/{deploymentAudience%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesDeploymentAudience:
		"""
		Get deploymentAudience
		Read the properties and relationships of a deploymentAudience object.
		Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-deploymentaudience-get?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesDeploymentAudience, error_mapping)

	async def patch(
		self,
		body: WindowsUpdatesDeploymentAudience,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesDeploymentAudience:
		"""
		Update the navigation property deploymentAudiences in admin
		
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesDeploymentAudience, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete deploymentAudience
		Delete a deploymentAudience object.
		Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-deploymentaudience-delete?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']
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



	def with_url(self, raw_url: str) -> ByDeploymentAudienceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeploymentAudienceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeploymentAudienceIdRequest(self.request_adapter, self.path_parameters)

	def applicable_content(self,
		deploymentAudience_id: str,
	) -> ApplicableContentRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id

		from .applicable_content import ApplicableContentRequest
		return ApplicableContentRequest(self.request_adapter, path_parameters)

	def exclusions(self,
		deploymentAudience_id: str,
	) -> ExclusionsRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id

		from .exclusions import ExclusionsRequest
		return ExclusionsRequest(self.request_adapter, path_parameters)

	def members(self,
		deploymentAudience_id: str,
	) -> MembersRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def windows_updates_update_audience(self,
		deploymentAudience_id: str,
	) -> WindowsUpdatesUpdateAudienceRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id

		from .windows_updates_update_audience import WindowsUpdatesUpdateAudienceRequest
		return WindowsUpdatesUpdateAudienceRequest(self.request_adapter, path_parameters)

	def windows_updates_update_audience_by_id(self,
		deploymentAudience_id: str,
	) -> WindowsUpdatesUpdateAudienceByIdRequest:
		if deploymentAudience_id is None:
			raise TypeError("deploymentAudience_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deploymentAudience%2Did"] =  deploymentAudience_id

		from .windows_updates_update_audience_by_id import WindowsUpdatesUpdateAudienceByIdRequest
		return WindowsUpdatesUpdateAudienceByIdRequest(self.request_adapter, path_parameters)

