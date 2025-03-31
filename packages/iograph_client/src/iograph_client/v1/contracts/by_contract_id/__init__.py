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
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.contract import Contract
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByContractIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/contracts/{contract%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Contract:
		"""
		Get Contract
		Retrieve the properties and relationships of contract object.
		Find more info here: https://learn.microsoft.com/graph/api/contract-get?view=graph-rest-1.0
		"""
		tags = ['contracts.contract']

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
		return await self.request_adapter.send_async(request_info, Contract, error_mapping)

	async def patch(
		self,
		body: Contract,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Contract:
		"""
		Update entity in contracts
		
		"""
		tags = ['contracts.contract']

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
		return await self.request_adapter.send_async(request_info, Contract, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from contracts
		
		"""
		tags = ['contracts.contract']
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



	def with_url(self, raw_url: str) -> ByContractIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByContractIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByContractIdRequest(self.request_adapter, self.path_parameters)

	def check_member_groups(self,
		contract_id: str,
	) -> CheckMemberGroupsRequest:
		if contract_id is None:
			raise TypeError("contract_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contract%2Did"] =  contract_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		contract_id: str,
	) -> CheckMemberObjectsRequest:
		if contract_id is None:
			raise TypeError("contract_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contract%2Did"] =  contract_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		contract_id: str,
	) -> GetMemberGroupsRequest:
		if contract_id is None:
			raise TypeError("contract_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contract%2Did"] =  contract_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		contract_id: str,
	) -> GetMemberObjectsRequest:
		if contract_id is None:
			raise TypeError("contract_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contract%2Did"] =  contract_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def restore(self,
		contract_id: str,
	) -> RestoreRequest:
		if contract_id is None:
			raise TypeError("contract_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contract%2Did"] =  contract_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

