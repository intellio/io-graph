from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommitPostRequest(BaseModel):
	fileEncryptionInfo: Optional[FileEncryptionInfo] = Field(alias="fileEncryptionInfo", default=None,)

from .file_encryption_info import FileEncryptionInfo

