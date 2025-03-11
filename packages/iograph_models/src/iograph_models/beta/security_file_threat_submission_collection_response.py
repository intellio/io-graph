from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFileThreatSubmissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[SecurityFileThreatSubmission]]] = Field(alias="value",default=None,)

from .security_file_threat_submission import SecurityFileThreatSubmission

