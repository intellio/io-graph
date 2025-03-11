from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[SecurityCaseStatus | str] = Field(alias="status",default=None,)
	closedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="closedBy",default=None,)
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	custodians: Optional[list[SecurityEdiscoveryCustodian]] = Field(alias="custodians",default=None,)
	legalHolds: Optional[list[SecurityEdiscoveryHoldPolicy]] = Field(alias="legalHolds",default=None,)
	noncustodialDataSources: Optional[list[SecurityEdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialDataSources",default=None,)
	operations: SerializeAsAny[Optional[list[SecurityCaseOperation]]] = Field(alias="operations",default=None,)
	reviewSets: Optional[list[SecurityEdiscoveryReviewSet]] = Field(alias="reviewSets",default=None,)
	searches: Optional[list[SecurityEdiscoverySearch]] = Field(alias="searches",default=None,)
	settings: Optional[SecurityEdiscoveryCaseSettings] = Field(alias="settings",default=None,)
	tags: Optional[list[SecurityEdiscoveryReviewTag]] = Field(alias="tags",default=None,)

from .identity_set import IdentitySet
from .security_case_status import SecurityCaseStatus
from .identity_set import IdentitySet
from .security_ediscovery_custodian import SecurityEdiscoveryCustodian
from .security_ediscovery_hold_policy import SecurityEdiscoveryHoldPolicy
from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource
from .security_case_operation import SecurityCaseOperation
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_search import SecurityEdiscoverySearch
from .security_ediscovery_case_settings import SecurityEdiscoveryCaseSettings
from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

