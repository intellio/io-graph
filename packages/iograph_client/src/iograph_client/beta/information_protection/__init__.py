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
	from .threat_assessment_requests import ThreatAssessmentRequestsRequest
	from .sensitivity_policy_settings import SensitivityPolicySettingsRequest
	from .sensitivity_labels import SensitivityLabelsRequest
	from .policy import PolicyRequest
	from .verify_signature import VerifySignatureRequest
	from .sign_digest import SignDigestRequest
	from .encrypt_buffer import EncryptBufferRequest
	from .decrypt_buffer import DecryptBufferRequest
	from .data_loss_prevention_policies import DataLossPreventionPoliciesRequest
	from .bitlocker import BitlockerRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.information_protection import InformationProtection


class InformationProtectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/informationProtection", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InformationProtection:
		"""
		Get informationProtection
		
		"""
		tags = ['informationProtection.informationProtection']

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
		return await self.request_adapter.send_async(request_info, InformationProtection, error_mapping)

	async def patch(
		self,
		body: InformationProtection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InformationProtection:
		"""
		Update informationProtection
		
		"""
		tags = ['informationProtection.informationProtection']

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
		return await self.request_adapter.send_async(request_info, InformationProtection, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> InformationProtectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: InformationProtectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return InformationProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def bitlocker(self,
	) -> BitlockerRequest:
		from .bitlocker import BitlockerRequest
		return BitlockerRequest(self.request_adapter, self.path_parameters)

	@property
	def data_loss_prevention_policies(self,
	) -> DataLossPreventionPoliciesRequest:
		from .data_loss_prevention_policies import DataLossPreventionPoliciesRequest
		return DataLossPreventionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def decrypt_buffer(self,
	) -> DecryptBufferRequest:
		from .decrypt_buffer import DecryptBufferRequest
		return DecryptBufferRequest(self.request_adapter, self.path_parameters)

	@property
	def encrypt_buffer(self,
	) -> EncryptBufferRequest:
		from .encrypt_buffer import EncryptBufferRequest
		return EncryptBufferRequest(self.request_adapter, self.path_parameters)

	@property
	def sign_digest(self,
	) -> SignDigestRequest:
		from .sign_digest import SignDigestRequest
		return SignDigestRequest(self.request_adapter, self.path_parameters)

	@property
	def verify_signature(self,
	) -> VerifySignatureRequest:
		from .verify_signature import VerifySignatureRequest
		return VerifySignatureRequest(self.request_adapter, self.path_parameters)

	@property
	def policy(self,
	) -> PolicyRequest:
		from .policy import PolicyRequest
		return PolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def sensitivity_labels(self,
	) -> SensitivityLabelsRequest:
		from .sensitivity_labels import SensitivityLabelsRequest
		return SensitivityLabelsRequest(self.request_adapter, self.path_parameters)

	@property
	def sensitivity_policy_settings(self,
	) -> SensitivityPolicySettingsRequest:
		from .sensitivity_policy_settings import SensitivityPolicySettingsRequest
		return SensitivityPolicySettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def threat_assessment_requests(self,
	) -> ThreatAssessmentRequestsRequest:
		from .threat_assessment_requests import ThreatAssessmentRequestsRequest
		return ThreatAssessmentRequestsRequest(self.request_adapter, self.path_parameters)

