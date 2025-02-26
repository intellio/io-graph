from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnenotePatchContentCommand(BaseModel):
	action: Optional[OnenotePatchActionType] = Field(default=None,alias="action",)
	content: Optional[str] = Field(default=None,alias="content",)
	position: Optional[OnenotePatchInsertPosition] = Field(default=None,alias="position",)
	target: Optional[str] = Field(default=None,alias="target",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .onenote_patch_action_type import OnenotePatchActionType
from .onenote_patch_insert_position import OnenotePatchInsertPosition

