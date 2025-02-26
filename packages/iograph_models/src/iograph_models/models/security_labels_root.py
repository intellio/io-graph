from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityLabelsRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authorities: list[SecurityAuthorityTemplate] = Field(alias="authorities",)
	categories: list[SecurityCategoryTemplate] = Field(alias="categories",)
	citations: list[SecurityCitationTemplate] = Field(alias="citations",)
	departments: list[SecurityDepartmentTemplate] = Field(alias="departments",)
	filePlanReferences: list[SecurityFilePlanReferenceTemplate] = Field(alias="filePlanReferences",)
	retentionLabels: list[SecurityRetentionLabel] = Field(alias="retentionLabels",)

from .security_authority_template import SecurityAuthorityTemplate
from .security_category_template import SecurityCategoryTemplate
from .security_citation_template import SecurityCitationTemplate
from .security_department_template import SecurityDepartmentTemplate
from .security_file_plan_reference_template import SecurityFilePlanReferenceTemplate
from .security_retention_label import SecurityRetentionLabel

