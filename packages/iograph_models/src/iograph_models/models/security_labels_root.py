from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityLabelsRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authorities: Optional[list[SecurityAuthorityTemplate]] = Field(default=None,alias="authorities",)
	categories: Optional[list[SecurityCategoryTemplate]] = Field(default=None,alias="categories",)
	citations: Optional[list[SecurityCitationTemplate]] = Field(default=None,alias="citations",)
	departments: Optional[list[SecurityDepartmentTemplate]] = Field(default=None,alias="departments",)
	filePlanReferences: Optional[list[SecurityFilePlanReferenceTemplate]] = Field(default=None,alias="filePlanReferences",)
	retentionLabels: Optional[list[SecurityRetentionLabel]] = Field(default=None,alias="retentionLabels",)

from .security_authority_template import SecurityAuthorityTemplate
from .security_category_template import SecurityCategoryTemplate
from .security_citation_template import SecurityCitationTemplate
from .security_department_template import SecurityDepartmentTemplate
from .security_file_plan_reference_template import SecurityFilePlanReferenceTemplate
from .security_retention_label import SecurityRetentionLabel

