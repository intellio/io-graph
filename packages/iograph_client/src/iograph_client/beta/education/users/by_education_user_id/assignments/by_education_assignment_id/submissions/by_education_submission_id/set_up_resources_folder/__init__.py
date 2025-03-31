# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.education_submission import EducationSubmission
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SetUpResourcesFolderRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/users/{educationUser%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/setUpResourcesFolder", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationSubmission:
		"""
		Invoke action setUpResourcesFolder
		Trigger the creation of the SharePoint resource folder where all file-based resources (Word, Excel, and so on) should be uploaded for a given submission. Only teachers and students can perform this operation. Note that files must be located in this folder in order to be added as resources. Only a student in the class can determine what files to upload in a given submission-level resource folder. 
		Find more info here: https://learn.microsoft.com/graph/api/educationsubmission-setupresourcesfolder?view=graph-rest-beta
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)


	def with_url(self, raw_url: str) -> SetUpResourcesFolderRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SetUpResourcesFolderRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SetUpResourcesFolderRequest(self.request_adapter, self.path_parameters)

