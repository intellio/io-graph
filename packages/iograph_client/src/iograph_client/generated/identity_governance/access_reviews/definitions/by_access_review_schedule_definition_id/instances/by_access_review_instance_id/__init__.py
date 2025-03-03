# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .stages import StagesRequest
	from .stop import StopRequest
	from .send_reminder import SendReminderRequest
	from .reset_decisions import ResetDecisionsRequest
	from .batch_record_decisions import BatchRecordDecisionsRequest
	from .apply_decisions import ApplyDecisionsRequest
	from .accept_recommendations import AcceptRecommendationsRequest
	from .decisions import DecisionsRequest
	from .contacted_reviewers import ContactedReviewersRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.access_review_instance import AccessReviewInstance
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByAccessReviewInstanceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/definitions/{accessReviewScheduleDefinition%2Did}/instances/{accessReviewInstance%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewInstance:
		"""
		Get accessReviewInstance
		Read the properties and relationships of an accessReviewInstance object.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewinstance-get?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		Update accessReviewInstance
		Update the properties of an accessReviewInstance object. Only the reviewers and fallbackReviewers properties can be updated but the scope property is also required in the request body. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewInstance, it's status must be InProgress.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewinstance-update?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		Delete navigation property instances for identityGovernance
		
		"""
		tags = ['identityGovernance.accessReviewSet']
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

	@property
	def contacted_reviewers(self,
	) -> ContactedReviewersRequest:
		from .contacted_reviewers import ContactedReviewersRequest
		return ContactedReviewersRequest(self.request_adapter, self.path_parameters)

	@property
	def decisions(self,
	) -> DecisionsRequest:
		from .decisions import DecisionsRequest
		return DecisionsRequest(self.request_adapter, self.path_parameters)

	@property
	def accept_recommendations(self,
	) -> AcceptRecommendationsRequest:
		from .accept_recommendations import AcceptRecommendationsRequest
		return AcceptRecommendationsRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_decisions(self,
	) -> ApplyDecisionsRequest:
		from .apply_decisions import ApplyDecisionsRequest
		return ApplyDecisionsRequest(self.request_adapter, self.path_parameters)

	@property
	def batch_record_decisions(self,
	) -> BatchRecordDecisionsRequest:
		from .batch_record_decisions import BatchRecordDecisionsRequest
		return BatchRecordDecisionsRequest(self.request_adapter, self.path_parameters)

	@property
	def reset_decisions(self,
	) -> ResetDecisionsRequest:
		from .reset_decisions import ResetDecisionsRequest
		return ResetDecisionsRequest(self.request_adapter, self.path_parameters)

	@property
	def send_reminder(self,
	) -> SendReminderRequest:
		from .send_reminder import SendReminderRequest
		return SendReminderRequest(self.request_adapter, self.path_parameters)

	@property
	def stop(self,
	) -> StopRequest:
		from .stop import StopRequest
		return StopRequest(self.request_adapter, self.path_parameters)

	@property
	def stages(self,
	) -> StagesRequest:
		from .stages import StagesRequest
		return StagesRequest(self.request_adapter, self.path_parameters)

