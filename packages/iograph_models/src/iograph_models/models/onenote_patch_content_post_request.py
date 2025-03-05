from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Onenote_patch_contentPostRequest(BaseModel):
	commands: Optional[list[OnenotePatchContentCommand]] = Field(default=None,alias="commands",)

from .onenote_patch_content_command import OnenotePatchContentCommand

