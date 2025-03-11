from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentResourceRole(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	originId: Optional[str] = Field(alias="originId",default=None,)
	originSystem: Optional[str] = Field(alias="originSystem",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	accessPackageAssignments: Optional[list[AccessPackageAssignment]] = Field(alias="accessPackageAssignments",default=None,)
	accessPackageResourceRole: Optional[AccessPackageResourceRole] = Field(alias="accessPackageResourceRole",default=None,)
	accessPackageResourceScope: Optional[AccessPackageResourceScope] = Field(alias="accessPackageResourceScope",default=None,)
	accessPackageSubject: Optional[AccessPackageSubject] = Field(alias="accessPackageSubject",default=None,)

from .access_package_assignment import AccessPackageAssignment
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope
from .access_package_subject import AccessPackageSubject

