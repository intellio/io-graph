from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCollaborationRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.collaborationRoot"] = Field(alias="@odata.type",)
	analyzedEmails: Optional[list[SecurityAnalyzedEmail]] = Field(alias="analyzedEmails", default=None,)

from .security_analyzed_email import SecurityAnalyzedEmail
