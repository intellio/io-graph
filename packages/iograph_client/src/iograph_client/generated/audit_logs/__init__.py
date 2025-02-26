# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sign_ins import SignInsRequest
	from .provisioning import ProvisioningRequest
	from .directory_audits import DirectoryAuditsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.audit_log_root import AuditLogRoot


class AuditLogsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/auditLogs"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuditLogRoot:
		"""
		Get auditLogs
		
		"""
		tags = ['auditLogs.auditLogRoot']

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
		return await self.request_adapter.send_async(request_info, AuditLogRoot, error_mapping)

	async def patch(
		self,
		body: AuditLogRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuditLogRoot:
		"""
		Update auditLogs
		
		"""
		tags = ['auditLogs.auditLogRoot']

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
		return await self.request_adapter.send_async(request_info, AuditLogRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	@property
	def directory_audits(self,
	) -> DirectoryAuditsRequest:
		from .directory_audits import DirectoryAuditsRequest
		return DirectoryAuditsRequest(self.request_adapter, self.path_parameters)

	@property
	def provisioning(self,
	) -> ProvisioningRequest:
		from .provisioning import ProvisioningRequest
		return ProvisioningRequest(self.request_adapter, self.path_parameters)

	@property
	def sign_ins(self,
	) -> SignInsRequest:
		from .sign_ins import SignInsRequest
		return SignInsRequest(self.request_adapter, self.path_parameters)

