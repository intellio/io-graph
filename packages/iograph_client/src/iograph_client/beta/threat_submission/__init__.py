# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .url_threats import UrlThreatsRequest
	from .file_threats import FileThreatsRequest
	from .email_threat_submission_policies import EmailThreatSubmissionPoliciesRequest
	from .email_threats import EmailThreatsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_threat_submission_root import SecurityThreatSubmissionRoot
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ThreatSubmissionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/threatSubmission", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityThreatSubmissionRoot:
		"""
		Get threatSubmission
		
		"""
		tags = ['threatSubmission.threatSubmissionRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityThreatSubmissionRoot, error_mapping)

	async def patch(
		self,
		body: SecurityThreatSubmissionRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityThreatSubmissionRoot:
		"""
		Update threatSubmission
		
		"""
		tags = ['threatSubmission.threatSubmissionRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityThreatSubmissionRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ThreatSubmissionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ThreatSubmissionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ThreatSubmissionRequest(self.request_adapter, self.path_parameters)

	@property
	def email_threats(self,
	) -> EmailThreatsRequest:
		from .email_threats import EmailThreatsRequest
		return EmailThreatsRequest(self.request_adapter, self.path_parameters)

	@property
	def email_threat_submission_policies(self,
	) -> EmailThreatSubmissionPoliciesRequest:
		from .email_threat_submission_policies import EmailThreatSubmissionPoliciesRequest
		return EmailThreatSubmissionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def file_threats(self,
	) -> FileThreatsRequest:
		from .file_threats import FileThreatsRequest
		return FileThreatsRequest(self.request_adapter, self.path_parameters)

	@property
	def url_threats(self,
	) -> UrlThreatsRequest:
		from .url_threats import UrlThreatsRequest
		return UrlThreatsRequest(self.request_adapter, self.path_parameters)

