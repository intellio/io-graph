from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAnalyzedEmailAttachmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityAnalyzedEmailAttachment]] = Field(alias="value",default=None,)

from .security_analyzed_email_attachment import SecurityAnalyzedEmailAttachment

