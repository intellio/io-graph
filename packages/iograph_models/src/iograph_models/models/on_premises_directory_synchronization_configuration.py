from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesDirectorySynchronizationConfiguration(BaseModel):
	accidentalDeletionPrevention: Optional[OnPremisesAccidentalDeletionPrevention] = Field(alias="accidentalDeletionPrevention",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .on_premises_accidental_deletion_prevention import OnPremisesAccidentalDeletionPrevention

