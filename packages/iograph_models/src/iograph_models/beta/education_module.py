from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationModule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isPinned: Optional[bool] = Field(alias="isPinned",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	resourcesFolderUrl: Optional[str] = Field(alias="resourcesFolderUrl",default=None,)
	status: Optional[EducationModuleStatus | str] = Field(alias="status",default=None,)
	resources: Optional[list[EducationModuleResource]] = Field(alias="resources",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .education_module_status import EducationModuleStatus
from .education_module_resource import EducationModuleResource

