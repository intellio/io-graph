from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Onenote_patch_contentPostRequest(BaseModel):
	commands: Optional[list[OnenotePatchContentCommand]] = Field(alias="commands", default=None,)

from .onenote_patch_content_command import OnenotePatchContentCommand
