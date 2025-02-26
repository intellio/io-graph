# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_mobile_app_assignment_id import ByMobileAppAssignmentIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.mobile_app_assignment import MobileAppAssignment
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.mobile_app_assignment_collection_response import MobileAppAssignmentCollectionResponse


class AssignmentsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.windowsMobileMSI/assignments"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MobileAppAssignmentCollectionResponse:
		"""
		Get assignments from deviceAppManagement
		The list of group assignments for this mobile app.
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, MobileAppAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: MobileAppAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MobileAppAssignment:
		"""
		Create new navigation property to assignments for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mobileApp']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, MobileAppAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_mobile_app_assignment_id(self,
		mobileApp_id: str,
		mobileAppAssignment_id: str,
	) -> ByMobileAppAssignmentIdRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")
		if mobileAppAssignment_id is None:
			raise TypeError("mobileAppAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id
		path_parameters["mobileAppAssignment%2Did"] =  mobileAppAssignment_id

		from .by_mobile_app_assignment_id import ByMobileAppAssignmentIdRequest
		return ByMobileAppAssignmentIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

