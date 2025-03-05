from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoverySearch(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	contentQuery: Optional[str] = Field(default=None,alias="contentQuery",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	dataSourceScopes: Optional[SecurityDataSourceScopes] = Field(default=None,alias="dataSourceScopes",)
	additionalSources: SerializeAsAny[Optional[list[SecurityDataSource]]] = Field(default=None,alias="additionalSources",)
	addToReviewSetOperation: Optional[SecurityEdiscoveryAddToReviewSetOperation] = Field(default=None,alias="addToReviewSetOperation",)
	custodianSources: SerializeAsAny[Optional[list[SecurityDataSource]]] = Field(default=None,alias="custodianSources",)
	lastEstimateStatisticsOperation: Optional[SecurityEdiscoveryEstimateOperation] = Field(default=None,alias="lastEstimateStatisticsOperation",)
	noncustodialSources: Optional[list[SecurityEdiscoveryNoncustodialDataSource]] = Field(default=None,alias="noncustodialSources",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .security_data_source_scopes import SecurityDataSourceScopes
from .security_data_source import SecurityDataSource
from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
from .security_data_source import SecurityDataSource
from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource

