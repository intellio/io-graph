from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationModule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isPinned: Optional[bool] = Field(default=None,alias="isPinned",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	resourcesFolderUrl: Optional[str] = Field(default=None,alias="resourcesFolderUrl",)
	status: Optional[EducationModuleStatus] = Field(default=None,alias="status",)
	resources: list[EducationModuleResource] = Field(alias="resources",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .education_module_status import EducationModuleStatus
from .education_module_resource import EducationModuleResource

