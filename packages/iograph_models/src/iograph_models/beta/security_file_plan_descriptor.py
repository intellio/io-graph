from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityFilePlanDescriptor(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.filePlanDescriptor"] = Field(alias="@odata.type",)
	authority: Optional[SecurityFilePlanAuthority] = Field(alias="authority", default=None,)
	category: Optional[SecurityFilePlanAppliedCategory] = Field(alias="category", default=None,)
	citation: Optional[SecurityFilePlanCitation] = Field(alias="citation", default=None,)
	department: Optional[SecurityFilePlanDepartment] = Field(alias="department", default=None,)
	filePlanReference: Optional[SecurityFilePlanReference] = Field(alias="filePlanReference", default=None,)
	authorityTemplate: Optional[SecurityAuthorityTemplate] = Field(alias="authorityTemplate", default=None,)
	categoryTemplate: Optional[SecurityCategoryTemplate] = Field(alias="categoryTemplate", default=None,)
	citationTemplate: Optional[SecurityCitationTemplate] = Field(alias="citationTemplate", default=None,)
	departmentTemplate: Optional[SecurityDepartmentTemplate] = Field(alias="departmentTemplate", default=None,)
	filePlanReferenceTemplate: Optional[SecurityFilePlanReferenceTemplate] = Field(alias="filePlanReferenceTemplate", default=None,)

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
