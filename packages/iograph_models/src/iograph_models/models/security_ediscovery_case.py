from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[SecurityCaseStatus] = Field(default=None,alias="status",)
	closedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="closedBy",)
	closedDateTime: Optional[datetime] = Field(default=None,alias="closedDateTime",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	custodians: Optional[list[SecurityEdiscoveryCustodian]] = Field(default=None,alias="custodians",)
	noncustodialDataSources: Optional[list[SecurityEdiscoveryNoncustodialDataSource]] = Field(default=None,alias="noncustodialDataSources",)
	operations: SerializeAsAny[Optional[list[SecurityCaseOperation]]] = Field(default=None,alias="operations",)
	reviewSets: Optional[list[SecurityEdiscoveryReviewSet]] = Field(default=None,alias="reviewSets",)
	searches: Optional[list[SecurityEdiscoverySearch]] = Field(default=None,alias="searches",)
	settings: Optional[SecurityEdiscoveryCaseSettings] = Field(default=None,alias="settings",)
	tags: Optional[list[SecurityEdiscoveryReviewTag]] = Field(default=None,alias="tags",)

from .identity_set import IdentitySet
from .security_case_status import SecurityCaseStatus
from .identity_set import IdentitySet
from .security_ediscovery_custodian import SecurityEdiscoveryCustodian
from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource
from .security_case_operation import SecurityCaseOperation
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_search import SecurityEdiscoverySearch
from .security_ediscovery_case_settings import SecurityEdiscoveryCaseSettings
from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

