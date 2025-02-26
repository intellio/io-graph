from __future__ import annotations
from pydantic import BaseModel, Field


class Onenote_patch_contentPostRequest(BaseModel):
	commands: list[OnenotePatchContentCommand] = Field(alias="commands",)

from .onenote_patch_content_command import OnenotePatchContentCommand

