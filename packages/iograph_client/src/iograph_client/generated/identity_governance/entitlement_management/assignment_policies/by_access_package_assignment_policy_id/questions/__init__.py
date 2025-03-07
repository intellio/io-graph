# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_access_package_question_id import ByAccessPackageQuestionIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.access_package_question_collection_response import AccessPackageQuestionCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.access_package_question import AccessPackageQuestion


class QuestionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentPolicies/{accessPackageAssignmentPolicy%2Did}/questions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageQuestionCollectionResponse:
		"""
		Get questions from identityGovernance
		Questions that are posed to the  requestor.
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageQuestionCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessPackageQuestion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageQuestion:
		"""
		Create new navigation property to questions for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageQuestion, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> QuestionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: QuestionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return QuestionsRequest(self.request_adapter, self.path_parameters)

	def by_access_package_question_id(self,
		accessPackageAssignmentPolicy_id: str,
		accessPackageQuestion_id: str,
	) -> ByAccessPackageQuestionIdRequest:
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")
		if accessPackageQuestion_id is None:
			raise TypeError("accessPackageQuestion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id
		path_parameters["accessPackageQuestion%2Did"] =  accessPackageQuestion_id

		from .by_access_package_question_id import ByAccessPackageQuestionIdRequest
		return ByAccessPackageQuestionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		accessPackageAssignmentPolicy_id: str,
	) -> CountRequest:
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

