from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFilePlanDescriptor(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authority: Optional[SecurityFilePlanAuthority] = Field(default=None,alias="authority",)
	category: Optional[SecurityFilePlanAppliedCategory] = Field(default=None,alias="category",)
	citation: Optional[SecurityFilePlanCitation] = Field(default=None,alias="citation",)
	department: Optional[SecurityFilePlanDepartment] = Field(default=None,alias="department",)
	filePlanReference: Optional[SecurityFilePlanReference] = Field(default=None,alias="filePlanReference",)
	authorityTemplate: Optional[SecurityAuthorityTemplate] = Field(default=None,alias="authorityTemplate",)
	categoryTemplate: Optional[SecurityCategoryTemplate] = Field(default=None,alias="categoryTemplate",)
	citationTemplate: Optional[SecurityCitationTemplate] = Field(default=None,alias="citationTemplate",)
	departmentTemplate: Optional[SecurityDepartmentTemplate] = Field(default=None,alias="departmentTemplate",)
	filePlanReferenceTemplate: Optional[SecurityFilePlanReferenceTemplate] = Field(default=None,alias="filePlanReferenceTemplate",)

from .security_file_plan_authority import SecurityFilePlanAuthority
from .security_file_plan_applied_category import SecurityFilePlanAppliedCategory
from .security_file_plan_citation import SecurityFilePlanCitation
from .security_file_plan_department import SecurityFilePlanDepartment
from .security_file_plan_reference import SecurityFilePlanReference
from .security_authority_template import SecurityAuthorityTemplate
from .security_category_template import SecurityCategoryTemplate
from .security_citation_template import SecurityCitationTemplate
from .security_department_template import SecurityDepartmentTemplate
from .security_file_plan_reference_template import SecurityFilePlanReferenceTemplate

