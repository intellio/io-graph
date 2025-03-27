from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyUploadedLanguageFileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GroupPolicyUploadedLanguageFile]] = Field(alias="value", default=None,)

from .group_policy_uploaded_language_file import GroupPolicyUploadedLanguageFile

