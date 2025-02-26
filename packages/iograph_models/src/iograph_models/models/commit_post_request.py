from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommitPostRequest(BaseModel):
	fileEncryptionInfo: Optional[FileEncryptionInfo] = Field(default=None,alias="fileEncryptionInfo",)

from .file_encryption_info import FileEncryptionInfo

