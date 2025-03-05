from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnenotePatchContentCommand(BaseModel):
	action: Optional[str | OnenotePatchActionType] = Field(alias="action",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	position: Optional[str | OnenotePatchInsertPosition] = Field(alias="position",default=None,)
	target: Optional[str] = Field(alias="target",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .onenote_patch_action_type import OnenotePatchActionType
from .onenote_patch_insert_position import OnenotePatchInsertPosition

