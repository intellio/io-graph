from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementTemplateCollectionTenantSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completeStepsCount: Optional[int] = Field(alias="completeStepsCount",default=None,)
	completeUsersCount: Optional[int] = Field(alias="completeUsersCount",default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	dismissedStepsCount: Optional[int] = Field(alias="dismissedStepsCount",default=None,)
	excludedUsersCount: Optional[int] = Field(alias="excludedUsersCount",default=None,)
	excludedUsersDistinctCount: Optional[int] = Field(alias="excludedUsersDistinctCount",default=None,)
	incompleteStepsCount: Optional[int] = Field(alias="incompleteStepsCount",default=None,)
	incompleteUsersCount: Optional[int] = Field(alias="incompleteUsersCount",default=None,)
	ineligibleStepsCount: Optional[int] = Field(alias="ineligibleStepsCount",default=None,)
	isComplete: Optional[bool] = Field(alias="isComplete",default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	managementTemplateCollectionDisplayName: Optional[str] = Field(alias="managementTemplateCollectionDisplayName",default=None,)
	managementTemplateCollectionId: Optional[str] = Field(alias="managementTemplateCollectionId",default=None,)
	regressedStepsCount: Optional[int] = Field(alias="regressedStepsCount",default=None,)
	regressedUsersCount: Optional[int] = Field(alias="regressedUsersCount",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	unlicensedUsersCount: Optional[int] = Field(alias="unlicensedUsersCount",default=None,)


