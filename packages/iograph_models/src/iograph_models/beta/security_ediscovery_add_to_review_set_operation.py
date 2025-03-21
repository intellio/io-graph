from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryAddToReviewSetOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[SecurityCaseAction | str] = Field(alias="action",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status",default=None,)
	additionalDataOptions: Optional[SecurityAdditionalDataOptions | str] = Field(alias="additionalDataOptions",default=None,)
	cloudAttachmentVersion: Optional[SecurityCloudAttachmentVersion | str] = Field(alias="cloudAttachmentVersion",default=None,)
	documentVersion: Optional[SecurityDocumentVersion | str] = Field(alias="documentVersion",default=None,)
	itemsToInclude: Optional[SecurityItemsToInclude | str] = Field(alias="itemsToInclude",default=None,)
	reviewSet: Optional[SecurityEdiscoveryReviewSet] = Field(alias="reviewSet",default=None,)
	search: Optional[SecurityEdiscoverySearch] = Field(alias="search",default=None,)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_additional_data_options import SecurityAdditionalDataOptions
from .security_cloud_attachment_version import SecurityCloudAttachmentVersion
from .security_document_version import SecurityDocumentVersion
from .security_items_to_include import SecurityItemsToInclude
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_search import SecurityEdiscoverySearch

