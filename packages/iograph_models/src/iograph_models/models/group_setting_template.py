from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class GroupSettingTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	values: list[SettingTemplateValue] = Field(alias="values",)

from .setting_template_value import SettingTemplateValue

