from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequestorSettings(BaseModel):
	allowCustomAssignmentSchedule: Optional[bool] = Field(default=None,alias="allowCustomAssignmentSchedule",)
	enableOnBehalfRequestorsToAddAccess: Optional[bool] = Field(default=None,alias="enableOnBehalfRequestorsToAddAccess",)
	enableOnBehalfRequestorsToRemoveAccess: Optional[bool] = Field(default=None,alias="enableOnBehalfRequestorsToRemoveAccess",)
	enableOnBehalfRequestorsToUpdateAccess: Optional[bool] = Field(default=None,alias="enableOnBehalfRequestorsToUpdateAccess",)
	enableTargetsToSelfAddAccess: Optional[bool] = Field(default=None,alias="enableTargetsToSelfAddAccess",)
	enableTargetsToSelfRemoveAccess: Optional[bool] = Field(default=None,alias="enableTargetsToSelfRemoveAccess",)
	enableTargetsToSelfUpdateAccess: Optional[bool] = Field(default=None,alias="enableTargetsToSelfUpdateAccess",)
	onBehalfRequestors: list[SubjectSet] = Field(alias="onBehalfRequestors",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .subject_set import SubjectSet

