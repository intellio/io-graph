from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoverySourceCollection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentQuery: Optional[str] = Field(alias="contentQuery",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	dataSourceScopes: Optional[EdiscoveryDataSourceScopes | str] = Field(alias="dataSourceScopes",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	additionalSources: SerializeAsAny[Optional[list[EdiscoveryDataSource]]] = Field(alias="additionalSources",default=None,)
	addToReviewSetOperation: Optional[EdiscoveryAddToReviewSetOperation] = Field(alias="addToReviewSetOperation",default=None,)
	custodianSources: SerializeAsAny[Optional[list[EdiscoveryDataSource]]] = Field(alias="custodianSources",default=None,)
	lastEstimateStatisticsOperation: Optional[EdiscoveryEstimateStatisticsOperation] = Field(alias="lastEstimateStatisticsOperation",default=None,)
	noncustodialSources: Optional[list[EdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialSources",default=None,)

from .identity_set import IdentitySet
from .ediscovery_data_source_scopes import EdiscoveryDataSourceScopes
from .identity_set import IdentitySet
from .ediscovery_data_source import EdiscoveryDataSource
from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
from .ediscovery_data_source import EdiscoveryDataSource
from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation
from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

