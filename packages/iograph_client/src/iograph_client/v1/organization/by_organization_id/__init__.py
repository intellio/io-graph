# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .set_mobile_device_management_authority import SetMobileDeviceManagementAuthorityRequest
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .extensions import ExtensionsRequest
	from .certificate_based_auth_configuration import CertificateBasedAuthConfigurationRequest
	from .branding import BrandingRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.organization import Organization


class ByOrganizationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Organization:
		"""
		Get organization
		Read properties and relationships of the organization object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-organization-get?view=graph-rest-1.0
		"""
		tags = ['organization.organization']

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
		return await self.request_adapter.send_async(request_info, Organization, error_mapping)

	async def patch(
		self,
		body: Organization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Organization:
		"""
		Update organization
		Update the properties of a organization object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-organization-update?view=graph-rest-1.0
		"""
		tags = ['organization.organization']

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
		return await self.request_adapter.send_async(request_info, Organization, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from organization
		
		"""
		tags = ['organization.organization']
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



	def with_url(self, raw_url: str) -> ByOrganizationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOrganizationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOrganizationIdRequest(self.request_adapter, self.path_parameters)

	def branding(self,
		organization_id: str,
	) -> BrandingRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .branding import BrandingRequest
		return BrandingRequest(self.request_adapter, path_parameters)

	def certificate_based_auth_configuration(self,
		organization_id: str,
	) -> CertificateBasedAuthConfigurationRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .certificate_based_auth_configuration import CertificateBasedAuthConfigurationRequest
		return CertificateBasedAuthConfigurationRequest(self.request_adapter, path_parameters)

	def extensions(self,
		organization_id: str,
	) -> ExtensionsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		organization_id: str,
	) -> CheckMemberGroupsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		organization_id: str,
	) -> CheckMemberObjectsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		organization_id: str,
	) -> GetMemberGroupsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		organization_id: str,
	) -> GetMemberObjectsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def restore(self,
		organization_id: str,
	) -> RestoreRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def set_mobile_device_management_authority(self,
		organization_id: str,
	) -> SetMobileDeviceManagementAuthorityRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .set_mobile_device_management_authority import SetMobileDeviceManagementAuthorityRequest
		return SetMobileDeviceManagementAuthorityRequest(self.request_adapter, path_parameters)

