from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementTemplateStepTenantSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignedTenantsCount: Optional[int] = Field(alias="assignedTenantsCount",default=None,)
	compliantTenantsCount: Optional[int] = Field(alias="compliantTenantsCount",default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	dismissedTenantsCount: Optional[int] = Field(alias="dismissedTenantsCount",default=None,)
	ineligibleTenantsCount: Optional[int] = Field(alias="ineligibleTenantsCount",default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	managementTemplateCollectionDisplayName: Optional[str] = Field(alias="managementTemplateCollectionDisplayName",default=None,)
	managementTemplateCollectionId: Optional[str] = Field(alias="managementTemplateCollectionId",default=None,)
	managementTemplateDisplayName: Optional[str] = Field(alias="managementTemplateDisplayName",default=None,)
	managementTemplateId: Optional[str] = Field(alias="managementTemplateId",default=None,)
	managementTemplateStepDisplayName: Optional[str] = Field(alias="managementTemplateStepDisplayName",default=None,)
	managementTemplateStepId: Optional[str] = Field(alias="managementTemplateStepId",default=None,)
	notCompliantTenantsCount: Optional[int] = Field(alias="notCompliantTenantsCount",default=None,)


