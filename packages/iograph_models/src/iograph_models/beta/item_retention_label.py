from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemRetentionLabel(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isLabelAppliedExplicitly: Optional[bool] = Field(alias="isLabelAppliedExplicitly",default=None,)
	labelAppliedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="labelAppliedBy",default=None,)
	labelAppliedDateTime: Optional[datetime] = Field(alias="labelAppliedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	retentionSettings: Optional[RetentionLabelSettings] = Field(alias="retentionSettings",default=None,)

from .identity_set import IdentitySet
from .retention_label_settings import RetentionLabelSettings

