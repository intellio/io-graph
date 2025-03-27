# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class JoinRequestRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/multiTenantOrganization/joinRequest", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MultiTenantOrganizationJoinRequestRecord:
		"""
		Get multiTenantOrganizationJoinRequestRecord
		Get the status of a tenant joining a multitenant organization.
		Find more info here: https://learn.microsoft.com/graph/api/multitenantorganizationjoinrequestrecord-get?view=graph-rest-1.0
		"""
		tags = ['tenantRelationships.multiTenantOrganization']

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
		return await self.request_adapter.send_async(request_info, MultiTenantOrganizationJoinRequestRecord, error_mapping)

	async def patch(
		self,
		body: MultiTenantOrganizationJoinRequestRecord,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MultiTenantOrganizationJoinRequestRecord:
		"""
		Update multiTenantOrganizationJoinRequestRecord
		Join a multitenant organization, after the owner of the multitenant organization has added your tenant to the multitenant organization as pending. Before a tenant added to a multitenant organization can participate in the multitenant organization, the administrator of the joining tenant must submit a join request. To allow for asynchronous processing, you must wait up to 2 hours before joining a multitenant organization is completed.
		Find more info here: https://learn.microsoft.com/graph/api/multitenantorganizationjoinrequestrecord-update?view=graph-rest-1.0
		"""
		tags = ['tenantRelationships.multiTenantOrganization']

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
		return await self.request_adapter.send_async(request_info, MultiTenantOrganizationJoinRequestRecord, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> JoinRequestRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: JoinRequestRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return JoinRequestRequest(self.request_adapter, self.path_parameters)

