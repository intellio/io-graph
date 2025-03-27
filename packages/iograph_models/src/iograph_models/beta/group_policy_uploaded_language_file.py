from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyUploadedLanguageFile(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	languageCode: Optional[str] = Field(alias="languageCode", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


