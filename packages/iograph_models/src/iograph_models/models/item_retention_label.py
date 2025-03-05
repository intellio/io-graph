from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemRetentionLabel(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isLabelAppliedExplicitly: Optional[bool] = Field(default=None,alias="isLabelAppliedExplicitly",)
	labelAppliedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="labelAppliedBy",)
	labelAppliedDateTime: Optional[datetime] = Field(default=None,alias="labelAppliedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	retentionSettings: Optional[RetentionLabelSettings] = Field(default=None,alias="retentionSettings",)

from .identity_set import IdentitySet
from .retention_label_settings import RetentionLabelSettings

