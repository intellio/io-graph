from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupSettingTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupSettingTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.groupSettingTemplate")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	values: Optional[list[SettingTemplateValue]] = Field(alias="values", default=None,)

from .setting_template_value import SettingTemplateValue
