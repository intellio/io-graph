# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .stages import StagesRequest
	from .stop_apply_decisions import StopApplyDecisionsRequest
	from .stop import StopRequest
	from .send_reminder import SendReminderRequest
	from .reset_decisions import ResetDecisionsRequest
	from .batch_record_decisions import BatchRecordDecisionsRequest
	from .apply_decisions import ApplyDecisionsRequest
	from .accept_recommendations import AcceptRecommendationsRequest
	from .definition import DefinitionRequest
	from .decisions import DecisionsRequest
	from .contacted_reviewers import ContactedReviewersRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_review_instance import AccessReviewInstance


class ByAccessReviewInstanceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/pendingAccessReviewInstances/{accessReviewInstance%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewInstance:
		"""
		Get pendingAccessReviewInstances from users
		Navigation property to get a list of access reviews pending approval by the reviewer.
		"""
		tags = ['users.accessReviewInstance']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstance, error_mapping)

	async def patch(
		self,
		body: AccessReviewInstance,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewInstance:
		"""
		Update the navigation property pendingAccessReviewInstances in users
		
		"""
		tags = ['users.accessReviewInstance']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstance, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property pendingAccessReviewInstances for users
		
		"""
		tags = ['users.accessReviewInstance']
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



	def with_url(self, raw_url: str) -> ByAccessReviewInstanceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessReviewInstanceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessReviewInstanceIdRequest(self.request_adapter, self.path_parameters)

	def contacted_reviewers(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> ContactedReviewersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .contacted_reviewers import ContactedReviewersRequest
		return ContactedReviewersRequest(self.request_adapter, path_parameters)

	def decisions(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> DecisionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .decisions import DecisionsRequest
		return DecisionsRequest(self.request_adapter, path_parameters)

	def definition(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> DefinitionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .definition import DefinitionRequest
		return DefinitionRequest(self.request_adapter, path_parameters)

	def accept_recommendations(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> AcceptRecommendationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .accept_recommendations import AcceptRecommendationsRequest
		return AcceptRecommendationsRequest(self.request_adapter, path_parameters)

	def apply_decisions(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> ApplyDecisionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .apply_decisions import ApplyDecisionsRequest
		return ApplyDecisionsRequest(self.request_adapter, path_parameters)

	def batch_record_decisions(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> BatchRecordDecisionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .batch_record_decisions import BatchRecordDecisionsRequest
		return BatchRecordDecisionsRequest(self.request_adapter, path_parameters)

	def reset_decisions(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> ResetDecisionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .reset_decisions import ResetDecisionsRequest
		return ResetDecisionsRequest(self.request_adapter, path_parameters)

	def send_reminder(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> SendReminderRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .send_reminder import SendReminderRequest
		return SendReminderRequest(self.request_adapter, path_parameters)

	def stop(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> StopRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .stop import StopRequest
		return StopRequest(self.request_adapter, path_parameters)

	def stop_apply_decisions(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> StopApplyDecisionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .stop_apply_decisions import StopApplyDecisionsRequest
		return StopApplyDecisionsRequest(self.request_adapter, path_parameters)

	def stages(self,
		user_id: str,
		accessReviewInstance_id: str,
	) -> StagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .stages import StagesRequest
		return StagesRequest(self.request_adapter, path_parameters)

