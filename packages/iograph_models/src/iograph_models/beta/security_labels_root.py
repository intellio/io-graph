from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityLabelsRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorities: Optional[list[SecurityAuthorityTemplate]] = Field(alias="authorities",default=None,)
	categories: Optional[list[SecurityCategoryTemplate]] = Field(alias="categories",default=None,)
	citations: Optional[list[SecurityCitationTemplate]] = Field(alias="citations",default=None,)
	departments: Optional[list[SecurityDepartmentTemplate]] = Field(alias="departments",default=None,)
	filePlanReferences: Optional[list[SecurityFilePlanReferenceTemplate]] = Field(alias="filePlanReferences",default=None,)
	retentionLabels: Optional[list[SecurityRetentionLabel]] = Field(alias="retentionLabels",default=None,)

from .security_authority_template import SecurityAuthorityTemplate
from .security_category_template import SecurityCategoryTemplate
from .security_citation_template import SecurityCitationTemplate
from .security_department_template import SecurityDepartmentTemplate
from .security_file_plan_reference_template import SecurityFilePlanReferenceTemplate
from .security_retention_label import SecurityRetentionLabel

