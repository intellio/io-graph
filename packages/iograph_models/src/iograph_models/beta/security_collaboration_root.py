from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCollaborationRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	analyzedEmails: Optional[list[SecurityAnalyzedEmail]] = Field(alias="analyzedEmails", default=None,)

from .security_analyzed_email import SecurityAnalyzedEmail

