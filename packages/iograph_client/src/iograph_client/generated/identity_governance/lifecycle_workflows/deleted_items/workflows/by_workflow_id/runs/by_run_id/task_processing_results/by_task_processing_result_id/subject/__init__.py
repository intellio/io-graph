# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .mailbox_settings import MailboxSettingsRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.models.user import User
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SubjectRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/runs/{run%2Did}/taskProcessingResults/{taskProcessingResult%2Did}/subject", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> User:
		"""
		Get subject from identityGovernance
		The unique identifier of the Microsoft Entra user targeted for the task execution.Supports $filter(eq, ne) and $expand.
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
		return await self.request_adapter.send_async(request_info, User, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> SubjectRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SubjectRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SubjectRequest(self.request_adapter, self.path_parameters)

	def mailbox_settings(self,
		workflow_id: str,
		run_id: str,
		taskProcessingResult_id: str,
	) -> MailboxSettingsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if run_id is None:
			raise TypeError("run_id cannot be null.")
		if taskProcessingResult_id is None:
			raise TypeError("taskProcessingResult_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["run%2Did"] =  run_id
		path_parameters["taskProcessingResult%2Did"] =  taskProcessingResult_id

		from .mailbox_settings import MailboxSettingsRequest
		return MailboxSettingsRequest(self.request_adapter, path_parameters)

	def service_provisioning_errors(self,
		workflow_id: str,
		run_id: str,
		taskProcessingResult_id: str,
	) -> ServiceProvisioningErrorsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if run_id is None:
			raise TypeError("run_id cannot be null.")
		if taskProcessingResult_id is None:
			raise TypeError("taskProcessingResult_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["run%2Did"] =  run_id
		path_parameters["taskProcessingResult%2Did"] =  taskProcessingResult_id

		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, path_parameters)

