from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoverySearch(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentQuery: Optional[str] = Field(alias="contentQuery",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	dataSourceScopes: Optional[str | SecurityDataSourceScopes] = Field(alias="dataSourceScopes",default=None,)
	additionalSources: SerializeAsAny[Optional[list[SecurityDataSource]]] = Field(alias="additionalSources",default=None,)
	addToReviewSetOperation: Optional[SecurityEdiscoveryAddToReviewSetOperation] = Field(alias="addToReviewSetOperation",default=None,)
	custodianSources: SerializeAsAny[Optional[list[SecurityDataSource]]] = Field(alias="custodianSources",default=None,)
	lastEstimateStatisticsOperation: Optional[SecurityEdiscoveryEstimateOperation] = Field(alias="lastEstimateStatisticsOperation",default=None,)
	noncustodialSources: Optional[list[SecurityEdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialSources",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .security_data_source_scopes import SecurityDataSourceScopes
from .security_data_source import SecurityDataSource
from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
from .security_data_source import SecurityDataSource
from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource

