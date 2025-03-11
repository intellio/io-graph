from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InformationalUrls(BaseModel):
	appSignUpUrl: Optional[str] = Field(alias="appSignUpUrl",default=None,)
	singleSignOnDocumentationUrl: Optional[str] = Field(alias="singleSignOnDocumentationUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


