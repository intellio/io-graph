from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	closedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="closedBy",default=None,)
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[EdiscoveryCaseStatus | str] = Field(alias="status",default=None,)
	custodians: Optional[list[EdiscoveryCustodian]] = Field(alias="custodians",default=None,)
	legalHolds: Optional[list[EdiscoveryLegalHold]] = Field(alias="legalHolds",default=None,)
	noncustodialDataSources: Optional[list[EdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialDataSources",default=None,)
	operations: SerializeAsAny[Optional[list[EdiscoveryCaseOperation]]] = Field(alias="operations",default=None,)
	reviewSets: Optional[list[EdiscoveryReviewSet]] = Field(alias="reviewSets",default=None,)
	settings: Optional[EdiscoveryCaseSettings] = Field(alias="settings",default=None,)
	sourceCollections: Optional[list[EdiscoverySourceCollection]] = Field(alias="sourceCollections",default=None,)
	tags: Optional[list[EdiscoveryTag]] = Field(alias="tags",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .ediscovery_case_status import EdiscoveryCaseStatus
from .ediscovery_custodian import EdiscoveryCustodian
from .ediscovery_legal_hold import EdiscoveryLegalHold
from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
from .ediscovery_case_operation import EdiscoveryCaseOperation
from .ediscovery_review_set import EdiscoveryReviewSet
from .ediscovery_case_settings import EdiscoveryCaseSettings
from .ediscovery_source_collection import EdiscoverySourceCollection
from .ediscovery_tag import EdiscoveryTag

