# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .upload_externally_signed_certification_authority_certificate import UploadExternallySignedCertificationAuthorityCertificateRequest
	from .search_cloud_certification_authority_leaf_certificate_by_serial_number import SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest
	from .revoke_leaf_certificate_by_serial_number import RevokeLeafCertificateBySerialNumberRequest
	from .revoke_leaf_certificate import RevokeLeafCertificateRequest
	from .revoke_cloud_certification_authority_certificate import RevokeCloudCertificationAuthorityCertificateRequest
	from .post_cloud_certification_authority import PostCloudCertificationAuthorityRequest
	from .patch_cloud_certification_authority import PatchCloudCertificationAuthorityRequest
	from .get_cloud_certification_authority import GetCloudCertificationAuthorityRequest
	from .get_all_cloud_certification_authority_leaf_certificates import GetAllCloudCertificationAuthorityLeafCertificatesRequest
	from .get_all_cloud_certification_authority import GetAllCloudCertificationAuthorityRequest
	from .change_cloud_certification_authority_status import ChangeCloudCertificationAuthorityStatusRequest
	from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificateRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.cloud_certification_authority import CloudCertificationAuthority
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCloudCertificationAuthorityIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/cloudCertificationAuthority/{cloudCertificationAuthority%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudCertificationAuthority:
		"""
		Get cloudCertificationAuthority from deviceManagement
		Collection of CloudCertificationAuthority records associated with account.
		"""
		tags = ['deviceManagement.cloudCertificationAuthority']

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
		return await self.request_adapter.send_async(request_info, CloudCertificationAuthority, error_mapping)

	async def patch(
		self,
		body: CloudCertificationAuthority,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudCertificationAuthority:
		"""
		Update the navigation property cloudCertificationAuthority in deviceManagement
		
		"""
		tags = ['deviceManagement.cloudCertificationAuthority']

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
		return await self.request_adapter.send_async(request_info, CloudCertificationAuthority, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property cloudCertificationAuthority for deviceManagement
		
		"""
		tags = ['deviceManagement.cloudCertificationAuthority']
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



	def with_url(self, raw_url: str) -> ByCloudCertificationAuthorityIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCloudCertificationAuthorityIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCloudCertificationAuthorityIdRequest(self.request_adapter, self.path_parameters)

	def cloud_certification_authority_leaf_certificate(self,
		cloudCertificationAuthority_id: str,
	) -> CloudCertificationAuthorityLeafCertificateRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificateRequest
		return CloudCertificationAuthorityLeafCertificateRequest(self.request_adapter, path_parameters)

	def change_cloud_certification_authority_status(self,
		cloudCertificationAuthority_id: str,
	) -> ChangeCloudCertificationAuthorityStatusRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .change_cloud_certification_authority_status import ChangeCloudCertificationAuthorityStatusRequest
		return ChangeCloudCertificationAuthorityStatusRequest(self.request_adapter, path_parameters)

	def get_all_cloud_certification_authority(self,
		cloudCertificationAuthority_id: str,
	) -> GetAllCloudCertificationAuthorityRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .get_all_cloud_certification_authority import GetAllCloudCertificationAuthorityRequest
		return GetAllCloudCertificationAuthorityRequest(self.request_adapter, path_parameters)

	def get_all_cloud_certification_authority_leaf_certificates(self,
		cloudCertificationAuthority_id: str,
	) -> GetAllCloudCertificationAuthorityLeafCertificatesRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .get_all_cloud_certification_authority_leaf_certificates import GetAllCloudCertificationAuthorityLeafCertificatesRequest
		return GetAllCloudCertificationAuthorityLeafCertificatesRequest(self.request_adapter, path_parameters)

	def get_cloud_certification_authority(self,
		cloudCertificationAuthority_id: str,
	) -> GetCloudCertificationAuthorityRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .get_cloud_certification_authority import GetCloudCertificationAuthorityRequest
		return GetCloudCertificationAuthorityRequest(self.request_adapter, path_parameters)

	def patch_cloud_certification_authority(self,
		cloudCertificationAuthority_id: str,
	) -> PatchCloudCertificationAuthorityRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .patch_cloud_certification_authority import PatchCloudCertificationAuthorityRequest
		return PatchCloudCertificationAuthorityRequest(self.request_adapter, path_parameters)

	def post_cloud_certification_authority(self,
		cloudCertificationAuthority_id: str,
	) -> PostCloudCertificationAuthorityRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .post_cloud_certification_authority import PostCloudCertificationAuthorityRequest
		return PostCloudCertificationAuthorityRequest(self.request_adapter, path_parameters)

	def revoke_cloud_certification_authority_certificate(self,
		cloudCertificationAuthority_id: str,
	) -> RevokeCloudCertificationAuthorityCertificateRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .revoke_cloud_certification_authority_certificate import RevokeCloudCertificationAuthorityCertificateRequest
		return RevokeCloudCertificationAuthorityCertificateRequest(self.request_adapter, path_parameters)

	def revoke_leaf_certificate(self,
		cloudCertificationAuthority_id: str,
	) -> RevokeLeafCertificateRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .revoke_leaf_certificate import RevokeLeafCertificateRequest
		return RevokeLeafCertificateRequest(self.request_adapter, path_parameters)

	def revoke_leaf_certificate_by_serial_number(self,
		cloudCertificationAuthority_id: str,
	) -> RevokeLeafCertificateBySerialNumberRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .revoke_leaf_certificate_by_serial_number import RevokeLeafCertificateBySerialNumberRequest
		return RevokeLeafCertificateBySerialNumberRequest(self.request_adapter, path_parameters)

	def search_cloud_certification_authority_leaf_certificate_by_serial_number(self,
		cloudCertificationAuthority_id: str,
	) -> SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .search_cloud_certification_authority_leaf_certificate_by_serial_number import SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest
		return SearchCloudCertificationAuthorityLeafCertificateBySerialNumberRequest(self.request_adapter, path_parameters)

	def upload_externally_signed_certification_authority_certificate(self,
		cloudCertificationAuthority_id: str,
	) -> UploadExternallySignedCertificationAuthorityCertificateRequest:
		if cloudCertificationAuthority_id is None:
			raise TypeError("cloudCertificationAuthority_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudCertificationAuthority%2Did"] =  cloudCertificationAuthority_id

		from .upload_externally_signed_certification_authority_certificate import UploadExternallySignedCertificationAuthorityCertificateRequest
		return UploadExternallySignedCertificationAuthorityCertificateRequest(self.request_adapter, path_parameters)

