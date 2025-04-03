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
	from .user_state_summary import UserStateSummaryRequest
	from .assign import AssignRequest
	from .install_summary import InstallSummaryRequest
	from .device_states import DeviceStatesRequest
	from .categories import CategoriesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.managed_e_book import ManagedEBook


class ByManagedEBookIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/managedEBooks/{managedEBook%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedEBook:
		"""
		Get managedEBooks from deviceAppManagement
		The Managed eBook.
		"""
		tags = ['deviceAppManagement.managedEBook']

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
		return await self.request_adapter.send_async(request_info, ManagedEBook, error_mapping)

	async def patch(
		self,
		body: ManagedEBook,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedEBook:
		"""
		Update the navigation property managedEBooks in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.managedEBook']

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
		return await self.request_adapter.send_async(request_info, ManagedEBook, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property managedEBooks for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.managedEBook']
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



	def with_url(self, raw_url: str) -> ByManagedEBookIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByManagedEBookIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByManagedEBookIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		managedEBook_id: str,
	) -> AssignmentsRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def categories(self,
		managedEBook_id: str,
	) -> CategoriesRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, path_parameters)

	def device_states(self,
		managedEBook_id: str,
	) -> DeviceStatesRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .device_states import DeviceStatesRequest
		return DeviceStatesRequest(self.request_adapter, path_parameters)

	def install_summary(self,
		managedEBook_id: str,
	) -> InstallSummaryRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .install_summary import InstallSummaryRequest
		return InstallSummaryRequest(self.request_adapter, path_parameters)

	def assign(self,
		managedEBook_id: str,
	) -> AssignRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def user_state_summary(self,
		managedEBook_id: str,
	) -> UserStateSummaryRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .user_state_summary import UserStateSummaryRequest
		return UserStateSummaryRequest(self.request_adapter, path_parameters)

