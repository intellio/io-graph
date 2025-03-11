from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequestorSettings(BaseModel):
	allowCustomAssignmentSchedule: Optional[bool] = Field(alias="allowCustomAssignmentSchedule",default=None,)
	enableOnBehalfRequestorsToAddAccess: Optional[bool] = Field(alias="enableOnBehalfRequestorsToAddAccess",default=None,)
	enableOnBehalfRequestorsToRemoveAccess: Optional[bool] = Field(alias="enableOnBehalfRequestorsToRemoveAccess",default=None,)
	enableOnBehalfRequestorsToUpdateAccess: Optional[bool] = Field(alias="enableOnBehalfRequestorsToUpdateAccess",default=None,)
	enableTargetsToSelfAddAccess: Optional[bool] = Field(alias="enableTargetsToSelfAddAccess",default=None,)
	enableTargetsToSelfRemoveAccess: Optional[bool] = Field(alias="enableTargetsToSelfRemoveAccess",default=None,)
	enableTargetsToSelfUpdateAccess: Optional[bool] = Field(alias="enableTargetsToSelfUpdateAccess",default=None,)
	onBehalfRequestors: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="onBehalfRequestors",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .subject_set import SubjectSet

