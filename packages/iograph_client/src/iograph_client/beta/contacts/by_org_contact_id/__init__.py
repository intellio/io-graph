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
	from .transitive_reports import TransitiveReportsRequest
	from .transitive_member_of import TransitiveMemberOfRequest
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .retry_service_provisioning import RetryServiceProvisioningRequest
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .member_of import MemberOfRequest
	from .manager import ManagerRequest
	from .direct_reports import DirectReportsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.org_contact import OrgContact
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByOrgContactIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/contacts/{orgContact%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OrgContact:
		"""
		Get orgContact
		Get the properties and relationships of an organizational contact object.
		Find more info here: https://learn.microsoft.com/graph/api/orgcontact-get?view=graph-rest-beta
		"""
		tags = ['contacts.orgContact']

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
		return await self.request_adapter.send_async(request_info, OrgContact, error_mapping)

	async def patch(
		self,
		body: OrgContact,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OrgContact:
		"""
		Update entity in contacts
		
		"""
		tags = ['contacts.orgContact']

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
		return await self.request_adapter.send_async(request_info, OrgContact, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from contacts
		
		"""
		tags = ['contacts.orgContact']
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



	def with_url(self, raw_url: str) -> ByOrgContactIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOrgContactIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOrgContactIdRequest(self.request_adapter, self.path_parameters)

	def direct_reports(self,
		orgContact_id: str,
	) -> DirectReportsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .direct_reports import DirectReportsRequest
		return DirectReportsRequest(self.request_adapter, path_parameters)

	def manager(self,
		orgContact_id: str,
	) -> ManagerRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .manager import ManagerRequest
		return ManagerRequest(self.request_adapter, path_parameters)

	def member_of(self,
		orgContact_id: str,
	) -> MemberOfRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		orgContact_id: str,
	) -> CheckMemberGroupsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		orgContact_id: str,
	) -> CheckMemberObjectsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		orgContact_id: str,
	) -> GetMemberGroupsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		orgContact_id: str,
	) -> GetMemberObjectsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def restore(self,
		orgContact_id: str,
	) -> RestoreRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def retry_service_provisioning(self,
		orgContact_id: str,
	) -> RetryServiceProvisioningRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .retry_service_provisioning import RetryServiceProvisioningRequest
		return RetryServiceProvisioningRequest(self.request_adapter, path_parameters)

	def service_provisioning_errors(self,
		orgContact_id: str,
	) -> ServiceProvisioningErrorsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, path_parameters)

	def transitive_member_of(self,
		orgContact_id: str,
	) -> TransitiveMemberOfRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, path_parameters)

	def transitive_reports(self,
		orgContact_id: str,
	) -> TransitiveReportsRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .transitive_reports import TransitiveReportsRequest
		return TransitiveReportsRequest(self.request_adapter, path_parameters)

