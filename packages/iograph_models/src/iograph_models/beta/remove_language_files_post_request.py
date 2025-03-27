from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Remove_language_filesPostRequest(BaseModel):
	groupPolicyUploadedLanguageFiles: Optional[list[GroupPolicyUploadedLanguageFile]] = Field(alias="groupPolicyUploadedLanguageFiles", default=None,)

from .group_policy_uploaded_language_file import GroupPolicyUploadedLanguageFile

