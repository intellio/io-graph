from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoveryCase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[SecurityCaseStatus] = Field(default=None,alias="status",)
	closedBy: Optional[IdentitySet] = Field(default=None,alias="closedBy",)
	closedDateTime: Optional[datetime] = Field(default=None,alias="closedDateTime",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	custodians: list[SecurityEdiscoveryCustodian] = Field(alias="custodians",)
	noncustodialDataSources: list[SecurityEdiscoveryNoncustodialDataSource] = Field(alias="noncustodialDataSources",)
	operations: list[SecurityCaseOperation] = Field(alias="operations",)
	reviewSets: list[SecurityEdiscoveryReviewSet] = Field(alias="reviewSets",)
	searches: list[SecurityEdiscoverySearch] = Field(alias="searches",)
	settings: Optional[SecurityEdiscoveryCaseSettings] = Field(default=None,alias="settings",)
	tags: list[SecurityEdiscoveryReviewTag] = Field(alias="tags",)

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

