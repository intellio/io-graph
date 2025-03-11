from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEmailContentThreatSubmission(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	adminReview: Optional[SecuritySubmissionAdminReview] = Field(alias="adminReview",default=None,)
	category: Optional[SecuritySubmissionCategory | str] = Field(alias="category",default=None,)
	clientSource: Optional[SecuritySubmissionClientSource | str] = Field(alias="clientSource",default=None,)
	contentType: Optional[SecuritySubmissionContentType | str] = Field(alias="contentType",default=None,)
	createdBy: Optional[SecuritySubmissionUserIdentity] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	result: Optional[SecuritySubmissionResult] = Field(alias="result",default=None,)
	source: Optional[SecuritySubmissionSource | str] = Field(alias="source",default=None,)
	status: Optional[SecurityLongRunningOperationStatus | str] = Field(alias="status",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	attackSimulationInfo: Optional[SecurityAttackSimulationInfo] = Field(alias="attackSimulationInfo",default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId",default=None,)
	originalCategory: Optional[SecuritySubmissionCategory | str] = Field(alias="originalCategory",default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime",default=None,)
	recipientEmailAddress: Optional[str] = Field(alias="recipientEmailAddress",default=None,)
	sender: Optional[str] = Field(alias="sender",default=None,)
	senderIP: Optional[str] = Field(alias="senderIP",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	tenantAllowOrBlockListAction: Optional[SecurityTenantAllowOrBlockListAction] = Field(alias="tenantAllowOrBlockListAction",default=None,)
	fileContent: Optional[str] = Field(alias="fileContent",default=None,)

from .security_submission_admin_review import SecuritySubmissionAdminReview
from .security_submission_category import SecuritySubmissionCategory
from .security_submission_client_source import SecuritySubmissionClientSource
from .security_submission_content_type import SecuritySubmissionContentType
from .security_submission_user_identity import SecuritySubmissionUserIdentity
from .security_submission_result import SecuritySubmissionResult
from .security_submission_source import SecuritySubmissionSource
from .security_long_running_operation_status import SecurityLongRunningOperationStatus
from .security_attack_simulation_info import SecurityAttackSimulationInfo
from .security_submission_category import SecuritySubmissionCategory
from .security_tenant_allow_or_block_list_action import SecurityTenantAllowOrBlockListAction

