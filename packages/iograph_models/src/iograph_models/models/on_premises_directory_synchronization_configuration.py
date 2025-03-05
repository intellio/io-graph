from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesDirectorySynchronizationConfiguration(BaseModel):
	accidentalDeletionPrevention: Optional[OnPremisesAccidentalDeletionPrevention] = Field(default=None,alias="accidentalDeletionPrevention",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .on_premises_accidental_deletion_prevention import OnPremisesAccidentalDeletionPrevention

